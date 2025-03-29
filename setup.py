from setuptools import setup, find_packages

setup(
    name="exclude_pages",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "exclude-pages = plugins.exclude_pages:ExcludePagesPlugin",
        ]
    },
)
