try:
    from setuptools import setup
except ImportError
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'name',
        'url': 'http://www.something.com'
        'download_url': 'http://ge.me/here.tgz',
        'author_email': 'a@bc.de',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'script': [],
        'name': 'projectname'
        }

setup(**config)


