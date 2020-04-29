
from setuptools import setup, find_packages

setup(
    name                = 'NetflixParser',
    version             = '0.1.2',
    description         = 'Netflix parser',
    license             = 'MIT',
    author              = 'caterina',
    author_email        = 'dalgona91@gmail.com',
    url                 = 'https://github.com/CATERINA-SEUL/NetflixParser',
    download_url        = 'https://github.com/CATERINA-SEUL/WavveParser/archive/NetflixParser-0.1.2.tar.gz',
    install_requires    = [],
    long_description    = open('README.md').read(),
    long_description_content_type = "text/markdown",
    packages            = find_packages(exclude = []),
    keywords            = ['netflix'],
    package_data        = {},
    python_requires     = '>=3',
    py_modules          = ['NetflixParser'],
    include_package_data= True,
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
    ],
)
