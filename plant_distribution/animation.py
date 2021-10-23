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
scat = ax.scatter(0, 0)

row_idx = 0
coordinates = []
colors = []


def update(frame):
    global row_idx
    for idx, row in df.iloc[row_idx:, :].iterrows():
        _, t, species, x, y, _ = row
        if t > frame:
            row_idx = idx
            break
        if species == 0:
            i = coordinates.index((x, y))
            coordinates.remove((x, y))
            del colors[i]
        elif species == -1:
            coordinates.append((row.x, row.y))
            colors.append('#fb6542')
        elif species == 1:
            coordinates.append((row.x, row.y))
            colors.append('#3f681c')
        else:
            raise RuntimeError("Unknown species")

    scat.set_offsets(coordinates)
    scat.set_edgecolors(colors)
    scat.set_sizes(np.repeat(10, len(coordinates)))

    return scat,


# animation = FuncAnimation(fig, update, interval=10)
animation = FuncAnimation(fig, update, frames=np.linspace(0, T, 500), blit=True)
plt.show()

# %%

print("Save video to disk")
animation.save(DATA_FOLDER / "video.mp4")
print("Video saved")

# video = animation.to_html5_video()
# html = display.HTML(video)
# display.display(html)

plt.close()
