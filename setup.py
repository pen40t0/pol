import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely."""
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


setup(
    name="polish_alphabet_converter",
    version="0.1.0",
    description="A script to replace Polish letters with ASCII equivalents.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Minh",
    url="https://github.com/definitelynotminh/polish",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
    entry_points={
        "console_scripts": ["polish=__main__:main"]
    },
    extras_require={"test": ["unittest"]},
    python_requires=">=3.5",
)
