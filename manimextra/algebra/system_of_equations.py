from manim import VGroup, BraceBetweenPoints
from manim.constants import *

from .bracket import BracketBetweenPoints

__all__ = [
    "SystemOfEquations"
]


class SystemOfEquations(VGroup):
    """
    A group of equations with a brace on the left side.

    Parameters
    ----------
    *equations : :class:`manim.mobject.Mobject`
        The equations.
    is_bracket : bool, optional
        Whether to use bracket instead of brace. Default to False.
    buff_between_equations : float, optional
        The buffer between equations. Default to 0.2.
    buff_between_brace_and_equations : float, optional
        The buffer between brace and equations. Default to 0.05.

    Examples
    --------
    .. manimextra:: SystemOfEquationsExample
        :save_last_frame:

        class SystemOfEquationsExample(Scene):
            def construct(self):
                system = SystemOfEquations(
                    MathTex("x^2", "+", "y^2", "=", "9"),
                    MathTex("y", "=", "x", "+", "1")
                )
                self.add(system)
    """
    def __init__(
            self,
            *equations,
            is_bracket=False,
            buff_between_equations=0.2,
            buff_between_brace_and_equations=0.05,
    ):
        self.equations = VGroup(*equations).arrange(DOWN, buff=buff_between_equations)
        self.is_bracket = is_bracket
        self.buff_between_equations = buff_between_equations
        self.buff_between_brace_and_equations = buff_between_brace_and_equations

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

    def swap(self, i, j):
        """
        Swap the i-th and j-th equations.
        :param i:
        :param j:
        :return:
        """
        self.equations[i], self.equations[j] = self.equations[j], self.equations[i]

        self.equations.arrange(DOWN, buff=self.buff_between_equations)
        max_width = max([equ.get_width() for equ in self.equations])
        for equ in self.equations:
            delta = (max_width - equ.get_width()) / 2
            equ.shift(LEFT * delta)

        self.brace.next_to(self.equations, LEFT, buff=self.buff_between_brace_and_equations)
        return self
