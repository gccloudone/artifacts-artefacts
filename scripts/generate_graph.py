import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.dates as mdates

# Use XKCD style for a hand-drawn effect
plt.xkcd()

# Read the CSV
df = pd.read_csv("stats/usage.csv", parse_dates=["date"])

# Drop duplicate dates (keep last if multiple entries on same day)
df = df.drop_duplicates(subset="date", keep="last")

# Convert datetime to just date (this ensures no time component)
df["just_date"] = df["date"].dt.date

# Get a title from the environment (fallback to a default)
title = os.getenv("CHART_TITLE", "Public Github Usage Over Time")

# Create figure + axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot using the “just_date” column
ax.plot(df["just_date"], df["count"], marker="o")

# Force Y-axis ticks to be integers only
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# Force X-axis to show one tick per unique date
ax.xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=15))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

# Rotate X-axis labels 45° so they don’t overlap
fig.autofmt_xdate(rotation=45)

# Labels + title
ax.set_xlabel("Date")
ax.set_ylabel("Repo Count")
ax.set_title(title)

plt.tight_layout()

output_path = "stats/usage.png"
plt.savefig(output_path)
print(f"Saved graph to {output_path}")