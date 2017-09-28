# -*- coding: utf-8 -*-

"""
A Frequently Asked Question (FAQ) management application for Django apps.

This Django_ application provides the ability to create and manage lists of
Frequently Asked Questions (FAQ), organized by topic.

This project is still under development, though several medium-to-large
websites are currently using it in production. The plan is to get a stable
version with a full test suite and documentation out the door in the coming
months.

.. _Django: http://www.djangoproject.com/

"""

__version_info__ = {
    'major': 0,
    'minor': 9,
    'micro': 1,
    'releaselevel': 'final',
    'serial': 1
}


def get_version(short=False):
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('%s%i' % (
            __version_info__['releaselevel'][0], __version_info__['serial']))
    return ''.join(vers)

__version__ = get_version()
