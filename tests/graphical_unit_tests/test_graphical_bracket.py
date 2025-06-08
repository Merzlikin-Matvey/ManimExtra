from manim import *
from manim.utils.testing.frames_comparison import frames_comparison
from manimextra import *

__module_test__ = "bracket"


@frames_comparison()
def test_bracket(scene):
    line = Line(color=RED)
    bracket = Bracket(line)
    scene.add(line, bracket)


@frames_comparison()
def test_bracket_direction(scene):
    square = Square(color=BLUE)
    bracket = Bracket(square, direction=RIGHT)
    scene.add(square, bracket)


@frames_comparison()
def test_bracket_between_points(scene):
    A = Dot(LEFT)
    B = Dot(RIGHT + UP)
    bracket = BracketBetweenPoints(A, B)
    scene.add(A, B, bracket)
