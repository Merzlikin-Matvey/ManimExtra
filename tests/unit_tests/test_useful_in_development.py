from manim import *
from manimextra import *


def test_distance():
    test_num = 100
    for _ in range(test_num):
        x_1, y_1, x_2, y_2 = [np.random.uniform(-10, 10) for _ in range(4)]
        dot_1 = Dot([x_1, y_1, 0])
        dot_2 = Dot([x_2, y_2, 0])
        assert Line(dot_1, dot_2).get_length() == distance(dot_1, dot_2)


def test_circle_symmetry():
    test_num = 100
    for _ in range(test_num):
        x = np.random.uniform(-5, 5)
        y = np.random.uniform(-5, 5)

        dot = Dot([x, y, 0])
        r = 2
        circle = Circle(radius=r, color=WHITE)

        symmetry = circle_symmetry(circle, dot)
        d_1 = distance(circle.get_center(), dot)
        d_2 = distance(dot, symmetry)
        d_3 = distance(circle.get_center(), symmetry)

        if d_1 < r:
            assert np.isclose(d_1 + d_2, d_3)
        else:
            assert np.isclose(d_3 + d_2, d_1)

        assert np.isclose(d_1 * d_3, r ** 2)
