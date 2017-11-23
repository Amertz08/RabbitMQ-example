from setuptools import setup

setup(
    name='cli',
    version='0.1',
    py_modules=['app'],
    entry_points='''
        [console_scripts]
        db=app:cli
    ''',
)
