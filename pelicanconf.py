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
RELATIVE_URLS = True
DEFAULT_PAGINATION = 10

# FEED CONFIG
RSS_FEED_SUMMARY_ONLY = True
FEED_MAX_ITEMS = 10

# LANG CONFIG
LANGUAGES = (
    # ('code', 'name', 'url'),
    ('pt-br', 'Português do Brasil', 'pt-br'),
    ('en', 'English', 'en'),
)
DEFAULT_LANG = 'pt-br'

TWITTER_USERNAME = 'juacywillian'
GITHUB_URL = 'https:github.com/juacywillian'
# DISQUS_SITENAME = ''
# GOOGLE_ANALYTICS = ''
# GA_COOKIE_DOMAIN = ''
# GOSQUARED_SITENAME = ''

# menuitems
DISPLAYMENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    # ('Home', '/'),
    # ('Todas as Categorias', '/categories.html'),
    # ('Todas as Tags', '/tags.html'),
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
ARTICLE_LANG_URL = 'article/{lang}/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_LANG_SAVE_AS = 'article/{lang}/{date:%Y}/{date:%m}/{slug}/index.html'

PAGE_URL = 'page/{slug}/'
PAGE_SAVE_AS = 'page/{slug}/index.html'
PAGE_LANG_URL = "page/{lang}/{slug}.html"
PAGE_LANG_SAVE_AS = "page/{lang}/{slug}.html"

YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/index.html'

LANGUAGE_URL = 'lang/{lang}'
LANGUAGE_SAVE_AS = 'lang/{lang}/index.html'

FEED_ALL_RSS = 'feed/all.rss.xml'
CATEGORY_FEED_RSS = 'feed/{slug}.rss.xml'
AUTHOR_FEED_RSS = 'feed/{slug}.rss.xml'
TRANSLATION_FEED_RSS = 'feed/all-{lang}.rss.xml'

FEED_ALL_RSS = 'feed/all.rss.xml'
CATEGORY_FEED_RSS = 'feed/{slug}.rss.xml'
AUTHOR_FEED_RSS = 'feed/{slug}.rss.xml'
TRANSLATION_FEED_RSS = 'feed/all-{lang}.rss.xml'
