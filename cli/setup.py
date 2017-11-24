from setuptools import setup

setup(
    name='bots-cli',
    version='0.1',
    py_modules=['app'],
    install_requires=[
        'arrow==0.10.0',
        'pika==0.11.0',
        'pymongo==3.5.1'
    ],
    entry_points={
        'console_scripts': [
            'bots = app:main'
        ]
    },
)
