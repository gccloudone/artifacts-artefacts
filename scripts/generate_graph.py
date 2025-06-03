import os
import pandas as pd
import matplotlib
# Use a non‑interactive backend so it works on the runner
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.dates as mdates
import numpy as np

# ============ Begin plot logic ============

# Use XKCD style for a hand‑drawn effect
plt.xkcd()

# Read the CSV
df = pd.read_csv("data/usage.csv", parse_dates=["date"])

# Drop duplicate dates (keep last if multiple entries on same day)
df = df.drop_duplicates(subset="date", keep="last")

# Convert datetime to just date (this ensures no time component)
df["just_date"] = df["date"].dt.date

# Add a tiny random jitter so the line looks even more hand‑drawn
jitter = np.random.normal(loc=0, scale=0.02, size=len(df))
df["y_jittered"] = df["count"] + jitter

# Get a title from the environment (fallback to a default)
title = os.getenv("CHART_TITLE", "Usage Over Time")

# -------------------------
# Create figure + axis
fig, ax = plt.subplots(figsize=(8, 5))

# -------------------------
# Plot a light, wiggly fill under the curve
ax.fill_between(
    df["just_date"],
    df["count"],
    alpha=0.2,
    color="skyblue"
)

# Plot the jittered line (marker style: diamond, dotted)
ax.plot(
    df["just_date"],
    df["y_jittered"],
    marker="D",
    markersize=6,
    linestyle=":",
    linewidth=1.5,
    color="tomato"
)

# -------------------------
# Annotate each true count above its plotted point
for x, y_true in zip(df["just_date"], df["count"]):
    ax.annotate(
        f"{y_true}",
        (x, y_true + 0.1),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center",
        fontsize=9
    )

# Add a “Peak usage!” note at the maximum point
max_idx = df["count"].idxmax()
x_max, y_max = df.loc[max_idx, "just_date"], df.loc[max_idx, "count"]
ax.text(
    x_max,
    y_max + 0.2,
    "🚀 Peak usage!",
    fontsize=11,
    ha="center"
)

# -------------------------
# Force Y‑axis ticks to be integers only
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# Force X‑axis to show one tick per day (format: MM-DD)
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))

# Rotate X‑axis labels 45° for readability
fig.autofmt_xdate(rotation=45)

# -------------------------
# Remove default spines and draw a hand‑drawn bounding box
for spine in ax.spines.values():
    spine.set_visible(False)

xmin, xmax = df["just_date"].min(), df["just_date"].max()
ymin, ymax = df["count"].min() - 0.1, df["count"].max() + 0.1

ax.plot(
    [xmin, xmin, xmax, xmax, xmin],
    [ymin, ymax, ymax, ymin, ymin],
    color="black",
    linewidth=1
)

# -------------------------
# Add a light, wiggly grid in the background
ax.grid(True, linestyle="--", linewidth=0.5, color="gray", alpha=0.5)

# -------------------------
# Use a playful font if available (fallback if not)
plt.rcParams["font.family"] = "Comic Sans MS"
plt.rcParams["font.size"] = 11

# Set axis labels and tilted title
ax.set_xlabel("Date")
ax.set_ylabel("Repo Count")
ax.set_title(title, rotation=2, fontsize=14)

plt.tight_layout()

# -------------------------
# Save the figure to disk
output_path = "data/usage.png"
plt.savefig(output_path)
print(f"Saved fun graph to {output_path}")
