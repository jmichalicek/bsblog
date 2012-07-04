from setuptools import setup, find_packages

package_data = ['templates/bsblog/*.html', 'static/bsblog/js/*', 'static/bsblog/css/*',
                'static/bsblog/img/*', 'fixtures/*,json', 'fixtures/*.xml']
dependencies = ['Markdown']
# Untested below... 
# dependency_links = ['https://github.com/jmichalicek/django-taxonomies/zipball/master#egg=django-taxonomies1.0']
setup(name = "bsblog",
      version = "0.0.1",
      description = "A django CMS/Blog app",
      author = "Justin Michalicek",
      author_email = "jmichalicek@gmail.com",
      license = "www.opensource.org/licenses/bsd-license.php",
      packages = find_packages(),
      #'package' package must contain files (see list above)
      package_data = {'bsblog' : package_data },
      install_requires = dependencies,
      long_description = """A django CMS/Blog app""" 
)
