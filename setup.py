import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='hedgehog',
    version='0.0.1',
    author='Max Halford',
    license='MIT',
    author_email='maxhalford25@gmail.com',
    description='Bayesian networks in Python',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/MaxHalford/hedgehog',
    packages=['hedgehog'],
    python_requires='>=3.6',
    install_requires=[
        'pandas'
    ],
    extras_require={
        'dev': ['pytest'],
        'gui': ['graphviz', 'streamlit']
    },
    entry_points={
       'console_scripts': [
           'hedgehog=hedgehog:cli_hook'
       ],
    }
)

