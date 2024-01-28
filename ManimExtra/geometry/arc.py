import manim
from manim.constants import *

from ..useful_in_development import *


class Circle(manim.Circle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def from_three_points(p1, p2, p3, auto_dot_to_array=True, **kwargs):
        if auto_dot_to_array:
            p1, p2, p3 = dot_to_array(p1, p2, p3)
        super().from_three_points(p1, p2, p3, **kwargs)

    def pow(self, dot):
        dot = dot_to_array(dot)[0]
        return round((pow(self.get_center()[0] - dot[0], 2) + pow(self.get_center()[1] - dot[1], 2)) -
                     self.radius ** 2, 4)

    def is_point_in_circle(self, dot):
        return self.pow(dot) == 0

        