from setuptools import find_packages, setup

PACKAGE = "zc_flightaware_router"

setup(
    name="zc-flightaware-router",
    version="0.0.1",
    packages=find_packages(include=PACKAGE),
    install_requires=[
        "pandas",
        "numpy",
        "python-dotenv",
        "requests",
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
        ]
    },
)
