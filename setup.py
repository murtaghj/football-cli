from setuptools import setup, find_packages

setup(
    name='football-stats-scraper',
    version='0.1.8',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    author='John Murtagh',
    author_email='john90murtagh@gmail.com',
    description='A Python script to scrape football league tables and fixtures',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/murtaghj/football-cli',
    install_requires=[
        'beautifulsoup4',
        'certifi',
        'charset-normalizer',
        'idna',
        'lxml',
        'numpy',
        'pandas',
        'python-dateutil',
        'pytz',
        'requests',
        'six',
        'soupsieve',
        'tzdata',
        'urllib3'
    ],
    entry_points={
        'console_scripts': [
            'football-cli=football_cli.__main__:entrypoint',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
