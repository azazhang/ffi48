from setuptools import setup, find_packages

setup(
    name='ffi48',
    version='0.1.0',
    packages=find_packages(),
    description='A package to classify SIC codes into Fama and French 48 industries',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ang Zhang',
    author_email='az@azhang.eu.org',
    url='https://github.com/azazhang/ffi48',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
