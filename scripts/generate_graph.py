import os
import pandas as pd
import matplotlib
# Use a non‐interactive backend so it survives on a headless runner
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# ============ Begin plot logic ============

# Use XKCD style for a hand‑drawn effect
plt.xkcd()

# Read the CSV
df = pd.read_csv("data/usage.csv", parse_dates=["date"])

# If you have duplicate dates, keep only the last occurrence for each date:
df = df.drop_duplicates(subset="date", keep="last")

# Get a title from the environment (fallback to a default)
title = os.getenv("CHART_TITLE", "Usage Over Time")

# Create figure + axis
fig, ax = plt.subplots()

# Plot the date vs. count
ax.plot(df["date"], df["count"], marker="o")

# Force Y‑axis ticks to be integers only
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# Labels + title
ax.set_xlabel("Date")
ax.set_ylabel("Repo Count")
ax.set_title(title)

# Rotate X‑axis date labels for readability
fig.autofmt_xdate()

plt.tight_layout()

# Output to data/usage.png
output_path = "data/usage.png"
plt.savefig(output_path)
print(f"Saved graph to {output_path}")
