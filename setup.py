from distutils.core import setup

setup(
    name='a',
    version='0.1.0',
    packages=['a'],
    package_data={'a': ['alias.yml']},
    entry_points={
        'console_scripts': [
            'a = a.__main__:main'
        ]
    },
    install_requires=['PyYAML']
)
