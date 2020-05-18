try:
    from setuptools import setup
except ImportError
    from distutils.core import setup

config = {
        'description': 'My Project 48',
        'author': 'name',
        'url': 'http://www.ex48.tld'
        'download_url': 'http://www.ex48.tld/here.tgz',
        'author_email': 'a@bc.de',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex48'],
        'script': [],
        'name': 'exercise48'
        }

setup(**config)


