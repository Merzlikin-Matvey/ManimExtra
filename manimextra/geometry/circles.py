from __future__ import annotations


from manim.typing import Point3DLike

from .default import *
from .intersection import intersection_circles
from ..useful_in_development import *
from .triangle_centers import *


__all__ = [
    "Tangent",
    "Incircle",
    "Circumcircle",
    "NinePointCircle",
    "CarnotCircle"

]


class Tangent(Line):
    """
    A class to represent a tangent to a circle.

    Parameters
    ----------
    circle : Circle
        The circle to which the tangent is drawn.
    dot : Point3DLike
        The point from which the tangent is drawn. It can be on the circle or outside the circle.
    is_other_tangent : bool, optionally
        If True, the tangent is drawn from the other intersection point of the circle and the line, by default, False.
    """
    def __init__(self, circle: Circle, dot: Point3DLike, is_other_tangent=False, **kwargs):
        if circle.pow(dot) < 0:
            raise Exception("Dot is inside the circle")

        self.circle = circle
        self.dot = dot
        self.tangent_point = Dot(intersection_circles(
            circle, Circle(arc_center=dot, radius=np.sqrt(
                pow(distance(circle.get_center(), dot), 2) - pow(circle.get_radius(), 2)
            ))
        )[is_other_tangent])
        self.is_other_tangent = is_other_tangent
        super().__init__(dot, self.tangent_point, **kwargs)

    def get_other_tangent(self):
        return Tangent(self.circle, self.dot, is_other_tangent=(not self.is_other_tangent))


class Incircle(Circle):
    """
    A class to represent the incircle of a triangle.

    Parameters
    ----------
    A : Point3DLike
        The first vertex of the triangle.
    B : Point3DLike
        The second vertex of the triangle.
    C : Point3DLike
        The third vertex of the triangle.
    """
    def __init__(self, A: Point3DLike, B: Point3DLike, C: Point3DLike, *args, **kwargs):
        I = Incenter(A, B, C).get_center()
        a = distance(B, C)
        b = distance(A, C)
        c = distance(A, B)
        p = (a + b + c) / 2
        r = np.sqrt((p - a) * (p - b) * (p - c) / p)
        super().__init__(radius=r, arc_center=I, *args, **kwargs)


class Circumcircle(Circle):
    """
    A class to represent the circumcircle of a triangle.

    Parameters
    ----------
    A : Point3DLike
        The first vertex of the triangle.
    B : Point3DLike
        The second vertex of the triangle.
    C : Point3DLike
        The third vertex of the triangle.
    """
    def __init__(self, A: Point3DLike, B: Point3DLike, C: Point3DLike, *args, **kwargs):
        O = Circumcenter(A, B, C).get_center()
        r = distance(O, A)
        super().__init__(radius=r, arc_center=O, *args, **kwargs)


class NinePointCircle(Circle):
    """
    A class to represent the nine-point circle of a triangle.

    Parameters
    ----------
    A : Point3DLike
        The first vertex of the triangle.
    B : Point3DLike
        The second vertex of the triangle.
    C : Point3DLike
        The third vertex of the triangle.
    """
    def __init__(self, A: Point3DLike, B: Point3DLike, C: Point3DLike, *args, **kwargs):
        r = distance(Circumcenter(A, B, C).get_center(), A) / 2
        print(r)
        O = NinePointCenter(A, B, C).get_center()
        super().__init__(radius=r, arc_center=O, *args, **kwargs)


class CarnotCircle(Circle):
    """
    A class to represent the Carnot circle of a triangle relative to side AC.

    Parameters
    ----------
    A : Point3DLike
        The first vertex of the triangle.
    B : Point3DLike
        The second vertex of the triangle.
    C : Point3DLike
        The third vertex of the triangle.
    """
    def __init__(self, A: Point3DLike, B: Point3DLike, C: Point3DLike, *args, **kwargs):
        circle = Circumcircle(A, B, C)
        circle.rotate(PI, about_point=Line(A, C).get_projection(circle.get_center()))
        super().__init__(radius=circle.get_radius(), arc_center=circle.get_center(), *args, **kwargs)
