from manim import *
from manimextra import *


def _triangle_points():
    A = Dot(2 * DOWN + 3.5 * LEFT).set_z_index(1)
    B = Dot(2.5 * UP + 2 * LEFT).set_z_index(1)
    C = Dot(2 * DOWN + 3.5 * RIGHT)

    a = Line(B, C, color=BLUE)
    b = Line(A, C, color=BLUE)
    c = Line(A, B, color=BLUE)

    return A, B, C, a, b, c



def test_bisector():
    A, B, C, a, b, c = _triangle_points()
    bisector = Bisector(A, B, C)
    bisector_foot = bisector.get_foot()

    angle_1 = Angle.from_three_points(A, B, bisector_foot)
    angle_2 = Angle.from_three_points(C, B, bisector_foot)

    assert np.isclose(angle_1.get_value(), angle_2.get_value())

def test_cevian_division():
    A, B, C, a, b, c = _triangle_points()
    alpha = 0.4
    cevian = Cevian(A, B, C, alpha=alpha)
    foot = cevian.get_foot()
    print(foot)

    AC = b.get_length()
    AF = Line(A, foot).get_length()
    ratio = AF / AC
    assert np.isclose(ratio, alpha)


