


"""
change file version with:
bumpversion --current-version 1.2.0 minor setup.py algorithms3x/__init__.py
"""


import pathlib
from setuptools import find_packages, setup
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
    name="python-algorithms-3x",
    version="1.3.2",
    description="Python sorting and searching algorithms",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Harvard90873/algorithms",
    author="Harvard90873",
    author_email="harvard90873@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
    ],
    packages=["algorithms3x"],
    include_package_data=False,
    install_requires=[],
)