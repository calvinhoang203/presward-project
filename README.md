# COVID-19 Data Explorer

This is a simple dashboard that lets you explore COVID-19 data from Our World in Data.

## What You’ll Find

* **Quick setup**: Load and clean a CSV with just a few lines of code.
* **Rolling averages**: See 7-day average trends for cases and deaths.
* **High-case days**: Filter out days when new cases spiked above 1,000.
* **Interactive tables & charts**: Sort, search, and hover to get more details.

## Why It Matters

Building dashboards usually takes a lot of setup, but with Preswald you can go from raw data to an interactive UI in minutes. This project shows how:

1. **Load your data** via a simple configuration in `preswald.toml`.
2. **Clean it** by parsing dates and filling gaps.
3. **Crunch numbers** with SQL-like filters and rolling averages.
4. **Visualize** with Plotly charts and built-in tables.

## Challenges

* **Data quirks**: Missing values and date formats needed a quick fix before charts made sense.
* **Preview layout**: Juggling tables and plots took a couple of tweaks to keep everything visible.
* **Config keys**: The name you give your dataset in `preswald.toml` has to match exactly in your code.
## Next Steps

* Add controls (like date pickers or sliders).
* Compare data from different countries.

