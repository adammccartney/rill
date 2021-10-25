#!/usr/bin/env python
import setuptools


if __name__ == "__main__":
    setuptools.setup(
        author="Adam McCartney",
        author_email="adam@mur.at",
        install_requires=(
            "abjad==3.1", 
            "abjad-ext-tonality", 
            "abjad-ext-rmakers"
        ),
        name="rill",
        packages=("rill",),
        url="https://github.com/adammccartney/rill",
        version="0.1",
        zip_safe=False,
    )
