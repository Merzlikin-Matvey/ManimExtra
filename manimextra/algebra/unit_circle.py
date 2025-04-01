import math

from manim import (
    MathTex,
    VGroup,
    Arc,
    FadeOut,
    AnimationGroup,
    override_animate,
    FadeIn
)

from manim.utils.color.manim_colors import *

from ..geometry.default import *

__all__ = [
    "UnitCircleLabel",
    "UnitCircle"
]


class UnitCircleLabel(MathTex):
    """
    A label for the unit circle.

    Parameters
    ----------
    direction : np.ndarray
        The direction of the label.
    repeats : int
        The number of repeats of the unit circle.
    fraction : bool
        Whether to use fraction. Default to True.
    """
    def __init__(self, direction=RIGHT, repeats=0, fraction=True, **kwargs):
        if (direction == RIGHT).all():
            self.other = False
            if repeats == 0:
                super().__init__(r'0', **kwargs)
            else:
                super().__init__(str(2 * repeats) + r'\pi', **kwargs)
        elif (direction == LEFT).all():
            if repeats == 0:
                super().__init__(r'\pi', **kwargs)
            elif repeats == -1:
                super().__init__(r'-\pi', **kwargs)
            else:
                super().__init__(str(2 * repeats + 1) + r'\pi', **kwargs)

        if fraction:
            if (direction == UP).all():
                if repeats > 0:
                    up_label_text = r'\dfrac{' + str(4 * repeats + 1) + r'\pi}{2}'
                elif repeats == 0:
                    up_label_text = r'\dfrac{\pi}{2}'
                else:
                    up_label_text = r'-\dfrac{' + str(-(4 * repeats + 1)) + r'\pi}{2}'
                super().__init__(up_label_text, **kwargs)
            if (direction == DOWN).all():
                if repeats >= 0:
                    down_label_text = r'\dfrac{' + str(4 * repeats + 3) + r'\pi}{2}'
                elif repeats == -1:
                    down_label_text = r'-\dfrac{\pi}{2}'
                else:
                    down_label_text = r'-\dfrac{' + str(-(4 * repeats + 3)) + r'\pi}{2}'
                super().__init__(down_label_text, **kwargs)

        else:
            if (direction == UP).all():
                super().__init__(str(2 * repeats + 0.5) + r'\pi', **kwargs)
            elif (direction == DOWN).all():
                super().__init__(str(2 * repeats + 1.5) + r'\pi', **kwargs)


class FadeInAndAdd(AnimationGroup):
    def __init__(self, unit_circle, *objects, **kwargs):
        self.unit_circle = unit_circle
        self.unit_circle.normalize_labels()

        animations = []
        for obj in objects:
            animations.append(FadeIn(obj))

        super().__init__(*animations, **kwargs)


class FadeOutAndRemove(AnimationGroup):
    def __init__(self, unit_circle, *objects, **kwargs):
        self.unit_circle = unit_circle
        self.unit_circle.normalize_labels()

        animations = []
        for obj in objects:
            animations.append(FadeOut(obj))

        super().__init__(*animations, **kwargs)


class UnitCircle(VGroup):
    """
    A unit circle.

    Parameters
    ----------
    point : float
        The point on the unit circle. Using this point we determine how many cycles have passed.
    radius : float, optional
        The radius of the circle. Default to 1.5.
    color : :class:`manim.utils.color.Color`, optional
        The color of the circle. Default to BLUE.
    label_buff : float, optional
        The buffer between the circle and the labels. Default to 0.2.
    font_size : int, optional
        The font size of the labels. Default to 32.
    fractions : bool, optional
        Whether to use fraction in the labels. Default to True.

    Examples
    --------
    .. manimextra:: UnitCircleExample
        :save_last_frame:

        class UnitCircleExample(Scene):
            def construct(self):
                circle = UnitCircle()
                circle.add_point(PI / 2, "\dfrac{\pi}{2}")
                circle.add_point(PI, "\pi")
                self.add(circle)
    """
    def __init__(self, point=0, radius=1.5, color=BLUE, label_buff=0.2, font_size=32, fractions=True):
        self.circle = Circle(radius=radius, color=color)
        self.circle.set_z_index(-5)

        self.labels = VGroup()
        self.dots = VGroup()

        self.other_right_basic_label = False

        repeats = math.floor(point / (2 * np.pi))
        self.repeats = repeats

        self.label_buff = label_buff
        self.font_size = font_size

        right = Dot(self.circle.point_at_angle(0))
        up = Dot(self.circle.point_at_angle(np.pi / 2))
        left = Dot(self.circle.point_at_angle(np.pi))
        down = Dot(self.circle.point_at_angle(3 * np.pi / 2))

        self.right = right
        self.up = up
        self.left = left
        self.down = down

        self.right_label = UnitCircleLabel(direction=RIGHT, repeats=repeats, fraction=fractions,
                                           font_size=font_size).next_to(right, RIGHT, buff=label_buff)
        self.up_label = UnitCircleLabel(direction=UP, repeats=repeats, fraction=fractions, font_size=font_size).next_to(
            up, UP, buff=label_buff)
        self.left_label = UnitCircleLabel(direction=LEFT, repeats=repeats, fraction=fractions,
                                          font_size=font_size).next_to(left, LEFT, buff=label_buff)
        self.down_label = UnitCircleLabel(direction=DOWN, repeats=repeats, fraction=fractions,
                                          font_size=font_size).next_to(down, DOWN, buff=label_buff)

        self.horizontal = Line(self.left, self.right)
        self.vertical = Line(self.down, self.up)

        super().__init__(self.circle, self.labels, self.dots)

    def change_right_point(self):
        if self.other_right_basic_label:
            self.right_label = UnitCircleLabel(direction=RIGHT, repeats=self.repeats, font_size=self.font_size).next_to(
                self.right, RIGHT, buff=self.label_buff)
        else:
            self.right_label = UnitCircleLabel(direction=RIGHT, repeats=self.repeats + 1,
                                               font_size=self.font_size).next_to(
                self.right, RIGHT, buff=self.label_buff)

        self.other_right_basic_label = not self.other_right_basic_label
        return self

    def get_center(self):
        """
        Get the center of the circle.
        Override because the center of VGroup is different from the center of the circle.
        """
        return self.circle.get_center()

    def add_point(self, point, label):
        """
        Add a point to the unit circle.

        Parameters
        ----------
        point
        label

        Returns
        -------

        """
        dot = Dot(self.circle.point_at_angle(point))
        if isinstance(label, str):
            print(Line(self.get_center(), dot.get_center()).get_unit_vector())
            label = MathTex(label,
                            font_size=self.font_size
                            ).next_to(dot,
                                      np.round(Line(self.get_center(), dot.get_center()).get_unit_vector(), 1),
                                      buff=self.label_buff
                                      )
        self.dots.add(dot)
        self.labels.add(label)
        return VGroup(dot, label)

    @override_animate(add_point)
    def _add_point_animation(self, point, label, anim_args=None):
        if anim_args is None:
            anim_args = {}
        dot, label = self.add_point(point, label)
        anim = FadeIn(VGroup(dot, label), **anim_args)
        return anim

    def normalize_labels(self):
        VGroup(self.right, self.up, self.left, self.down, self.right_label, self.up_label, self.left_label,
               self.down_label).move_to(self.circle.get_center())

    def show_labels(self):
        self.normalize_labels()
        self.add(self.right, self.up, self.left, self.down, self.right_label, self.up_label, self.left_label,
                 self.down_label)
        return self

    def hide_labels(self):
        self.remove(self.right, self.up, self.left, self.down, self.right_label, self.up_label, self.left_label,
                    self.down_label)
        return self

    @override_animate(show_labels)
    def _show_labels_animation(self, anim_args=None):
        self.normalize_labels()
        if anim_args is None:
            anim_args = {}
        return FadeInAndAdd(self, self.right, self.up, self.left, self.down,
                            self.right_label, self.up_label, self.left_label, self.down_label, **anim_args)

    @override_animate(hide_labels)
    def _hide_labels_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return FadeOutAndRemove(self, self.right, self.up, self.left, self.down,
                                self.right_label, self.up_label, self.left_label, self.down_label, **anim_args)

    def show_horizontal(self):
        self.add(self.horizontal)
        return self

    def hide_horizontal(self):
        self.remove(self.horizontal)
        return self

    @override_animate(show_horizontal)
    def _show_horizontal_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return FadeInAndAdd(self, self.horizontal, **anim_args)

    @override_animate(hide_horizontal)
    def _hide_horizontal_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return FadeOutAndRemove(self, self.horizontal, **anim_args)

    def show_vertical(self):
        self.add(self.vertical)
        return self

    def hide_vertical(self):
        self.remove(self.vertical)
        return self

    @override_animate(show_vertical)
    def _show_vertical_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return FadeInAndAdd(self, self.vertical, **anim_args)

    @override_animate(hide_vertical)
    def _hide_vertical_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return FadeOutAndRemove(self, self.vertical, **anim_args)

    def show_axes(self):
        self.add(self.horizontal, self.vertical)
        return self

    def hide_axes(self):
        self.remove(self.horizontal, self.vertical)
        return self

    @override_animate(show_axes)
    def _show_axes_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return FadeInAndAdd(self, self.horizontal, self.vertical, **anim_args)

    @override_animate(hide_axes)
    def _hide_axes_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return FadeOutAndRemove(self, self.horizontal, self.vertical, **anim_args)

    def get_abscissa_point(self, point):
        alpha = (1 + point) / 2
        return self.horizontal.point_from_proportion(alpha)

    def get_ordinate_point(self, point):
        alpha = (1 + point) / 2
        return self.vertical.point_from_proportion(alpha)

    def get_arc(self, start, end, **kwargs):
        if start > end:
            start, end = end, start

        angle = end - start
        return Arc(arc_center=self.circle.get_center(), radius=self.circle.get_radius(),
                   start_angle=start, angle=angle,
                   **kwargs)

    def point_at_angle(self, angle):
        return self.circle.point_at_angle(angle)
