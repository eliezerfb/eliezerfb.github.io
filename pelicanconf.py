#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Eliézer F. Bourchardt'
SITENAME = 'Eliézer Bourchardt Personal Blog'
SITEURL = 'eliezerfb.eti.br'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/eliezer-bourchardt/'),
          ('GitHub', 'https://github.com/eliezerfb'),
	  ('Twitter', 'https://twitter.com/eliezerfb'),
          ('Facebook', 'https://www.facebook.com/eliezer.bourchardt'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images','extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
