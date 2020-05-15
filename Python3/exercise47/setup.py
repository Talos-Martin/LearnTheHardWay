try:
    from setuptools import setup
except ImportError
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'name',
        'url': 'http://www.ex47.tld'
        'download_url': 'http://www.ex47.tld/here.tgz',
        'author_email': 'a@bc.de',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex47'],
        'script': [],
        'name': 'exercise47'
        }

setup(**config)


