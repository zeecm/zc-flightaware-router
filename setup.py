from setuptools import find_packages, setup

PACKAGE = "zc_flightplan_toolkit"

setup(
    name="zc-flightplan-toolkit",
    version="0.0.1",
    packages=find_packages(include=PACKAGE),
    install_requires=[
        "pandas",
        "numpy",
        "python-dotenv",
        "requests",
        "pyside6",
        "loguru",
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
            "pycln",
            "pytest",
            "pytest-cov",
            "pytest-mock",
            "radon",
            "codespell",
            "pre-commit",
            "pyright",
            "pylint",
            "pyinstaller",
            "pytest-qt; platform_system=='Windows'",
        ]
    },
)
