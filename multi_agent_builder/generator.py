"""Generator functions for scaffolding AI agent projects."""

import os
import shutil
from pathlib import Path


def list_templates():
    """Return available templates."""
    from agent_starter.templates import BASIC_TEMPLATES
    return [
        {"key": k, **v} for k, v in BASIC_TEMPLATES.items()
    ]


def generate_agent_project(template="basic", project_name="my-agent"):
    """Generate a new agent project from a template.

    Args:
        template: Template name ('basic' or 'advanced')
        project_name: Name for the project directory
    """
    from agent_starter.templates import BASIC_TEMPLATES

    tpl = BASIC_TEMPLATES.get(template)
    if not tpl:
        raise ValueError(f"Unknown template: {template}. Available: {list(BASIC_TEMPLATES.keys())}")

    # Create project directory
    project_dir = Path(project_name)
    project_dir.mkdir(exist_ok=True)

    # Render templates (replace {{VARIABLE}} placeholders)
    for filename, content in tpl["files"].items():
        rendered = content.replace("{{PROJECT_NAME}}", project_name)
        filepath = project_dir / filename
        filepath.parent.mkdir(exist_ok=True)
        filepath.write_text(rendered)

    # Make main.py executable
    (project_dir / "main.py").chmod(0o755)

    return str(project_dir)
