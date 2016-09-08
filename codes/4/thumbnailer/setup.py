from setuptools import setup


setup(
    name='thumbnailer',
    version='0.1.0',
    packages=['thumbnailer'],
    entry_points={
        'console_scripts': ['thumbnailer=thumbnailer.main:main'],
    },
)
