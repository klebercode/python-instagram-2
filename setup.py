#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="python-instagram-2",
    version="1.3.3.b",
    url="http://github.com/klebercode/python-instagram-2",
    license="MIT License",
    author="Kleber Soares",
    author_email="kleberss@gmail.com",
    keywords="instagram",
    description="Instagram API client",
    packages=find_packages(),
    install_requires=["simplejson", "httplib2", "six"],
    zip_safe=True,
)
