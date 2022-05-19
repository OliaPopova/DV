from dash import Dash, dcc, html, Input, Output, callback
import dash
import dash_bootstrap_components as dbc



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

server = app.server

app.layout= html.Div([
    dcc.Link('Go to Page 1', href='/P1web.py'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/P2web.py'),
])

page_1_layout = html.Div([
    html.H1('Page 1'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'], 'LA', id='page-1-dropdown'),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/P2web.py'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])

if __name__ == '__main__':
    app.run_server(debug=True)