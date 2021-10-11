import data as dt
import dash 
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('')
])
app.run_server(debug=False)