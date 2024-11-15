from manim import *
from manimextra import *


class SystemOfEquationsScene(Scene):
    def construct(self):
        first = SystemOfEquations(
            MathTex('3x', '+', '1', '=', '0'),
            MathTex(r'\sin', '{x}', '=', '0.5'),
            is_bracket=True
        )

        second = SystemOfEquations(
            MathTex('3x', '=', '-', '1'),
            MathTex(r'\sin', '{x}', '=', '0.5'),
            is_bracket=True
        )

        self.play(FadeIn(first))
        self.wait(0.4)
        self.play(TransformSystem(first, second))
        self.wait(0.4)


class Trigonometry(Scene):
    def construct(self):
        circle = UnitCircle()
        arc = circle.get_arc(PI / 2, 2 * PI / 3, color=YELLOW)
        dot = circle.add_point(0.6 * PI, r'0.6 \pi')

        self.play(FadeIn(circle), circle.animate.show_axes())
        self.play(FadeIn(arc))


class Triangle(Scene):
    def construct(self):
        A = Dot(3 * LEFT + 2.5 * DOWN).set_z_index(1)
        B = Dot(2 * LEFT + 3 * UP).set_z_index(1)
        C = Dot(3 * RIGHT + 2.5 * DOWN).set_z_index(1)

        a = Line(B, C, color=BLUE)
        b = Line(A, C, color=BLUE)
        c = Line(A, B, color=BLUE)

        biss_a = Bisector(B, A, C, color=YELLOW)
        biss_b = Bisector(A, B, C, color=YELLOW)
        biss_c = Bisector(A, C, B, color=YELLOW)

        I = Incenter(A, B, C)
        incircle = Incircle(A, B, C, color=GREEN)

        self.play(FadeIn(VGroup(A, B, C)))
        self.play(FadeIn(VGroup(a, b, c)))
        self.play(Create(biss_a))
        self.play(Create(biss_b))
        self.play(Create(biss_c))

        self.play(FadeIn(I))
        self.play(Create(incircle))


if __name__ == "__main__":
    config.media_dir = "media/examples"

    SystemOfEquationsScene().render()
    Trigonometry().render()
    Triangle().render()
