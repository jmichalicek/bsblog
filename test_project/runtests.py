#This file mainly exists to allow python setup.py test to work.
# based on http://ericholscher.com/blog/2009/jun/29/enable-setuppy-test-your-django-apps/
# except I can't manage to get this to actually work from setup.py.  It works standalone, though
# It does not seem to load fixtures, so back to the drawing board on this.
import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project.settings'

from django.conf import settings
from django.test.simple import DjangoTestSuiteRunner


test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)

def runtests(test_labels, verbosity=1,    interactive=True, extra_tests=None,
              **kwargs):
    """Test runner that only runs tests for the apps
    listed in "settings.TEST_APPS".
    """
    extra_tests = extra_tests or []
    app_labels = getattr(settings, 'TEST_APPS', test_labels)
    #return django_test_runner(app_labels, verbosity=verbosity,
    trunner = DjangoTestSuiteRunner()
    return trunner.run_tests(app_labels, verbosity=verbosity,
                              interactive=interactive,
                              extra_tests=extra_tests, **kwargs)

if __name__ == '__main__':
    runtests(['bsblog'])
