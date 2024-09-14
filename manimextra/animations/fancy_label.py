from __future__ import annotations

import manim
from manim.constants import *

__all__ = [
    "Fancy_label"
]


def Fancy_label(text: manim.Tex, mode='normal', buff=manim.MED_LARGE_BUFF):
    mode = mode.lower()
    modes = ['vlow', 'low', 'normal', 'fast', 'vfast']

    if mode not in modes:
        mode = 'normal'


    symbols = len(text.get_tex_string())
    time = (symbols / (9+modes.index(mode))) + 0.25

    return manim.AnimationGroup(manim.Write(text.to_edge(UP, buff=buff).set_z_index(999)), run_time=time)