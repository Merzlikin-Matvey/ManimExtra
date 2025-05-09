from manim import *
from manimextra import *
import numpy as np


def test_intersection_lines():
    line1 = Line(Dot([0, 0, 0]), Dot([2, 2, 0]))
    line2 = Line(Dot([0, 2, 0]), Dot([2, 0, 0]))
    expected = np.array([1, 1, 0])
    result = intersection_lines(line1, line2)
    assert np.allclose(result, expected)

    try:
        parallel_line1 = Line([0, 0, 0], [2, 2, 0])
        parallel_line2 = Line([1, 1, 0], [3, 3, 0])
        intersection_lines(parallel_line1, parallel_line2)

        assert False, "Exception not raised for parallel lines"
    except Exception:
        pass


def test_intersection_circles():
    circle1 = Circle(radius=5, color=WHITE)
    circle2 = Circle(radius=5, color=WHITE)
    circle2.shift(np.array([6, 0, 0]))

    p1, p2 = intersection_circles(circle1, circle2)
    for p in (p1, p2):
        d1 = np.linalg.norm(p - circle1.get_center())
        d2 = np.linalg.norm(p - circle2.get_center())
        assert np.isclose(d1, 5, atol=1e-2)
        assert np.isclose(d2, 5, atol=1e-2)

    circle3 = Circle(radius=5, color=WHITE)
    circle3.shift(np.array([11, 0, 0]))
    try:
        intersection_circles(circle1, circle3)
        assert False, "Exception not raised for non intersecting circles"
    except Exception:
        pass


def test_intersection_line_and_circle():
    circle = Circle(radius=5, color=WHITE)
    line = Line(Dot([-10, 0, 0]), Dot([10, 0, 0]))
    p1, p2 = intersection_line_and_circle(line, circle)

    if p1[1] > p2[1]:
        p1, p2 = p2, p1

    assert np.isclose(p1, [0, -5, 0]).all()
    assert np.isclose(p2, [0, 5, 0]).all()
