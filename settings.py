# Django settings for solanaABM010 project.
import os





PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
MENU_CACHE_TIME = -1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'solanaABM012',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-ar'
#ROSETTA_WSGI_AUTO_RELOAD

# Path a las traducciones
# que podria levantar el ROSETTA
LOCALE_PATHS = (
    #'/home/www/project/common_files/locale',
   # '/usr/local/lib/python2.6/dist-packages/django/contrib/admin/locale'
)


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = ''
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
#MEDIA_ROOT= ''
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/andrea/Dropbox/Andrea/solanaABMConMenu/solanaABM012/grappelli/'
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
#ADMIN_MEDIA_PREFIX = '/static/admin/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'# --volver a poner si anda mal grappelli
#ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
#ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
   # '/usr/local/lib/python2.6/dist-packages/django_grappelli-2.3.5-py2.6.egg/grappelli/static/grappelli',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'nevdhr9!nryzh=i6%6p5v7!^jgoognkki$3&rn0ko*txw0ihkx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'solanaABM012.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
      #'/home/andrea/solanaABM012/grappelli/templates',	    
    '/home/andrea/Dropbox/Andrea/solanaABMConMenu/solanaABM012/grappelli/',
    #"C:/solanaABM012/grappelli/templates",
    #"c:/solanaABM012/templates",
    
    # '/home/andrea/solanaABM012/treemenus/templates/admin/treemenus/menu',
  #   '/home/andrea/solanaABM012/templates/admin/edit_inline',
      
)
TEMPLATE_CONTEXT_PROCESSORS = (
		'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.request', 
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',     
                'snippets.1921.applist',
    # required by django.contrib.admin anyway
#    'django.core.context_processors.request',   c 
    #"django.core.context_processors.auth",
    # required by grappelli
#    'django.contrib.auth.context_processors.auth',
#    'django.core.context_processors.request',
    
    # required to render correct templates (grappelli+admin-tools or grappelli "standalone")
    #'grappelli.context_processors.admin_template_path',
)
INSTALLED_APPS = (
    'auth',
    'django.contrib.admindocs', 
    #'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  #  'django.contrib.sites',
    'sistema',
    'smart_selects',
    'clientes',
    'pruebas',
 #   'rosetta',
    'grappelli',
    'grappelli.dashboard',
    'django_extensions',

    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'south',
)

GRAPPELLI_ADMIN_TITLE = 'Solana SRL'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

import dj_database_url
DATABASES['default'] =  dj_database_url.config()
