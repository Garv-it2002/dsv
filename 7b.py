import plotly.express as px

df = px.data.gapminder().query("year==2007")

fig = px.scatter_geo(df, locations="iso_alpha", size="pop", hover_name="country", projection="natural earth", title='World Map - Garvit Saraf USN: 1BI21CS185')

fig.show()
