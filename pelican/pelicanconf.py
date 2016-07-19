#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'charlesreid1'
SITENAME = u'Asmodeus'

# If you are building this for Github, you need to use the site prefix /project-name
#SITEURL = '/asmodeus'

# If you are building this for local testing, you need to use the site prefix /
SITEURL=''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'




# --------------8<---------------------

THEME = 'atom-hammer-theme'




# Don't try to turn HTML files into pages
READERS = {'html': None}

STATIC_PATHS = ['images']

DISPLAY_PAGES_ON_MENU = False

TEMPLATE_PAGES = {'blog.html':'blog.html'}



# --------------8<---------------------



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

