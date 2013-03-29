# :coding: utf-8
# :copyright: Copyright (c) 2012 Martin Pengelly-Phillips
# :license: See LICENSE.txt.

'''Bark documentation build configuration file'''

# -- General ------------------------------------------------------------------

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Bark'
copyright = u'2012, Martin Pengelly-Phillips'

# Version
version = '?.?'
release = '?.?.?'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['static', 'template']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of prefixes to ignore for module listings
modindex_common_prefix = ['bark.']


# -- HTML output --------------------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['static']

# If True, copy source rst files to output for reference
html_copy_source = True


# -- Autodoc ------------------------------------------------------------------

autoclass_content = 'both'


# -- Intersphinx --------------------------------------------------------------

intersphinx_mapping = {'python':('http://docs.python.org/', None)}

