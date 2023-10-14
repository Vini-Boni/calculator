from setuptools import setup

setup(
    name="calc",
    version="1.0.0",
    packages=["calculator"],
    entry_points={"console_scripts": ["mycalc = calculator.__main__:main"]},
)
