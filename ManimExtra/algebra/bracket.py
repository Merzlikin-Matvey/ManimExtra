from typing import Sequence
import svgelements as se

from manim import (
    VMobjectFromSVGPath,
    Mobject
)
from manim.constants import *

from ..useful_in_development import *
from ..geometry.default import Line

__all__ = [
    "Bracket"
]


class Bracket(VMobjectFromSVGPath):
    def __init__(
            self,
            mobject: Mobject,
            direction=DOWN,
            buff=0.2,
            **kwargs
    ):
        path_string = "M0.95 0.33H0.7337V2.31H0.95"
        path = se.Path(path_string)

        self.buff = buff

        super().__init__(path_obj=path, **kwargs)

        angle = -np.arctan2(*direction[:2]) + np.pi
        mobject.rotate(-angle)

        left = mobject.get_corner(DOWN + LEFT)
        right = mobject.get_corner(DOWN + RIGHT)
        self.width = right[0] - left[0]
        self.scale_to_fit_height(self.width)

        self.rotate(PI / 2)
        self.shift(left - self.get_corner(UP + LEFT) + self.buff * DOWN)
        self.rotate(angle, about_point=mobject.get_center())


class BracketBetweenPoints(Bracket):
    def __init__(
        self,
        point_1: Sequence[float] | None,
        point_2: Sequence[float] | None,
        direction: Sequence[float] | None = ORIGIN,
        **kwargs,
    ):
        if all(direction == ORIGIN):
            line_vector = np.array(point_2) - np.array(point_1)
            direction = np.array([line_vector[1], -line_vector[0], 0])
            direction = direction / np.linalg.norm(direction)
        print(point_1, point_2, direction)
        super().__init__(Line(point_1, point_2), direction=direction, **kwargs)