from __future__ import annotations

from manim.constants import *

from .default import Line, Circle, Dot, Angle
from .intersection import intersection_circles
from ..useful_in_development import *
from .triangle_centers import *


__all__ = [
    "Tangent",
    "Incircle",
    "Circumcircle",
    "CarnotCircle"

]

class Tangent(Line):
    def __init__(self, circle: Circle, dot: Dot, is_other_tangent=False, **kwargs):
        dot = dot_to_array(dot)[0]
        if (circle.pow(dot) < 0):
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
    def __init__(self, A, B, C, *args, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        I = Incenter(A, B, C).get_center()
        a = distance(B, C)
        b = distance(A, C)
        c = distance(A, B)
        p = (a + b + c) / 2
        r = np.sqrt((p - a) * (p - b) * (p - c) / p)
        super().__init__(radius=r, arc_center=I, *args, **kwargs)


class Circumcircle(Circle):
    def __init__(self, A, B, C, *args, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        O = Circumcenter(A, B, C).get_center()
        r = distance(O, A)
        super().__init__(radius=r, arc_center=O, *args, **kwargs)


class CarnotCircle(Circle):
    def __init__(self, A, B, C, *args, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        circle = Circumcircle(A, B, C)
        circle.rotate(PI, about_point=Line(A, C).get_projection(circle.get_center()))
        super().__init__(radius=circle.get_radius(), arc_center=circle.get_center(), *args, **kwargs)




