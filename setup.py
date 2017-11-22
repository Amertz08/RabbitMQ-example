from setuptools import setup

setup(name='example',
      version='0.1',
      py_modules=['app'],
      entry_points={
          'console_scripts': [
              'example=app:main'  # this line sets application command line alias
          ]
      },
)
