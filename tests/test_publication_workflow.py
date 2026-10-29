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


def test_spec_delivery_uses_canonical_aggregate_and_development_skill():
    config = yaml.safe_load((ROOT / ".pre-commit-config.yaml").read_text())
    pipelines = next(
        repo
        for repo in config["repos"]
        if repo["repo"] == "https://github.com/Knuckles-Team/pipelines"
    )
    assert pipelines["rev"] == CONTRACT
    assert [hook["id"] for hook in pipelines["hooks"]].count("spec") == 1

    skill = (
        ROOT / "ciso_assistant_api/skills/ciso-assistant-api-development/SKILL.md"
    ).read_text()
    assert "name: ciso-assistant-api-development" in skill
    assert "## Rapid delivery: the 5-minute contract" in skill
