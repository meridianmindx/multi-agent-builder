"""Agent project templates for scaffolding AI agent projects.
Each template defines a complete project structure with a generator function.
"""

BASIC_TEMPLATES = {
    "basic": {
        "name": "Basic Agent",
        "description": "Minimal agent with a main loop and tools",
        "files": {
            "main.py": '''#!/usr/bin/env python3
"""Agent entry point."""
from agent_starter import generate_agent_project

def main():
    """Run the agent."""
    agent = Agent()
    agent.run()

if __name__ == "__main__":
    main()
''',
            "agent.py": '''"""Agent core logic."""

class Agent:
    """Main agent class."""

    def __init__(self):
        self.name = "my-agent"
        self.running = False

    def run(self):
        """Start the agent loop."""
        self.running = True
        print(f"Starting agent: {self.name}")
        while self.running:
            self.step()

    def step(self):
        """Single agent step."""
        pass

    def stop(self):
        """Stop the agent."""
        self.running = False
''',
            "tools.py": '''"""Tool implementations."""

class ToolRegistry:
    """Manages available tools."""

    def __init__(self):
        self.tools = {}

    def register(self, name, func):
        """Register a tool."""
        self.tools[name] = func

    def get(self, name):
        """Get a tool by name."""
        return self.tools.get(name)
''',
            "config.py": '''"""Configuration management."""

import os
from dataclasses import dataclass

@dataclass
class Config:
    """Agent configuration."""
    name: str = "default-agent"
    debug: bool = False

    @classmethod
    def from_env(cls):
        """Load from environment."""
        return cls(
            name=os.environ.get("AGENT_NAME", "default"),
            debug=os.environ.get("DEBUG", "false").lower() == "true",
        )
''',
            "README.md": "# {{PROJECT_NAME}}\n\nA minimal AI agent project.\n\n## Usage\n\n```bash\npython -m main\n```\n"
        }
    },
    "advanced": {
        "name": "Advanced Agent",
        "description": "Agent with memory, tools, and event loop",
        "files": {
            "main.py": '''#!/usr/bin/env python3
"""Agent entry point."""
from agent_starter import generate_agent_project

def main():
    """Run the agent."""
    agent = Agent()
    agent.run()

if __name__ == "__main__":
    main()
''',
            "agent.py": '''"""Agent core logic."""

class Agent:
    """Advanced agent with memory and tools."""

    def __init__(self):
        self.name = "advanced-agent"
        self.running = False
        self.memory = []

    def run(self):
        """Start the agent loop."""
        self.running = True
        print(f"Starting agent: {self.name}")
        while self.running:
            self.step()

    def step(self):
        """Single agent step."""
        pass

    def remember(self, item):
        """Remember an item."""
        self.memory.append(item)

    def recall(self, query):
        """Recall items matching query."""
        return [m for m in self.memory if query in m]
''',
            "tools.py": '''"""Tool implementations."""

class ToolRegistry:
    """Manages available tools."""

    def __init__(self):
        self.tools = {}

    def register(self, name, func):
        """Register a tool."""
        self.tools[name] = func

    def get(self, name):
        """Get a tool by name."""
        return self.tools.get(name)
''',
            "config.py": '''"""Configuration management."""

import os
from dataclasses import dataclass

@dataclass
class Config:
    """Agent configuration."""
    name: str = "advanced-agent"
    debug: bool = False
    memory_size: int = 100

    @classmethod
    def from_env(cls):
        """Load from environment."""
        return cls(
            name=os.environ.get("AGENT_NAME", "default"),
            debug=os.environ.get("DEBUG", "false").lower() == "true",
            memory_size=int(os.environ.get("MEMORY_SIZE", "100")),
        )
''',
            "README.md": "# {{PROJECT_NAME}}\n\nAn advanced AI agent project with memory and tools.\n\n## Usage\n\n```bash\npython -m main\n```\n"
        }
    },
}

AGENT_TPL = "basic"
