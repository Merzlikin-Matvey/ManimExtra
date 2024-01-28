import manim
from manim import UP, DOWN, LEFT, RIGHT, UR, UL, DR, DL, PI


from ..useful_in_development import *


class Line(manim.Line):

    def __init__(self, start: manim.Dot = manim.LEFT, end: manim.Dot = manim.RIGHT, auto_dot_to_array=True, **kwargs):
        if auto_dot_to_array:
            start, end = dot_to_array(start, end)
        super().__init__(start, end, **kwargs)

    def is_point_in_line(self, dot):
        dot = dot_to_array(dot)[0]
        x1, y1 = self.get_start()[0], self.get_start()[1]
        x2, y2 = self.get_end()[0], self.get_end()[1]
        x3, y3 = dot[0], dot[1]
        return round(np.linalg.det(np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])), 3) == 0

    def set_length_about_point(self, dot, length):
        A = dot + np.array([length, 0, 0])
        line = Line(dot, A).rotate(about_point=dot, angle=self.get_angle())
        self.put_start_and_end_on(line.get_start(), line.get_end())
        return self

    def get_distance(self, dot):
        dot = dot_to_array(dot)[0]
        return Line(dot, self.get_projection(dot)).get_length()

    def equal(self, n=1, buff=0.1, length=0.2, **kwargs):
        return manim.VGroup(*[Line(**kwargs).set_length(length).rotate(
            about_point=Line(**kwargs).set_length(length).get_center(), angle=np.pi / 2) for i in range(n)]).arrange(
            buff=buff, direction=RIGHT).move_to(self.get_center()).rotate(
            about_point=self.get_center(), angle=self.get_angle()).set_z_index(1)

    def paral(self, n=1, buff=0.08, length=0.15, rotate=False, **kwargs):
        elem = manim.VGroup(
            Line(**kwargs).set_length(length).rotate(about_point=Line().set_length(0.2).get_end(),
                                                     angle=PI / 4).shift(0.02 * UR),
            Line(**kwargs).set_length(length).rotate(about_point=Line().set_length(0.2).get_end(),
                                                     angle=-PI / 4).shift(0.02 * DR)
        ).rotate(int(rotate) * np.pi)
        return manim.VGroup(*[elem.copy() for i in range(n)]).arrange(buff=buff, direction=RIGHT).move_to(
            self.get_center()).rotate(about_point=self.get_center(), angle=self.get_angle()).set_z_index(1)