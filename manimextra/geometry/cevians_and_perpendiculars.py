from __future__ import annotations

from .default import Line, Angle
from manim import VGroup
from manim.constants import PI
from manim.typing import Point3DLike

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
    """
    A class to represent a cevian in a triangle.

    Parameters
    ----------
    A : Point3DLike
        The first vertex of the triangle.
    B : Point3DLike
        The second vertex of the triangle. Cevian passes through this point.
    C : Point3DLike
        The third vertex of the triangle.
    alpha : float, optional
        The proportion of the cevian, by default 0.35. Let D be the foot of the cevian, then the proportion is the AD:AC ratio.
    """

    def __init__(self, A: Point3DLike, B: Point3DLike, C: Point3DLike, alpha: float = 0.35, **kwargs):
        D = Line(A, C).point_from_proportion(alpha)

        self.foot = D
        self.general_vertex = B
        self.extra_vertex_1 = A
        self.extra_vertex_2 = C
        self.proportion = alpha

        super().__init__(B, D, **kwargs)

    def get_foot(self) -> Point3DLike:
        return self.foot

    def get_vertex(self) -> Point3DLike:
        return self.general_vertex

    def get_proportion(self) -> float:
        return self.proportion


class Bisector(Cevian):
    """
    A class to represent a bisector in a triangle.

    Parameters
    ----------
    A : Point3DLike
        The first vertex of the triangle.
    B : Point3DLike
        The second vertex of the triangle.
    C : Point3DLike
        The third vertex of the triangle.
    """

    def __init__(self, A: Point3DLike, B: Point3DLike, C: Point3DLike, **kwargs):
        alpha = ((Line(A, C).get_length() * Line(A, B).get_length()) /
                 (Line(B, C).get_length() + Line(A, B).get_length())) / Line(A, C).get_length()
        super().__init__(A, B, C, alpha, **kwargs)

    def get_bisected_angles(self, radius_alpha: float = 1.1, **kwargs) -> VGroup:
        first_angle = Angle.from_three_points(self.extra_vertex_1, self.general_vertex, self.foot, **kwargs)
        kwargs['radius'] = first_angle.radius * radius_alpha
        second_angle = Angle.from_three_points(self.extra_vertex_2, self.general_vertex, self.foot, **kwargs)
        return VGroup(first_angle, second_angle)


class Median(Cevian):
    """
    A class to represent a median in a triangle.

    Parameters
    ----------
    A : Point3DLike
        The first vertex of the triangle.
    B : Point3DLike
        The second vertex of the triangle.
    C : Point3DLike
        The third vertex of the triangle.
    """

    def __init__(self, A: Point3DLike, B: Point3DLike, C: Point3DLike, **kwargs):
        super().__init__(A, B, C, 0.5, **kwargs)

    def get_equal_segments(self, **kwargs) -> VGroup:
        return VGroup(
            Line(self.extra_vertex_1, self.foot).equal(**kwargs),
            Line(self.extra_vertex_2, self.foot).equal(**kwargs),
        )


class Symmedian(Cevian):
    """
    A class to represent a symmedian in a triangle.

    Parameters
    ----------
    A : Point3DLike
        The first vertex of the triangle.
    B : Point3DLike
        The second vertex of the triangle.
    C : Point3DLike
        The third vertex of the triangle
    """

    def __init__(self, A: Point3DLike, B: Point3DLike, C: Point3DLike, **kwargs):
        a, b, c = Line(B, C).get_length(), Line(A, C).get_length(), Line(A, B).get_length()
        alpha = c ** 2 / (a ** 2 + c ** 2)
        super().__init__(A, B, C, alpha=alpha, **kwargs)


class Perpendicular(Line):
    """
    A class to represent a perpendicular line to another line.

    Parameters
    ----------
    line : Line
        The line to which the perpendicular line is drawn.
    dot : Point3DLike
        The point through which the perpendicular line passes.
    length : float, optional
        The length of the perpendicular line, by default 1.0.
    rotate : bool, optionally
        Use if you want the perpendicular to be in the other direction, by default, False.
    """

    def __init__(self, line: Line, dot: Point3DLike, length: float = 1.0, rotate: bool = False, **kwargs):
        X = dot
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
        return self.line

    def get_vertex(self) -> Point3DLike:
        return self.vertex

    def get_foot(self) -> Point3DLike:
        return self.foot

    def get_angles(self, **kwargs) -> VGroup:
        return VGroup(
            Angle.from_three_points(self.vertex, self.foot, self.line.get_start(), elbow=True, **kwargs),
            Angle.from_three_points(self.vertex, self.foot, self.line.get_end(), elbow=True, **kwargs)
        )


class PerpendicularBisector(Line):
    """
    A class to represent a perpendicular bisector to a line.

    Parameters
    ----------
    line : Line
        The line to which the perpendicular bisector is drawn.
    length : float, optional
        The length of the perpendicular bisector, by default 1.0.
    """

    def __init__(self, line: Line, length: float = 1, **kwargs):
        line_1 = Perpendicular(line=line, dot=line.get_center(), length=length / 2, rotate=False)
        line_2 = Perpendicular(line=line, dot=line.get_center(), length=length / 2, rotate=True)

        self.dot = line.get_center()
        self.line = line

        super().__init__(line_1.get_end(), line_2.get_end(), **kwargs)

    def get_angles(self, **kwargs) -> VGroup:
        """
        Get all the angles formed by the perpendicular bisector.

        :param kwargs:
        :return:
        """
        return VGroup(
            Angle.from_three_points(self.line.get_start(), self.dot, self.get_start(), **kwargs),
            Angle.from_three_points(self.line.get_start(), self.dot, self.get_end(), **kwargs),
            Angle.from_three_points(self.line.get_end(), self.dot, self.get_start(), **kwargs),
            Angle.from_three_points(self.line.get_end(), self.dot, self.get_end(), **kwargs),
        )


class Altitude(Perpendicular):
    """
    A class to represent an altitude in a triangle. Important: it is not a cevian.

    Parameters
    ----------
    A : Point3DLike
        The first vertex of the triangle.
    B : Point3DLike
        The second vertex of the triangle.
    C : Point3DLike
        The third vertex of the triangle.
    """

    def __init__(self, A: Point3DLike, B: Point3DLike, C: Point3DLike, **kwargs):
        line = Line(A, C)
        super().__init__(line, B, **kwargs)


class EuclidLine(Line):
    """
    A class to represent an EuclidLine for a triangle.This line is parallel to AC, and pass through B

    Parameters
    ----------
    A : Point3DLike
        The first vertex of the triangle.
    B : Point3DLike
        The second vertex of the triangle.
    C : Point3DLike
        The third vertex of the triangle.
    """

    def __init__(self, A: Point3DLike, B: Point3DLike, C: Point3DLike, **kwargs):
        line = Line(A, C).move_to(B)
        super().__init__(line.get_start(), line.get_end(), **kwargs)
