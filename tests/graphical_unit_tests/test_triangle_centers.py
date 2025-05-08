from manim import *
from manim.utils.testing.frames_comparison import frames_comparison
from manimextra import *

__module_test__ = "triangle_centers"


def _triangle_points():
    A = Dot(2 * DOWN + 3.5 * LEFT).set_z_index(1)
    B = Dot(2.5 * UP + 2 * LEFT).set_z_index(1)
    C = Dot(2 * DOWN + 3.5 * RIGHT)

    a = Line(B, C, color=BLUE)
    b = Line(A, C, color=BLUE)
    c = Line(A, B, color=BLUE)

    return A, B, C, a, b, c


@frames_comparison()
def test_excenter(scene):
    A, B, C, a, b, c = _triangle_points()
    excenter = Excenter(A, B, C)
    scene.add(A, B, C, a, b, c, excenter)


@frames_comparison()
def test_centroid(scene):
    A, B, C, a, b, c = _triangle_points()
    centroid = Centroid(A, B, C)
    scene.add(A, B, C, a, b, c, centroid)


@frames_comparison()
def test_circumcenter(scene):
    A, B, C, a, b, c = _triangle_points()
    circumcenter = Circumcenter(A, B, C)
    scene.add(A, B, C, a, b, c, circumcenter)


@frames_comparison()
def test_orthocenter(scene):
    A, B, C, a, b, c = _triangle_points()
    orthocenter = Orthocenter(A, B, C)
    scene.add(A, B, C, a, b, c, orthocenter)


@frames_comparison()
def test_nine_point_center(scene):
    A, B, C, a, b, c = _triangle_points()
    nine_point = NinePointCenter(A, B, C)
    scene.add(A, B, C, a, b, c, nine_point)


@frames_comparison()
def test_lemoine_point(scene):
    A, B, C, a, b, c = _triangle_points()
    lemoine = LemoinePoint(A, B, C)
    scene.add(A, B, C, a, b, c, lemoine)


@frames_comparison()
def test_gergonne_point(scene):
    A, B, C, a, b, c = _triangle_points()
    gergonne = GergonnePoint(A, B, C)
    scene.add(A, B, C, a, b, c, gergonne)


@frames_comparison()
def test_nagel_point(scene):
    A, B, C, a, b, c = _triangle_points()
    nagel = NagelPoint(A, B, C)
    scene.add(A, B, C, a, b, c, nagel)


@frames_comparison()
def test_mittenpunkt(scene):
    A, B, C, a, b, c = _triangle_points()
    mittenpunkt = Mittenpunkt(A, B, C)
    scene.add(A, B, C, a, b, c, mittenpunkt)


@frames_comparison()
def test_spieker_center(scene):
    A, B, C, a, b, c = _triangle_points()
    spieker = SpiekerCenter(A, B, C)
    scene.add(A, B, C, a, b, c, spieker)


@frames_comparison()
def test_feuerbach_point(scene):
    A, B, C, a, b, c = _triangle_points()
    feuerbach = FeuerbachPoint(A, B, C)
    scene.add(A, B, C, a, b, c, feuerbach)


@frames_comparison()
def test_fermat_point(scene):
    A, B, C, a, b, c = _triangle_points()
    fermat = FermatPoint(A, B, C)
    scene.add(A, B, C, a, b, c, fermat)
