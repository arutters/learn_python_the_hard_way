try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project 1 project',
    'author': 'Annabelle',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Project1'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)