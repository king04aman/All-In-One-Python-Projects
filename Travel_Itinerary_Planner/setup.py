from setuptools import setup, find_packages

setup(
    name="task_manager_cli",  # Updated project name
    version="0.2",  # Updated version to reflect the new project
    packages=find_packages(where='src'),  # Automatically locate packages under 'src'
    package_dir={'': 'src'},  # Packages are located in the 'src' directory

    # Dependencies required for the updated functionality
    install_requires=[
        "pick==2.4.0",
        "python-dateutil>=2.8",  # For robust date validation
        "rich==14.2.0",         # FIRST ISSUE: For formatted table
        "colorama==0.4.6",
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "Pygments==2.19.1",
        "six==1.17.0",
        "coverage",
        "flake8==7.3.0",
        "pick==v2.4.0"
    ],

    # Project metadata
    author="Gabrielle",
    author_email="your-email@example.com",
)
