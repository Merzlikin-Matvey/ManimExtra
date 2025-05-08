from manim import *
from manim.utils.testing.frames_comparison import frames_comparison
from manimextra import *

__module_test__ = "cevians_and_perpendiculars"


def _triangle_points():
    A = Dot(2 * DOWN + 3.5 * LEFT).set_z_index(1)
    B = Dot(2.5 * UP + 2 * LEFT).set_z_index(1)
    C = Dot(2 * DOWN + 3.5 * RIGHT)

    a = Line(B, C, color=BLUE)
    b = Line(A, C, color=BLUE)
    c = Line(A, B, color=BLUE)

    return A, B, C, a, b, c


@frames_comparison()
def test_cevian(scene):
    A, B, C, a, b, c = _triangle_points()
    cevian = Cevian(A, B, C, alpha=0.4, color=YELLOW)
    scene.add(A, B, C, a, b, c, cevian)


@frames_comparison()
def test_bisector(scene):
    A, B, C, a, b, c = _triangle_points()
    bisector = Bisector(A, B, C, color=YELLOW)
    angles = bisector.get_bisected_angles()
    scene.add(A, B, C, a, b, c, bisector, angles)


@frames_comparison()
def test_median(scene):
    A, B, C, a, b, c = _triangle_points()
    median = Median(A, B, C, color=YELLOW)
    segments = median.get_equal_segments()
    scene.add(A, B, C, a, b, c, median, segments)


@frames_comparison()
def test_symmedian(scene):
    A, B, C, a, b, c = _triangle_points()
    symmedian = Symmedian(A, B, C, color=YELLOW)
    scene.add(A, B, C, a, b, c, symmedian)


@frames_comparison()
def test_perpendicular(scene):
    A, B, C, a, b, c = _triangle_points()
    line = a
    dot = B
    perp = Perpendicular(line, dot, length=2, color=YELLOW)
    scene.add(A, B, C, a, b, c, perp)


@frames_comparison()
def test_perpendicular_bisector(scene):
    A, B, C, a, b, c = _triangle_points()
    bisector = PerpendicularBisector(a, length=2, color=YELLOW)
    angles = bisector.get_angles()
    scene.add(A, B, C, a, b, c, bisector, angles)


@frames_comparison()
def test_altitude(scene):
    A, B, C, a, b, c = _triangle_points()
    altitude = Altitude(A, B, C, color=YELLOW)
    scene.add(A, B, C, a, b, c, altitude)


@frames_comparison()
def test_euclid_line(scene):
    A, B, C, a, b, c = _triangle_points()
    euclid_line = EuclidLine(A, B, C, color=YELLOW)
    scene.add(A, B, C, a, b, c, euclid_line)
