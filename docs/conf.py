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
    "sphinx_copybutton",
    "manimextra.utils.docbuild.manim_directive",
    "manimextra.utils.docbuild.autocolor_directive",
    "manimextra.utils.docbuild.autoaliasattr_directive",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pillow": ("https://pillow.readthedocs.io/en/stable/", None),
}

html_theme_options = {
    "light_css_variables": {
        "color-content-foreground": "#000000",
        "color-background-primary": "#ffffff",
        "color-background-border": "#ffffff",
        "color-sidebar-background": "#f8f9fb",
        "color-brand-content": "#1c00e3",
        "color-brand-primary": "#192bd0",
        "color-link": "#c93434",
        "color-link--hover": "#5b0000",
        "color-inline-code-background": "#f6f6f6;",
        "color-foreground-secondary": "#000",
    },
    "dark_css_variables": {
        "color-content-foreground": "#ffffffd9",
        "color-background-primary": "#131416",
        "color-background-border": "#303335",
        "color-sidebar-background": "#1a1c1e",
        "color-brand-content": "#2196f3",
        "color-brand-primary": "#007fff",
        "color-link": "#51ba86",
        "color-link--hover": "#9cefc6",
        "color-inline-code-background": "#262626",
        "color-foreground-secondary": "#ffffffd9",
    },
}


templates_path = ['_templates']
html_static_path = ['static']
html_css_files = ['styles.css']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = "furo"

autosummary_generate = True
