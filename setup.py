# python-example/setup.py
import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

entry_points = """
    [paste.app_factory]
    main = python_example:main
    [console_scripts]
    web = python_example:web
"""

setup(name='python_example',
      version='0.0.4',
      description='Flynn python example.',
      long_description=README,
      packages=find_packages(),
      entry_points=entry_points)
