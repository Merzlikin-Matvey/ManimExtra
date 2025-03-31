import svgelements as se

from manim import (
    VMobjectFromSVGPath,
    Mobject
)
from manim.constants import *
from manim.typing import Point3DLike

from ..useful_in_development import *
from ..geometry.default import Line

__all__ = [
    "Bracket",
    "BracketBetweenPoints"
]


class Bracket(VMobjectFromSVGPath):
    """Analogue of manim's Brace, but for a rectangle.

    Examples
    --------
    .. manimextra:: BracketExample
        :save_last_frame:

        class BracketExample(Scene):
            def construct(self):
                sq = Square(color=BLUE, fill_opacity=0.5)
                bracket = Bracket(sq, buff=0.1)
                self.add(sq, bracket)
    """
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
    """Class that creates a bracket between two points.

    Parameters
    ----------
    point_1 : Point3DLike, optional
        The first point, by default ORIGIN
    point_2 : Point3DLike, optional
        The second point, by default ORIGIN
    direction : Point3DLike, optional
        The direction of the bracket, by default ORIGIN

    Examples
    --------
    .. manimextra:: BracketBetweenPointsExample
        :save_last_frame:

        class BracketBetweenPointsExample(Scene):
            def construct(self):
                A = Dot(LEFT + DOWN)
                B = Dot(RIGHT + UP)
                bracket = BracketBetweenPoints(A, B, buff=0.1)
                self.add(A, B, bracket)

    """
    def __init__(
        self,
        point_1: Point3DLike = LEFT,
        point_2: Point3DLike = RIGHT,
        direction: Point3DLike | None = ORIGIN,
        **kwargs,
    ):
        point_1, point_2 = dot_to_array(point_1, point_2)
        if all(direction == ORIGIN):
            line_vector = point_2 - point_1
            direction = np.array([line_vector[1], -line_vector[0], 0])
            direction = direction / np.linalg.norm(direction)
        super().__init__(Line(point_1, point_2), direction=direction, **kwargs)
