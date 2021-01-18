"""Application entry point."""
from pathlib import Path

from kedro.framework.session import KedroSession
from mltemplate import PACKAGE_NAME


def run_package():
    # entry point for running pip-install projects
    # using `<project_package>` command

    # For PyCharm use
    # with KedroSession.create(package_name=PACKAGE_NAME, project_path=Path.cwd().parent.parent) as session:
    with KedroSession.create(package_name=PACKAGE_NAME, project_path=Path.cwd()) as session:
        project_context = session.load_context()
        project_context.run()


if __name__ == "__main__":
    # entry point for running pip-installed projects
    # using `python -m <project_package>.run` command
    run_package()
