import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from plant_distribution import DATA_FOLDER
from plant_distribution.simulation import n, T

from IPython import display

# matplotlib.use('TkAgg')

# %%

df = pd.read_csv(DATA_FOLDER / "sim_history.csv")

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, n - 1)
ax.set_xticks([])
ax.set_ylim(0, n - 1)
ax.set_yticks([])

# Construct the scatter which will be updated during animation
scat = ax.scatter(0, 0)

row_idx = 0


def update(t):
    global row_idx
    coordinates = []
    colors = []
    for idx, row in df.iloc[row_idx:, :].iterrows():
        if row['t'] > t:
            row_idx = idx
            break
        coordinates.append((row.x, row.y))
        col = 'w' if row.species == 0 else 'r'
        colors.append(col)

    if len(coordinates) > 0:
        scat.set_edgecolors(colors)
        arr = np.array(coordinates)
        scat.set_sizes(np.repeat(10, len(arr)))
        scat.set_offsets(arr)

    return scat,


# animation = FuncAnimation(fig, update, interval=10)
animation = FuncAnimation(fig, update, frames=np.linspace(0, T, 100), blit=True)
# plt.show()

animation.save(DATA_FOLDER / "video.mp4")
video = animation.to_html5_video()
html = display.HTML(video)
display.display(html)

# good practice to close the plt object.
plt.close()
