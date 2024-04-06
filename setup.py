from setuptools import setup, find_packages

# Read the dependencies from requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='football-stats-scraper',
    version='0.1.7',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    author='John Murtagh',
    author_email='john90murtagh@gmail.com',
    description='A Python script to scrape football league tables and fixtures',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/murtaghj/football-cli',
    install_requires=required,
    entry_points={
        'console_scripts': [
            'football-cli=football_cli.__main__:entrypoint',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_data={'': ['requirements.txt']},
)
