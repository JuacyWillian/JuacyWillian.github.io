#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Juacy Willian'
ADDRESS_COM = ''
SITENAME = 'Juacy Willian'
SITESUBTITLE = 'Lorem ipsum dolor sit amet consectetur adipiscing elit, purus fusce per suscipit congue eget, urna vulputate quisque nullam cursus laoreet.'
# SITEURL = 'localhost:8000'
TIMEZONE = 'America/Sao_Paulo'

PATH = 'content'
RELATIVE_URLS = False
DEFAULT_PAGINATION = 10

# FEED CONFIG
RSS_FEED_SUMMARY_ONLY = True
ATOM_FEED_SUMMARY_ONLY = True
FEED_MAX_ITEMS = 10

# LANG CONFIG
LANGUAGES = (
    # ('code', 'name', 'url'),
    ('pt-br', 'Português do Brasil', 'lang/pt-br'),
    ('en', 'English', 'lang/en'),
)
DEFAULT_LANG = 'pt-br'

TWITTER_USERNAME = 'juacywillian'
GITHUB_URL = 'https://github.com/juacywillian/'
# DISQUS_SITENAME = ''
# GOOGLE_ANALYTICS = ''
# GA_COOKIE_DOMAIN = ''
# GOSQUARED_SITENAME = ''

# menuitems
DISPLAYMENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    # ('label', 'url'),
    # ('label', (('label', 'url'))),
    # ('Home', ''),
    # ('Todas as Categorias', 'categories.html'),
    # ('Todas as Tags', 'tags.html'),
    # ('Arquivo', 'archives.html'),
)

# Blogroll
LINKS = (
    # ('label', 'url'),
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    # ('label', 'url'),
    ('twitter', 'https://twitter.com/juacywillian'),
    # ('Another social link', '#'),
)

FOOTER_TEXT = '2018'


# Uncomment following line if you want document-relative URLs when developing

THEME = "pelican-themes/dev-random3"

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'tag_cloud',
    # 'langcategory'
]

# URL CONFIG
ARTICLE_URL = 'article/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'article/{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_LANG_URL = 'article/{date:%Y}/{date:%m}/{lang}/{slug}/'
ARTICLE_LANG_SAVE_AS = 'article/{date:%Y}/{date:%m}/{lang}/{slug}/index.html'

PAGE_URL = 'page/{slug}'
PAGE_SAVE_AS = 'page/{slug}.html'
PAGE_LANG_URL = "page/{slug}_{lang}.html"
PAGE_LANG_SAVE_AS = "page/{slug}_{lang}.html"

YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/index.html'

LANGUAGE_URL = 'lang/{lang}'
LANGUAGE_SAVE_AS = 'lang/{lang}.html'

# FEED_RSS = 'feeds/rss'
# FEED_ALL_RSS = 'feeds/rss/all.rss.xml'
# TRANSLATION_FEED_RSS = 'feeds/rss/all-{lang}.rss.xml'
# CATEGORY_FEED_RSS = 'feeds/rss/{slug}.rss.xml'
# AUTHOR_FEED_RSS = 'feeds/rss/{slug}.rss.xml'

# FEED_ATOM = 'feeds/atom'
# FEED_ATOM_ALL = 'feeds/atom/all.atom.xml'
# TRANSLATION_FEED_ATOM = 'feeds/atom/all-{lang}.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/atom/{slug}.atom.xml'
# AUTHOR_FEED_ATOM = 'feeds/atom/{slug}.atom.xml'
