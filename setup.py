# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup, find_packages


here = os.path.dirname(__file__)
version = __import__('faq').get_version()


def get_long_desc():
    return open(os.path.join(here, 'README.rst')).read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py bdist_wheel upload -r natgeo')
    print("You probably want to also tag the version now:")
    print("  python setup.py tag")
    sys.exit()
elif sys.argv[-1] == 'tag':
    cmd = "git tag -a %s -m 'version %s';git push --tags" % (version, version)
    os.system(cmd)
    sys.exit()


setup(
    name='django-faq',
    version=version.replace(' ', '-'),
    description='Frequently Asked Question (FAQ) management for Django apps.',
    url='https://github.com/natgeosociety/django-faq/',
    author='Ben Spaulding',
    author_email='ben@benspaulding.us',
    license='BSD',
    long_description=get_long_desc(),
    packages=find_packages(exclude=['example*']),
    package_data={
        'faq': [
            'fixtures/*',
            'locale/*/LC_MESSAGES/*',
            'templates/faq/*',
            'templates/search/indexes/faq/*',
        ],
    },
    install_requires=['future'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
