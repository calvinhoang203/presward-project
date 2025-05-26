from preswald import connect, get_df, query, text, table, plotly
import plotly.express as px

# Connect & load by the TOML key
connect()
df = get_df("owid_covid_data")

# Preview the raw data
text("# COVID-19 Data Explorer")
text("## Data Preview")
table(df.head(5))

# Filter for days with >1,000 new cases
sql = """
  SELECT *
    FROM owid_covid_data
   WHERE new_cases > 1000
"""
high_cases = query(sql)

text(f"**Total days with > 1,000 new cases:** {len(high_cases)}")
table(high_cases.head(5))

# Build & display a scatter plot
fig = px.scatter(
    high_cases,
    x="new_cases_per_million",
    y="new_deaths_per_million",
    color="continent",
    hover_name="location",
    title="Cases vs. Deaths per Million",
    labels={
        "new_cases_per_million": "Cases per Million",
        "new_deaths_per_million": "Deaths per Million"
    }
)
fig.update_traces(marker=dict(size=8))
fig.update_layout(template="plotly_white")

text("## Visualization")
plotly(fig)

# Wrap-up summary
text(
  "Use the table above to inspect individual high-case days, and the scatter plot to compare how case rates translate into death rates across different continents."
)