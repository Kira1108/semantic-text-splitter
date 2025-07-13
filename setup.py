from setuptools import setup
from setuptools import find_packages

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

setup(name='semantic_splitter',
      version='0.0.1',
      description='fucking text splitter',
      author='The fastest man alive.',
      packages=find_packages(),
      install_requires=parse_requirements('requirements.txt')
)