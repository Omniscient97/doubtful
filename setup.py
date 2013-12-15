try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setuptools

config = {
	'description': 'Doubtful; A text adventure in a western setting.',
	'author': 'Joshua Rowe & Liam Reeves',
	'url': 'toinputlater',
	'download_url': 'toenterlater',
	'author_email': 'joshuarowe1@icloud.com'
	'version': '0.0'
	'install_requires': ['nose'],
	'packages': ['Doubtful'],
	'scripts': [],
	'name': 'Doubtful'
}

setup(**config)