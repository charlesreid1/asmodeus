#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#
# Use this pelican configuration file when publishing to Github.

from __future__ import unicode_literals

AUTHOR = u'charlesreid1'
SITENAME = u'Asmodeus'

SITEURL = '/asmodeus'

PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
THEME = 'atom-hammer-theme'

# Don't try to turn HTML files into pages
READERS = {'html': None}
STATIC_PATHS = ['images']
DISPLAY_PAGES_ON_MENU = False
TEMPLATE_PAGES = {'blog.html':'blog.html'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = True

