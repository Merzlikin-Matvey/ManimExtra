from __future__ import annotations

import manim
from manim.constants import *
from manim.utils.deprecation import deprecated

__all__ = [
    "Fancy_label"
]


@deprecated(since="v1.11.4", message="Please, dont use this cringe.")
def Fancy_label(text: manim.Tex, mode='normal', buff=manim.MED_LARGE_BUFF):
    """
    A function that writes text at the very top and adapts to its length

    Examples:
        .. manimextra:: FancyLabelExample

            class FancyLabelExample(manim.Scene):
                def construct(self):
                    label = Tex("Hello, World!")
                    self.play(Fancy_label(label))
                    self.wait()
    """

    mode = mode.lower()
    modes = ['vlow', 'low', 'normal', 'fast', 'vfast']

    if mode not in modes:
        mode = 'normal'

    symbols = len(text.get_tex_string())
    time = (symbols / (9 + modes.index(mode))) + 0.25

    return manim.AnimationGroup(manim.Write(text.to_edge(UP, buff=buff).set_z_index(999)), run_time=time)
