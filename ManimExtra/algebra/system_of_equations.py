from manim import VGroup, BraceBetweenPoints
from manim.constants import *

from .bracket import BracketBetweenPoints

__all__ = [
    "SystemOfEquations"
]


class SystemOfEquations(VGroup):
    def __init__(
            self,
            *equations,
            is_bracket=False,
            buff_between_equations=0.2,
            buff_between_brace_and_equations=0.05,
    ):
        self.equations = VGroup(*equations).arrange(DOWN, buff=buff_between_equations)
        self.is_bracket = is_bracket

        max_width = max([equ.get_width() for equ in self.equations])
        for equ in self.equations:
            delta = (max_width - equ.get_width()) / 2
            equ.shift(LEFT * delta)

        if not is_bracket:
            self.brace = BraceBetweenPoints(
                self.equations[0].get_corner(UP + LEFT) + 0.1 * UP,
                self.equations[-1].get_corner(DOWN + LEFT) + 0.1 * DOWN,
            )
        else:
            self.brace = BracketBetweenPoints(
                self.equations[0].get_corner(UP + LEFT) + 0.1 * UP,
                self.equations[-1].get_corner(DOWN + LEFT) + 0.1 * DOWN,
            )

        self.brace.next_to(self.equations, LEFT, buff=buff_between_brace_and_equations)
        super().__init__(self.equations, self.brace)
