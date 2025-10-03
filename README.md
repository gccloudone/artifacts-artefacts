# 📊 Public Usage Stats Branch

This branch is **dedicated solely** to tracking and visualizing usage of the `JF_URL` reference across GitHub repositories.
It is not intended for development or deployment code — it exists as a **data + reporting branch** maintained automatically by a GitHub Action.

---

## 🔄 How It Works

* A scheduled GitHub Action runs every day at **03:00 UTC** (and can also be triggered manually).
* The Action:

  1. Searches public GitHub repositories for workflow files referencing
     `artifacts-artefacts.devops.cloud-nuage.canada.ca`
  2. Counts the number of **unique repositories**.
  3. Appends the count to [`stats/usage.csv`](./stats/usage.csv).
  4. Generates an XKCD-style time series graph via [`scripts/generate_graph.py`](./scripts/generate_graph.py).
  5. Commits the updated CSV and graph back to this branch.

---

## 📂 Branch Structure

```none
├── scripts/
│   └── generate_graph.py   # Python script to generate the usage graph
└── stats/
    ├── usage.csv           # Historical counts (date,count)
    └── usage.png           # Auto-generated graph of usage over time
```

---

## 📈 Current Graph

![Usage graph](./stats/usage.png)

---

## ⚙️ Notes

* This branch is maintained by automation; **do not edit files manually** (changes may be overwritten).
* For source code and project files, see the [`main`](https://github.com/gccloudone/artifacts-artefacts/tree/main) branch.
* Graphs use [matplotlib’s XKCD mode](https://matplotlib.org/stable/api/pyplot_api.html#matplotlib.pyplot.xkcd) for a hand-drawn style.
