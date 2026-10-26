"""Keep docs pushes separate from guarded package publication."""

from fnmatch import fnmatchcase
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = "main"


def _workflow(name):
    return yaml.safe_load((ROOT / ".github/workflows" / name).read_text())


def _push_matches(workflow, ref):
    # PyYAML's YAML 1.1 reader represents the Actions "on" key as True.
    push = workflow[True]["push"]
    kind, name = ref.removeprefix("refs/").split("/", 1)
    filters = push.get({"heads": "branches", "tags": "tags"}[kind], [])
    return any(fnmatchcase(name, pattern) for pattern in filters)


@pytest.mark.parametrize(
    "ref, expected",
    [
        ("refs/heads/main", True),
        ("refs/heads/docs-update", False),
        ("refs/tags/v2.1.0", False),
    ],
)
def test_only_main_starts_package_publication(ref, expected):
    assert _push_matches(_workflow("pipeline.yml"), ref) is expected


def test_each_package_publisher_uses_the_shared_pipelines():
    jobs = _workflow("pipeline.yml")["jobs"]
    assert set(jobs) == {"publish-pypi"}
    assert jobs["publish-pypi"]["uses"].endswith("/python_pipeline.yml@main")
    assert _workflow("pipeline.yml")[True]["push"]["paths-ignore"] == [
        "docker/Dockerfile",
        ".bumpversion.cfg",
    ]
    container = _workflow("container-release.yml")
    assert container[True]["push"] == {
        "branches": ["main"],
        "paths": ["docker/Dockerfile"],
    }
    assert container["jobs"]["publish-docker"]["needs"] == "verify-public-wheel"
    assert container["jobs"]["publish-docker"]["uses"].endswith(
        "/container_pipeline.yml@main"
    )
    for publisher in (jobs["publish-pypi"], container["jobs"]["publish-docker"]):
        assert "if" not in publisher
        assert not publisher.get("continue-on-error", False)
    guard = container["jobs"]["verify-public-wheel"]["steps"][-1]
    assert guard["with"] == {
        "mode": "published-wheel",
        "distribution": "ciso-assistant-api",
        "module": "ciso_assistant_api",
    }


def test_pages_keeps_shared_main_and_spec_triggers():
    workflow = _workflow("pages.yml")
    publisher = workflow["jobs"]["publish-pages"]
    assert publisher["uses"].endswith("/pages_pipeline.yml@main")
    assert publisher["with"]["spec_dashboard_enabled"] is True
    assert "specs/**" in workflow[True]["push"]["paths"]
    assert ".github/spec-dashboard.json" in workflow[True]["push"]["paths"]


def test_release_hook_inherits_catalogue_policy():
    config = yaml.safe_load((ROOT / ".pre-commit-config.yaml").read_text())
    matches = [
        (repo, hook)
        for repo in config["repos"]
        for hook in repo["hooks"]
        if hook["id"] == "dependency-readiness"
    ]
    assert len(matches) == 1
    repo, hook = matches[0]
    assert repo["repo"] == "https://github.com/Knuckles-Team/pipelines"
    assert repo["rev"] == CONTRACT
    assert hook == {"id": "dependency-readiness"}


@pytest.mark.parametrize(
    "path, expected",
    [
        ("docker/Dockerfile", False),
        (".bumpversion.cfg", False),
        ("pyproject.toml", True),
        ("uv.lock", True),
        ("ciso_assistant_api/mcp_server.py", True),
        ("README.md", True),
        (".github/workflows/pipeline.yml", True),
    ],
)
def test_package_publication_skips_only_container_pin_refresh(path, expected):
    ignores = _workflow("pipeline.yml")[True]["push"]["paths-ignore"]
    assert (not any(fnmatchcase(path, pattern) for pattern in ignores)) is expected
