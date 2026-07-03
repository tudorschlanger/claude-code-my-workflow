"""
Shared matplotlib settings for all scripts plots.
Import and call apply_style() at the top of every plotting script.

Rule: always add horizontal grey lines aligned with y-axis ticks.
"""

import matplotlib as mpl
import matplotlib.ticker as mticker

# ─────────────────────────────────────────────
# Okabe-Ito colorblind-friendly palette
# ─────────────────────────────────────────────

OKABE_ITO = {
    "black":   "#000000",
    "orange":  "#E69F00",
    "sky_blue": "#56B4E9",
    "green":   "#009E73",
    "yellow":  "#F0E442",
    "blue":    "#0072B2",
    "vermillion": "#D55E00",
    "purple":  "#CC79A7",
}


def apply_style() -> None:
    # Font: Palatino (system font on macOS)
    mpl.rcParams["text.usetex"] = False
    mpl.rcParams["font.family"] = "serif"
    mpl.rcParams["font.serif"] = ["Palatino"]

    # Size
    mpl.rcParams["font.size"] = 18
    mpl.rcParams["axes.titlesize"] = 20
    mpl.rcParams["axes.labelsize"] = 18
    mpl.rcParams["legend.fontsize"] = 16

    # Legend: white background
    mpl.rcParams["legend.frameon"] = True
    mpl.rcParams["legend.facecolor"] = "white"
    mpl.rcParams["legend.edgecolor"] = "none"

    # Axes: keep left and bottom spines, remove top and right
    mpl.rcParams["axes.spines.top"] = False
    mpl.rcParams["axes.spines.right"] = False

    # Grid: thin dotted grey lines aligned with y-axis major ticks, drawn behind data
    mpl.rcParams["axes.grid.axis"] = "y"
    mpl.rcParams["axes.grid.which"] = "major"
    mpl.rcParams["grid.color"] = "#d4d4d4"
    mpl.rcParams["grid.linestyle"] = ":"
    mpl.rcParams["grid.linewidth"] = 0.4
    mpl.rcParams["axes.axisbelow"] = True

    # DPI
    mpl.rcParams["figure.dpi"] = 150
    mpl.rcParams["savefig.dpi"] = 300


def align_grid(ax) -> None:
    """Ensure horizontal grid lines align with y-axis ticks on an axes."""
    ax.yaxis.set_major_locator(mticker.MaxNLocator())
    ax.grid(True, axis="y")


def percent_axis(ax, *, top: float = 1.0, step: float = 0.1) -> None:
    """House style for a percentage / share y-axis.

    Always shows the full 0..`top` range on a 0% / 10% / ... / 100% scale: a tick
    every `step` (default 0.1 = 10 percentage points) with 100% always present and
    labelled. Percentage figures are therefore never axis-truncated, so variation
    is not visually exaggerated and shares stay comparable across a figure set.
    Data are assumed to be fractions in [0, 1] (``xmax=1.0``).

    Call this *after* ``align_grid(ax)``: it installs a fixed ``MultipleLocator``
    that overrides align_grid's ``MaxNLocator`` (see memory ``align-grid-yticks``),
    and the grid then aligns to the 10% ticks. Pass ``top > 1.0`` only if a series
    legitimately exceeds 100%.
    """
    ax.yaxis.set_major_locator(mticker.MultipleLocator(step))
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0, decimals=0))
    ax.set_ylim(0, top)
