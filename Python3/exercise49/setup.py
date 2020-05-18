try:
    from setuptools import setup
except ImportError
    from distutils.core import setup

config = {
        'description': 'My Project 49',
        'author': 'name',
        'url': 'http://www.ex49.tld'
        'download_url': 'http://www.ex49.tld/here.tgz',
        'author_email': 'a@bc.de',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex49'],
        'script': [],
        'name': 'exercise49'
        }

setup(**config)


