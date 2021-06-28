# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='bitcoin_tools',

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.2.3',  # Required
    description='Bitcoin Tools',
    license='BSD3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/captain13128/bitcoin_tools',
    author='captain13128',
    packages=find_packages(include=['bitcoin_tools', 'bitcoin_tools.*']),  # Required
    python_requires='~=3.6',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'ecdsa',
        'python-bitcoinlib',
        'base58',
        'qrcode',
        'Pillow',
        'plyvel',
        'matplotlib',
        'numpy',
        'ujson',
        ],
)
