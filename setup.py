from setuptools import setup
from distutils.core import setup
from beespammer.version import __version__

setup(
    name="bee-spammer",
    version=__version__,
    python_requires=">=3.6",
    description="A text spammer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="UltiRequiem",
    author_email="eliaz.bobadilladev@gmail.com",
    url="https://github.com/UltiRequiem/BeeSpammer.py",
    license="MIT",
    packages=["beespammer"],
    entry_points={"console_scripts": ["beespam = beespammer.beespammer:main"]},
)
