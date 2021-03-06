from os.path import dirname, join, normpath, pardir

FILE_ROOT = normpath(join(dirname(__file__), pardir))

USE_I18N = True

MEDIA_ROOT = join(FILE_ROOT, '../tapz/media')

MEDIA_URL = '/media'

ADMIN_MEDIA_PREFIX = '/admin_media/'

ROOT_URLCONF = 'example_project.urls'

SITE_ID = 1

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    #'tapz.errors.middleware.ErrorPanelMiddleware',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(FILE_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
)

INSTALLED_APPS = (
    'djcelery',
    'tapz',
    'tapz.errors',
    'tapz.pagespeed',
)


