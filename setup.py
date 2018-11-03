from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='Manage users on a server using a JSON file inventory',
    long_description=readme,
    author='Rohit',
    author_email='rohitmungi@gmail.com',
    install_requires=['pytest','pytest-mock'],
    packages=find_packages('src'),
    package_dir={'':'src'},
    entry_points={
        'console_scripts': [
            'hr=hr.cli:main',
        ]
    }
)
