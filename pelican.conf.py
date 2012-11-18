AUTHOR = 'Ian Forsey'
SITENAME = "Just Some <em>Dev</em>"
SITETITLE = "Just Some Dev - Blogging about programming"
SITEDESCRIPTION = "Just Some Developer - Blogging about programming"

#SITEURL = ''
#TIMEZONE = ""

DISQUS_SITENAME = 'justsomedev'

DEFAULT_DATE_FORMAT = '%d %b %Y'
REVERSE_ARCHIVE_ORDER = True
TAG_CLOUD_STEPS = 8

ARTICLE_DIR='articles'
PAGE_DIR='pages'


THEME = 'notiansidea'

PATH = '/work/blog/content'
OUTPUT_PATH = '/work/theon.github.com'

MARKUP = 'md'
#MD_EXTENSIONS = 'extra'

FEED_RSS = 'feeds/all.rss.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

GOOGLE_ANALYTICS = 'UA-30513668-1'
#HTML_LANG = 'en'
#TWITTER_USERNAME = ''

#SOCIAL = (('Github.png', 'http://github.com/theon'),
#          ('Linkedin.png', 'http://www.linkedin.com/pub/ian-forsey/27/712/999'),
#	      ('Google-Plus.png', 'https://plus.google.com/111938457571698764905/posts'),
#	      ('Facebook.png', 'https://www.facebook.com/ian.forsey'))

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATS_ON_MENU = False
MENUITEMS = (('Home', '/'),
             ('Archive', '/archives.html'),
#	         ('Todo', '/pages/todo.html'),
             ('About', '/pages/about.html'))

PELICANGIT_PORT=8080
PELICANGIT_USER="ubuntu"

PELICANGIT_SOURCE_REPO="/work/blog"
PELICANGIT_SOURCE_REMOTE="origin"
PELICANGIT_SOURCE_BRANCH="master"

PELICANGIT_DEPLOY_REPO="/work/theon.github.com"
PELICANGIT_DEPLOY_REMOTE="origin"
PELICANGIT_DEPLOY_BRANCH="master"

PELICANGIT_WHITELISTED_FILES = [
    "README.md",
    "googled50a97559ea3af0e.html"
]
