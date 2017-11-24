from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session='hack')

reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='bots-cli',
    version='0.1',
    py_modules=['app'],
    install_requires=reqs,
    entry_points='''
        [console_scripts]
        bots=app:main
    ''',
)
