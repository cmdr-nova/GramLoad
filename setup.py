from setuptools import setup, find_packages

setup(
    name='gramload',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'instaloader',
    ],
    entry_points={
        'console_scripts': [
            'gramload=gramload.gramload:main',
        ],
    },
    author='cmdr-nova',
    author_email='net_run@mkultra.monster',
    description='A simple tool for downloading entire Instagram profiles.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cmdr-nova/gramload',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)