from __future__ import annotations

import numpy as np

from .default import Line, Circle, Dot, Angle
from .intersection import intersection_circles
from ..useful_in_development import *


__all__ = [
    "Tangent"
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






