import os
import sys

sys.path.insert(0, os.path.abspath('../'))

project = 'ManimExtra'
copyright = '2024, Merzlikin Matvey'
author = 'Merzlikin Matvey'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx.ext.autosummary",
    "manim.utils.docbuild.manim_directive",
    "manim.utils.docbuild.autocolor_directive",
    "manim.utils.docbuild.autoaliasattr_directive",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pillow": ("https://pillow.readthedocs.io/en/stable/", None),
}


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = "furo"
html_static_path = ['_static']



autosummary_generate = True

