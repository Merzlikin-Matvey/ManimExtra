from manim import *
from manim.utils.testing.frames_comparison import frames_comparison
from manimextra import *

__module_test__ = "circles"

def _triangle_points():
    A = Dot(2 * DOWN + 3.5 * LEFT).set_z_index(1)
    B = Dot(2.5 * UP + 2 * LEFT).set_z_index(1)
    C = Dot(2 * DOWN + 3.5 * RIGHT)

    a = Line(B, C, color=BLUE)
    b = Line(A, C, color=BLUE)
    c = Line(A, B, color=BLUE)

    return A, B, C, a, b, c

@frames_comparison()
def test_incircle(scene):
    A, B, C, a, b, c = _triangle_points()
    incircle = Incircle(A, B, C)
    scene.add(A, B, C, a, b, c, incircle)

@frames_comparison()
def test_circumcircle(scene):
    A, B, C, a, b, c = _triangle_points()
    circumcircle = Circumcircle(A, B, C)
    scene.add(A, B, C, a, b, c, circumcircle)

@frames_comparison()
def test_nine_point_circle(scene):
    A, B, C, a, b, c = _triangle_points()
    nine_point_circle = NinePointCircle(A, B, C)
    scene.add(A, B, C, a, b, c, nine_point_circle)

@frames_comparison()
def test_carnot_circle(scene):
    A, B, C, a, b, c = _triangle_points()
    carnot_circle = CarnotCircle(A, B, C)
    scene.add(A, B, C, a, b, c, carnot_circle)