import marimo

__generated_with = "0.9.33"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    return mo, np, plt


@app.cell
def __(mo):
    mo.md(
        r"""
        Write a function to find the UV offset for a frame if an animation has 16 frames and is laid out in a grid with 8 rows and 2 columns, and current frame's position is indexed by decimal relative to the total size of the image, like animated textures via Figura's setUV method.

        There are 8 frames in each column. It should repeat infinitely hence the mod 2: $y=\frac{x}{8}\mod2$
        """
    )
    return


@app.cell
def __(np, plt):
    _x = np.linspace(0, 32, 1000)
    # _x = np.arange(0, 32, 0.01)
    _y = (_x / 8) % 2

    _fig, _ax = plt.subplots()
    _ax.plot(_x, _y)

    _ax
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        The x position should be 0 for 8 frames, then 0.5 for 8 frames, and this pattern should continue to repeat.

        If $\frac{x}{8}\mod2\geq1$, then $x=\frac{1}{2}$. If $\frac{x}{8}\mod2<1$, then $x=0$.
        """
    )
    return


@app.cell
def __(np, plt):
    _x = np.linspace(0, 32, 1000)
    # _x = np.arange(0, 32, 0.01)
    _y = np.where(_x / 8 % 2 >= 1, 0.5, 0)

    _fig, _ax = plt.subplots()
    _ax.plot(_x, _y)
    _ax.set_ylim(0, 1)

    _ax
    return


if __name__ == "__main__":
    app.run()
