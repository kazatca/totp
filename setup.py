from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='totp',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'getpass',
    ],
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
)