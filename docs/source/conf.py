# -*- coding: utf-8 -*-

import os
import sys
from deezepy import __version__
import datetime

sys.path.insert(0, os.path.abspath('.'))

project = 'deezepy'
copyright = '2020, CyanBook'
author = 'CyanBook'
version = __version__
release = version

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary'
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'

html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_context = {
    'version': version,
    'today': datetime.date.today().strftime('%B %d, %y'),
}
