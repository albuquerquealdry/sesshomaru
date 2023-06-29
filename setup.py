from setuptools import setup
setup(
    name = 'sesshomaru',
    version = '0.1.0',
    packages = ['./'],
    entry_points = {
        'console_scripts': [
            'sessho = main:main'
        ]
    })