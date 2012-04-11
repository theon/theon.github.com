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

#PATH = ''
THEME = 'notiansidea'

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
#	         ('Todo', '/pages/todo.html'),
             ('About', '/pages/about.html'))

SOURCE_GIT_REPO="/work/blog"
SOURCE_GIT_REMOTE="origin"
SOURCE_GIT_BRANCH="master"

DEPLOY_GIT_REPO="/work/theon.github.com"
DEPLOY_GIT_REMOTE="origin"
DEPLOY_GIT_BRANCH="master"

GIT_WHITELISTED_FILES = [
    "README.md",
    "googled50a97559ea3af0e.html"
]
