import dash
import numpy
import plotly.graph_objects as go
from P5 import foo_p5
from allgraph import func
from dash import dcc, no_update
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

# git commit -m "Demo"
# git push heroku main
# heroku ps:scale web=1


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

server = app.server

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.P(
                "P5",
                style={'font-size': '26px', 'font-weight': 'normal',
                       'font-family': 'Open Sans', 'color': 'white'}, id='dashname'),
            width={"size": 10, "offset": 2})
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "S6", id='text1',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea1', className="textarea", readOnly=True,
                                         style={}),
                        ]),
                        dbc.CardBody([
                            dcc.Slider(id='S6', value=3000, min=3000, max=6000, step=1, marks=None,
                                       className="S6slider")])
                    ], className='container-fluid'),

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card5'),
            ], align="center"),

        ], width={'size': 12}),
    ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Graph(id='fig1', config={
                    'staticPlot': False,  # True, False
                    'displayModeBar': False,  # True, False, 'hover'
                    'watermark': True,
                }, )
            ], className='fig1')
        )

    ], style={'background-color': '#323436'}),
    dcc.Dropdown(
        ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023', id='dropdown'
    ),

    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Graph(id='fig2', config={
                    'staticPlot': False,  # True, False
                    'displayModeBar': False,  # True, False, 'hover'
                    'watermark': True,
                }, )
            ], className='fig2')
        )

    ], style={'background-color': '#323436'}),

], style={'height': '100vh', 'background-color': '#323436'}, fluid=True)


@app.callback(
    Output('fig1', 'figure'),
    [Input('S6', 'value')])
# create our callback function
def update_figure(selected_S6):
    df = foo_p5(selected_S6)

    fig = px.bar(data_frame=df, x='года', y='значения',
                 color='года',
                 color_discrete_map={
                     '2020': '#2dbfcf',
                     '2021': '#1fad94',
                     '2022': '#148e95',
                     '2023': '#0068b4',
                     '2024': '#309ec1',
                     '2025': '#b0d9ff'}, template='plotly')

    return (fig)


@app.callback(
    Output('fig2', 'figure'),
    [Input('dropdown', 'value'),
     Input('S6', 'value'),
     ])
# create our callback function
def update_figure(selected_year,selected_S6):
    # (p2,f2,s1,pr1,p3,s5,s2,s3,f4,ar1,ar2,ar3,p4,f5,f6,s8,s6)
    df = func(selected_year, 0, 0, 0, 0, 0, 0, 0,0 , 0, 0, 0, 0, 0, 0, 0, 0,selected_S6)
    fig = px.bar(data_frame=df, x='показатель', y='значение', color='показатель', template='plotly')

    return (fig)



@app.callback(Output('textarea1', 'value'), [Input('S6', 'value')])
def textarea5input(normv):
    if normv:
        textareav = str(normv)
        return textareav

if __name__ == '__main__':
    app.run_server(debug=True)
