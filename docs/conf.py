import sys, os

extensions = []
templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = 'django-announcements'
package = 'announcements'
copyright_holder = 'Eldarion'
copyright = '2013, %s' % copyright_holder
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
htmlhelp_basename = '%sdoc' % project
latex_documents = [
  ('index', '%s.tex' % project, '%s Documentation' % project,
   copyright_holder, 'manual'),
]
man_pages = [
    ('index', project, '%s Documentation' % project,
     [copyright_holder], 1)
]

sys.path.insert(0, os.pardir)
m = __import__(package)

version = m.__version__
release = version
