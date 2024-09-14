from __future__ import annotations

import numpy as np
from .default import Line, Circle, Dot

__all__ = [
    "intersection_lines",
    "intersection_circles",
    "intersection_line_and_circle"
]


def intersection_lines(line_1: Line, line_2: Line) -> np.ndarray:
    x1, y1 = line_1.get_start()[0], line_1.get_start()[1],
    x2, y2 = line_1.get_end()[0], line_1.get_end()[1],
    x3, y3 = line_2.get_start()[0], line_2.get_start()[1],
    x4, y4 = line_2.get_end()[0], line_2.get_end()[1],
    try:
        x0 = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
            (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        y0 = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
            (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    except ZeroDivisionError:
        raise Exception("Lines are parallel")
    return np.array([x0, y0, 0])


def intersection_circles(circle_1: Circle, circle_2: Circle) -> tuple[np.ndarray, np.ndarray]:
    o1 = circle_1.get_center()
    o2 = circle_2.get_center()
    r1 = circle_1.radius
    r2 = circle_2.radius
    l = Line(o1, o2).get_length()

    if l > r1 + r2 + 0.02:
        raise Exception('Circles do not intersect')

    x1 = Dot(Line(o1, o2).set_length_about_point(r1, o1).get_end())
    x2 = x1.copy()

    alpha = np.arccos(round((r2 ** 2 - r1 ** 2 - l ** 2) / (-2 * r1 * l), 4))
    x1.rotate(about_point=o1, angle=alpha)
    x2.rotate(about_point=o1, angle=-alpha)

    return x1.get_center(), x2.get_center()


def intersection_line_and_circle(line: Line, circle: Circle) -> tuple[np.ndarray, np.ndarray]:
    o, r = circle.get_center(), circle.radius
    h = Line(line.get_projection(o), o).get_length()
    alpha = np.arccos(round(h / r, 4))
    x1 = Dot(Line(o, line.get_projection(o)).set_length_about_point(r, o).get_end())
    x2 = x1.copy()
    x1.rotate(about_point=o, angle=alpha)
    x2.rotate(about_point=o, angle=-alpha)
    return x1.get_center(), x2.get_center()
