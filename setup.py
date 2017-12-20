#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'schematics',
    'jsonschema'
]

test_requirements = [
    'flake8==2.6.0',
    'tox == 2.3.1',
    'coverage == 4.1',
    'Sphinx == 1.4.8',
    'schematics == 1.1.1',
    'jsonschema',
    'mock'
]

setup(
    name='schematics_flexible',
    version='0.1.2',
    description="",
    long_description=readme + '\n\n' + history,
    author="Serbokryl Oleg",
    author_email='oleh.serbokryl@unity-bars.com',
    url='https://github.com/Krokop/schematics-flexible',
    packages=[
        'schematics_flexible',
    ],
    package_dir={'schematics_flexible':
                 'schematics_flexible'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='schematics_flexible',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
