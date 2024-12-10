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
    mo.md(r"""The unit circle is a circle with radius 1 (unit radius) centered at the origin.""")
    return


@app.cell
def __(np, plt):
    _fig, _ax = plt.subplots()

    _ax.add_patch(plt.Circle((0, 0), 1, fill=False))
    _ax.set_aspect('equal')
    _ax.set_xlim([-1.5, 1.5])
    _ax.set_ylim([-1.5, 1.5])
    _ax.add_line(plt.Line2D([-1, 1], [0, 0], color='k'))
    _ax.add_line(plt.Line2D([0, 0], [-1, 1], color='k'))

    _ax.annotate(r'$(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2})$', xy=(np.sqrt(2)/2, np.sqrt(2)/2), xytext=(np.sqrt(2)/2 + 0.1, np.sqrt(2)/2 + 0.1), arrowprops=dict(arrowstyle='->'))
    _ax.add_line(plt.Line2D([-(np.sqrt(2)/2), (np.sqrt(2)/2)], [-(np.sqrt(2)/2), (np.sqrt(2)/2)], color='k', linestyle='dashed'))
    _ax.add_line(plt.Line2D([-(np.sqrt(2)/2), (np.sqrt(2)/2)], [(np.sqrt(2)/2), -(np.sqrt(2)/2)], color='k', linestyle='dashed'))

    _ax
    return


@app.cell
def __(np, plt):
    _fig, _ax = plt.subplots()

    _x = np.linspace(0, 360, 2)
    _y = ((_x / 90) * np.pi) / 2

    _ax.plot(_x, _y)
    _ax.plot(90, np.pi / 2, 'o')
    _ax.plot(180, np.pi, 'o')
    _ax.plot(270, 3 * np.pi / 2, 'o')

    _ax
    return


if __name__ == "__main__":
    app.run()
