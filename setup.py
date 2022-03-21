from setuptools import setup, find_packages
from pathlib import Path
from taskquant import __version__


setup(
    name="taskquant",
    version=__version__,
    description="A python CLI that extends taskwarrior for productivity scoreboard & gamification (quantified self)",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/onlyphantom/taskquant",
    author="Samuel Chan",
    author_email="s@supertype.ai",
    license="MIT",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    include_package_data=True,
    install_requires=["tasklib"],
    extra_requires=["tabulate"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System" " :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "tq=taskquant.__main__:main",
        ]
    },
    python_requires=">=3.7",
)
