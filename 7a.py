import plotly.express as px
import numpy as np
import datetime

# Generate dates and values
dates = [datetime.datetime.now() + datetime.timedelta(days=i) for i in range(100)]
values = np.random.randn(100).cumsum()

px.line(x=dates, y=values).show()