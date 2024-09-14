from __future__ import annotations

from ..useful_in_development import *

from .default import Line, Angle
from manim import VGroup
from manim.constants import PI

__all__ = [
    "Cevian",
    "Bisector",
    "Median",
    "Perpendicular",
    "Altitude",
    "PerpendicularBisector",
    "Symmedian",
    "EuclidLine",
]


class Cevian(Line):
    def __init__(self, A, B, C, alpha=0.35, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        D = Line(A, C).point_from_proportion(alpha)

        self.foot = D
        self.general_vertex = B
        self.extra_vertex_1 = A
        self.extra_vertex_2 = C
        self.proportion = alpha

        super().__init__(B, D, **kwargs)

    def get_foot(self) -> np.ndarray:
        return self.foot

    def get_vertex(self) -> np.ndarray:
        return self.general_vertex

    def get_proportion(self) -> float:
        return self.proportion


class Bisector(Cevian):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        alpha = ((Line(A, C).get_length() * Line(A, B).get_length()) /
                 (Line(B, C).get_length() + Line(A, B).get_length())) / Line(A, C).get_length()
        super().__init__(A, B, C, alpha, **kwargs)

    def get_bisected_angles(self, radius_alpha=1.1, *args, **kwargs) -> VGroup(Angle, Angle):
        first_angle = Angle.from_three_points(self.extra_vertex_1, self.general_vertex, self.foot, **kwargs)
        kwargs['radius'] = first_angle.radius * radius_alpha
        second_angle = Angle.from_three_points(self.extra_vertex_2, self.general_vertex, self.foot, **kwargs)
        return VGroup(first_angle, second_angle)


class Median(Cevian):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(A, B, C, 0.5, **kwargs)

    def get_equal_segments(self, **kwargs) -> VGroup(Line, Line):
        return VGroup(
            Line(self.extra_vertex_1, self.foot).equal(**kwargs),
            Line(self.extra_vertex_2, self.foot).equal(**kwargs),
        )


class Symmedian(Cevian):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        a, b, c = Line(B, C).get_length(), Line(A, C).get_length(), Line(A, B).get_length()
        alpha = c**2 / (a**2 + c**2)
        super().__init__(A, B, C, alpha=alpha, **kwargs)


class Perpendicular(Line):
    def __init__(self, line: Line, dot, length=1.0, rotate=False, **kwargs):
        X = dot_to_array(dot)[0]
        A, B = line.get_start(), line.get_end()
        if Line(A, B).is_point_in_line(X):
            perpendicular = Line(A, X).rotate(
                about_point=X, angle=PI / 2 + int(rotate) * PI).set_length_about_point(length, X)
        else:
            perpendicular = Line(X, Line(A, B).get_projection(X))

        self.vertex = X
        self.foot = Line(A, B).get_projection(X)
        self.line = line

        super().__init__(perpendicular.get_start(), perpendicular.get_end(), **kwargs)

    def get_line(self) -> Line:
        return self.linez

    def get_vertex(self) -> np.ndarray:
        return self.vertex

    def get_foot(self) -> np.ndarray:
        return self.foot

    def get_angles(self, **kwargs):
        return VGroup(
            Angle.from_three_points(self.vertex, self.dot, self.line.get_start(), elbow=True, **kwargs),
            Angle.from_three_points(self.vertex, self.dot, self.line.get_end(), elbow=True, **kwargs)
        )


class PerpendicularBisector(Line):
    def __init__(self, line: Line, length=1, **kwargs):
        line_1 = Perpendicular(line=line, dot=line.get_center(), length=length / 2, rotate=False)
        line_2 = Perpendicular(line=line, dot=line.get_center(), length=length / 2, rotate=True)

        self.dot = line.get_center()
        self.line = line

        super().__init__(line_1.get_end(), line_2.get_end(), **kwargs)

    def get_angles(self, **kwargs):
        return VGroup(
            Angle.from_three_points(self.line.get_start(), self.dot, self.get_start(), **kwargs),
            Angle.from_three_points(self.line.get_start(), self.dot, self.get_end(), **kwargs),
            Angle.from_three_points(self.line.get_end(), self.dot, self.get_start(), **kwargs),
            Angle.from_three_points(self.line.get_end(), self.dot, self.get_end(), **kwargs),
        )


class Altitude(Perpendicular):

    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        line = Line(A, C)
        super().__init__(line, B, **kwargs)


class EuclidLine(Line):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        line = Line(A, C).move_to(B)
        super().__init__(line.get_start(), line.get_end(), **kwargs)
