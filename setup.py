# setup.py
from setuptools import setup, find_packages
import os

# Handle long_description safely
long_description = ""
if os.path.exists('README.md'):
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='NWIS_Data_Downloader',  # Change this if you want a different package name
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.0',
        'pandas>=1.3.0',
        'tqdm>=4.62.0',
    ],
    author='Your Name',  # Customize as needed
    description='A package to fetch and process USGS NWIS daily water data',
    long_description=long_description,
    long_description_content_type='text/markdown',  # If using Markdown in README
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)