#!/usr/bin/env python3
"""CLI entry point for multi_agent_builder."""

import sys
from multi_agent_builder.generator import list_templates, generate_agent_project


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m multi_agent_builder {list|generate}")
        return

    cmd = sys.argv[1]
    if cmd == "list":
        templates = list_templates()
        for t in templates:
            print(f"- {t['name']}")
            print(f"  {t['description']}")
    elif cmd == "generate":
        template = sys.argv[2] if len(sys.argv) > 2 else "basic"
        name = sys.argv[3] if len(sys.argv) > 3 else "my-agent"
        path = generate_agent_project(template=template, project_name=name)
        print(f"Created project at: {path}")
    else:
        print(f"Unknown command: {cmd}")
        print("Use 'list' or 'generate'")


if __name__ == "__main__":
    main()
