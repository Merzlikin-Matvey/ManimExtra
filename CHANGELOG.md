# Changelog

All significant changes to the project are recorded in this file

---

## [1.13] — 2025.05.09

## Added
- Added tests (unit and graphical)
- Added CI/CD pipeline for automatic testing

## Changed
- Refactored all CI/CD pipelines

## Fixed
- Fixed documentation

## [1.12] — 2025.04.01

## Added
- Added Sphinx documentation with deployment on GitHub pages
- Added CI/CD pipeline for deployment to GitHub Releases
- Added `utils\docbuild` module for building documentation

## Changed
- Python 3.13 is now supported
- Updated docstrings in the code for Sphinx documentation
- Development dependencies removed from `pyproject.toml`
- `Point3DLike` is now used

## Fixed
- Fixed `from_three_points` method in `Angle` class

## [1.11] — 2024.09.14

## Added
- Added CI/CD pipline for automatic deployment to PyPI
- Added flake8 linter to the project (also in CI/CD)
- Added `change_right_point` method to the `UnitCircle` class for changing the right point of the unit circle 
(for example, from 0 to 2π)
- Added `NinePoint Circle` class, which represents the nine-point circle of a triangle

## Changed
- Adapted the code to the style set by linter

## Fixed
- Small fixes in the `UnitCircle` class
- Fixed `TransformSystem` class`

## [1.10] — 2024.08.13

## Added
- Added `BracketBetweenPoints` class for creating brackets between two points
- Added `UnitCircle` class for creating a unit circle for trigonometry
- Added methods for `UnitCircle` class:
  - `get_center`: returns the center coordinates of the unit circle.
  - `add_point`: adds a new point on the circle at a given angle and attaches a label to it.
  - `show_labels`: displays the default labels (right, up, left, and down) on the circle.
  - `hide_labels`: hides the currently visible labels.
  - `show_horizontal`: adds the horizontal axis (line) to the unit circle.
  - `hide_horizontal`: removes the horizontal axis from the unit circle.
  - `show_vertical`: adds the vertical axis (line) to the unit circle.
  - `hide_vertical`: removes the vertical axis from the unit circle.
  - `show_axes`: displays both horizontal and vertical axes simultaneously.
  - `hide_axes`: hides both horizontal and vertical axes simultaneously.
  - `get_arc`: returns an arc segment on the circle between two specified angles.
- Added `SwapEquations` animation class for swapping equations in a system of equations
- Added `swap` method to `SystemOfEquations` class for swapping equations in a system of equations

## [1.9] — 2024.07.31

## Added

- Added `Bracket` class for creating brackets. Similar to `Brace`
- Added `SystemOfEquations` class for creating systems of equations. You can also create sets of equations
  using the `is_bracket`
- Added `TransformSystem` class for transforming systems of equations
- Added `EuclidLine` class. This line is parallel to the side of the triangle and passes through the opposite vertex
- Added `Circumcircle` class, which represents the circumcircle of a triangle
- Added `CarnotCircle` class
- Now the project is distributed under the MIT license

## Changed

- Simplified project dependencies

## [1.8] — 2024.07.24

## Added

- Added `get_diametrically_opposite_point` method to `Circle` class

## Changed

- Changed `bisected_angles` method in `Bisector` class. Now angles are slightly different because of
  the `radius_alpha=1.1` parameter

## Fixed

- Fixed `set_length_about_point` method in `Line` class. Now it works with `Dot` correctly
- Fixed `Angle` and `Perpendicular` class initialization
- Fixed `intersection_lines` function

## [1.7] — 2024.07.24

## Added

- Added `Incircle` class, which represents the incircle of a triangle

## [1.6] — 2024.07.20

## Added

- Added `Fancy_label` function for easy writing of a title with dynamic animation time
- Added `Piechart` class for creating pie charts

## Changed

- Changed `get_label_center` method in `Angle` class

## [1.5] — 2024.06.08

## Added

- Added `Tangent` class, which represents a tangent to a circle
- Added `.gitignore` file to ignore unnecessary files

## Changed

- Changed `from_three_points` method in `Angle` class. Now the angle is always less than 180 degrees

## Fixed

- Fixed `__init__` method in `Angle` and `Dot`

## [1.4] — 2024.02.06

## Added

- Added new triangle cevians and related classes:
    - `Cevian`
    - `Bisector`
    - `Median`
    - `Symmedian`
    - `Perpendicular`
    - `PerpendicularBisector`
    - `Altitude`

## [1.3] — 2024.02.06

## Added

- Added functions to get intersections of some curves:
    - `intersection_lines`
    - `intersection_circles`
    - `intersection_line_and_circle`

## [1.2] — 2024.02.06

## Added

- Added triangle centers:
    - `Incenter`
    - `Excenter`
    - `Centroid`
    - `Circumcenter`
    - `Orthocenter`
    - `NinePointCenter`
    - `LemoinePoint`
    - `GergonnePoint`
    - `NagelPoint`
    - `Mittenpunkt`
    - `SpiekerCenter`
    - `FeuerbachPoint`
    - `FermatPoint`

## Fixed

- Fixed `from_three_points` method in `Angle`. Now you can transfer regular `Dot`

## [1.1] — 2024.02.01

### Added

- Added the `inversion` method to the `Line` class, that returns the inversion of the line relative to given `Circle`

## [1.0] — 2024-01-28

### Added

- Initial release of the project
- Custom `Line`, `Angle`, and `Circle` classes. You can pass not only NumPy arrays to them, but also regular `Dot`
- Added methods to the `Line` class:
    - `is_point_in_line`: checks if the point lies on a straight line
    - `set_length_about_point`: sets the length of a straight line, with one end remaining at a given point
    - `get_distance`: gets the distance from a point to a straight line
    - `equal`: adds a straight equality icon to the middle
    - `paral`: adds a straight parallelism icon to the middle
- Added the `get_label_center` method to the `Angle` class, which returns a point inside the corner where it is
  convenient to insert a label
- Added methods to the `Circle` class:
    - `pow`: returns the power of a point relative to a circle
    - `is_point_in_circle`: checks if the point lies inside a circle=