#!/usr/bin/env python3

import os
import io
import re
import ast

from setuptools import setup, find_packages

DEPENDENCIES=['click>=8.1', 'importlib-metadata', 'pathlib', 'numpy', 'pandas', 'multiprocess']
EXCLUDE_FROM_PACKAGES=["contrib", "docs", "tests*"]
CURDIR=os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as readme_file:
    readme=readme_file.read()

setup(
    name="scGPT",
    author="Haotian",
    author_email="subercui@gmail.com",
    python_requires=">=3.8",
    description="Large-scale generative pretrain of single cell using transformer.",
    install_requires=DEPENDENCIES,
    packages=find_packages(
        where='scgpt',
        exclude=EXCLUDE_FROM_PACKAGES
        ),
    package_dir={},
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=[],
    scripts=[],
    setup_requires=[],
    entry_points={},
		url="https://github.com/bowang-lab/scGPT",
    version='0.1.2.post1',
    zip_safe=False,
    license="MIT license",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
)
