import os
from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

PACKAGE_NAME = 'ha-philipsjs'
HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = '2.7.2'

PACKAGES = find_packages(exclude=['tests', 'tests.*', 'dist', 'ccu', 'build'])

REQUIRES = [
    "cryptography",
    "httpx",
]

setup(
        name=PACKAGE_NAME,
        version=VERSION,
        license='MIT License',
        url='https://github.com/danielperna84/ha-philipsjs',
        download_url='https://github.com/danielperna84/ha-philipsjs/tarball/'+VERSION,
        author='Daniel Perna',
        author_email='danielperna84@gmail.com',
        description='jointSPACE API for Home-Assistant',
        long_description=readme(),
        long_description_content_type='text/markdown',
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
        platforms='any',
        install_requires=REQUIRES,
        keywords=['jointSPACE'],
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.8'
        ],
        extras_require={
            'tests': [
                'pytest>3.6.4',
                'pytest-cov<2.6',
                'pytest-aiohttp',
                'coveralls',
                'pytest-mock',
                'respx>=0.16.2',
            ]
        },
        python_requires='>=3.8'
)
