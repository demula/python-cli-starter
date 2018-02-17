from setuptools import setup

setup(
    name='python-cli-starter',
    version='0.1.0',
    description='Starter project for python CLI utils',
    url='https://github.com/demula/python-cli-starter',
    author='Jesus de Mula Cano',
    author_email='demula@gmail.com',
    py_modules=['app'],
    include_package_data=True,
    test_suite='nose2.collector.collector',
    install_requires=[
        'click==6.7',
    ],
    extras_require={
        'dev': [
            'nose2==0.6.5'
        ]
    },
    entry_points='''
        [console_scripts]
        app_cli=app.cli:cli_main
    ''',
)
