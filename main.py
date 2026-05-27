"""Central launcher for the projects in this repository."""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SKIP_DIRECTORIES = {'.git', '.github', '__pycache__'}
ENTRYPOINT_NAMES = (
    'main.py',
    'app.py',
    'calculate.py',
    'generate.py',
    'track.py',
    'translate.py',
    'validate.py',
)


@dataclass(frozen=True)
class Project:
    name: str
    directory: Path
    entrypoint: Path


def find_entrypoint(project_dir: Path) -> Path | None:
    """Return the best Python entrypoint for a project directory."""
    for filename in ENTRYPOINT_NAMES:
        candidate = project_dir / filename
        if candidate.is_file():
            return candidate

    python_files = sorted(
        path for path in project_dir.glob('*.py')
        if path.name != Path(__file__).name
    )
    if python_files:
        return python_files[0]
    return None


def discover_projects(root: Path = ROOT) -> list[Project]:
    """Find top-level project folders that contain a runnable Python file."""
    projects: list[Project] = []
    for child in sorted(root.iterdir(), key=lambda path: path.name.lower()):
        if not child.is_dir() or child.name in SKIP_DIRECTORIES or child.name.startswith('.'):
            continue
        entrypoint = find_entrypoint(child)
        if entrypoint is None:
            continue
        projects.append(Project(child.name, child, entrypoint))
    return projects


def print_projects(projects: list[Project]) -> None:
    if not projects:
        print('No runnable projects were found.')
        return

    width = len(str(len(projects)))
    print('Available projects:')
    for index, project in enumerate(projects, start=1):
        relative_entrypoint = project.entrypoint.relative_to(ROOT).as_posix()
        print(f'{index:>{width}}. {project.name} ({relative_entrypoint})')


def resolve_selection(selection: str, projects: list[Project]) -> Project | None:
    normalized = selection.strip().lower()
    if normalized.isdigit():
        index = int(normalized) - 1
        if 0 <= index < len(projects):
            return projects[index]

    for project in projects:
        if project.name.lower() == normalized:
            return project
    return None


def run_project(project: Project) -> int:
    print(f'Launching {project.name}...')
    print(f'Entrypoint: {project.entrypoint.relative_to(ROOT).as_posix()}')
    completed = subprocess.run(
        [sys.executable, str(project.entrypoint)],
        cwd=project.directory,
        check=False,
    )
    return completed.returncode


def interactive_menu(projects: list[Project]) -> int:
    while True:
        print_projects(projects)
        choice = input("Enter a project number/name to run, or 'q' to quit: ").strip()
        if choice.lower() in {'q', 'quit', 'exit'}:
            return 0

        project = resolve_selection(choice, projects)
        if project is None:
            print('Invalid selection. Please try again.\n')
            continue
        return run_project(project)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Launch any Python project in this repository.')
    parser.add_argument('--list', action='store_true', help='List available projects and exit.')
    parser.add_argument('--run', metavar='PROJECT', help='Run a project by number or exact folder name.')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    projects = discover_projects()

    if args.list:
        print_projects(projects)
        return 0

    if args.run:
        project = resolve_selection(args.run, projects)
        if project is None:
            print(f"Project not found: {args.run}", file=sys.stderr)
            return 1
        return run_project(project)

    return interactive_menu(projects)


if __name__ == '__main__':
    raise SystemExit(main())
