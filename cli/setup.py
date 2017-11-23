from setuptools import setup

setup(
    name='bots-cli',
    version='0.1',
    py_modules=['app'],
    entry_points='''
        [console_scripts]
        bots=app:main
    ''',
)
