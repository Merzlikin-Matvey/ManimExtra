from __future__ import annotations

import numpy as np

from ManimExtra import BLACK, Mobject, Scene, VMobject


def test_import_color():
    import ManimExtra.utils.color as C

    C.WHITE


def test_background_color():
    S = Scene()
    S.camera.background_color = "#ff0000"
    S.renderer.update_frame(S)
    np.testing.assert_array_equal(
        S.renderer.get_frame()[0, 0], np.array([255, 0, 0, 255])
    )

    S.camera.background_color = "#436f80"
    S.renderer.update_frame(S)
    np.testing.assert_array_equal(
        S.renderer.get_frame()[0, 0], np.array([67, 111, 128, 255])
    )

    S.camera.background_color = "#fff"
    S.renderer.update_frame(S)
    np.testing.assert_array_equal(
        S.renderer.get_frame()[0, 0], np.array([255, 255, 255, 255])
    )

    S.camera.background_color = "#bbffbb"
    S.camera.background_opacity = 0.5
    S.renderer.update_frame(S)
    np.testing.assert_array_equal(
        S.renderer.get_frame()[0, 0], np.array([93, 127, 93, 127])
    )


def test_set_color():
    m = Mobject()
    assert m.color.hex == "#fff"
    m.set_color(BLACK)
    assert m.color.hex == "#000"

    m = VMobject()
    assert m.color.hex == "#fff"
    m.set_color(BLACK)
    assert m.color.hex == "#000"
