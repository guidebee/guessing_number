
from setuptools import find_packages, setup

setup(
    name="guessing_number",
    version="0.0.1",
    install_requires=["gym>=0.2.3", "numpy"],
    packages=find_packages(),
)
