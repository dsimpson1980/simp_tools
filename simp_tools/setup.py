from setuptools import setup
import yaml

with open('meta.yaml') as f:
    meta = yaml.load(f)

setup(name=meta['package']['name'],
      version=meta['package']['version'],
      description='Simple tools for sharing between repos',
      url='http://github.com/dsimpson1980/simp_tools',
      author='Dave Simpson',
      author_email='davesimpson1980@gmail.com',
      license='MIT',
      packages=['simp_tools'])