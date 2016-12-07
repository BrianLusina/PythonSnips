#!/usr/bin/env python

# Python 2.*/3.* imports
try:
    from distutils.core import setup
except ImportError:
    from setuptools import setup

from pysnips import constants

setup(
    name='PySnips',
    version=constants.PYSNIPS_VERSION,
    description='A Python library containing small Python algorithms',
    author='Brian Lusina (@brianlusina)',
    author_email='lusinabrian@gmail.com',
    url='https://github.com/BrianLusina/Python_Snippets',
    packages=['pysnips', 'tests', 'pyowm.caches', 'pyowm.commons',
              'pyowm.exceptions', 'pyowm.utils', 'pyowm.webapi25',
              'pyowm.webapi25.cityids', 'pyowm.webapi25.xsd',
              'tests.unit', 'tests.functional'],
    install_requires=['nose', "nose2", "pytest"],
    long_description=open("README.md").read(),
    classifiers=[
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python",
      "Natural Language :: English",
      "Operating System :: OS Independent",
      "Development Status :: 5 - Production/Stable",
      "Intended Audience :: Developers",
      "Topic :: Software Development :: Libraries"],
    package_data={
        '': ['*.txt', '*.xsd']
    },
    keywords='Python snippets and algorithms',
    license='MIT',
    test_suite='tests'
)