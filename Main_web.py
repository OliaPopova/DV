from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
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