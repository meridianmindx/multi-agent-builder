"""
multi_agent_builder - CLI for scaffolding AI agent projects.

Usage:
    python -m multi_agent_builder list        # List available templates
    python -m multi_agent_builder generate    # Interactively scaffold a project

API usage:
    from multi_agent_builder import generate_agent_project
    generate_agent_project(template='basic', project_name='my-agent')
"""

from multi_agent_builder.templates import AGENT_TPL, BASIC_TEMPLATES
from multi_agent_builder.generator import generate_agent_project, list_templates

__all__ = ['generate_agent_project', 'list_templates', 'AGENT_TPL', 'BASIC_TEMPLATES']
