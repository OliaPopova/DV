import dash
import numpy
import plotly.graph_objects as go
from P3 import foo_p3
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
                "P3",
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
                                "S5", id='text1',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea1', className="textarea", readOnly=True,
                                         style={}),
                        ]),
                        dbc.CardBody([
                            dcc.Slider(id='S5', value=1000, min=1000, max=2500, step=1, marks=None,
                                       className="S5slider")])
                    ], className='container-fluid'),

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card1'),
                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "S2", id='text2',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea2', className="textarea", readOnly=True,
                                         style={}),

                        ]),
                        dbc.CardBody([
                            dcc.Slider(id='S2', value=8000, min=8000, max=15000, step=1, marks=None,
                                       className="S2slider")])
                    ], className='container-fluid')

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card2'),
                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "S3", id='text3',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea3', className="textarea", readOnly=True,
                                         style={})
                        ]),

                    ], className='container-fluid'),
                    dbc.CardBody([
                        dcc.Slider(id='S3', value=1200, min=1200, max=1900, step=1, marks=None,
                                   className="S3slider")]),

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card3'),

                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "P2", id='text4',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea4', className="textarea", readOnly=True,
                                         style={}),
                        ]),
                        dbc.CardBody([
                            dcc.Slider(id='P2', value=300, min=300, max=500, step=1, marks=None,
                                       className="P2slider")])
                    ], className='container-fluid'),

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card4'),
                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "F2", id='text5',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea5', className="textarea", readOnly=True,
                                         style={}),

                        ]),
                        dbc.CardBody([
                            dcc.Slider(id='F2', value=400, min=400, max=750, step=1, marks=None,
                                       className="F2slider")])
                    ], className='container-fluid')

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card5'),
                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "S1", id='text6',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea6', className="textarea", readOnly=True,
                                         style={})
                        ]),

                    ], className='container-fluid'),
                    dbc.CardBody([
                        dcc.Slider(id='S1', value=20000, min=20000, max=30000, step=1, marks=None,
                                   className="S1slider")]),

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card6'),
                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "Pr1", id='text7',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea7', className="textarea", readOnly=True,
                                         style={})
                        ]),

                    ], className='container-fluid'),
                    dbc.CardBody([
                        dcc.Slider(id='Pr1', value=140, min=140, max=250, step=1, marks=None,
                                   className="Pr1slider")]),

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card7'),

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
    [Input('S5', 'value'),
     Input('S2', 'value'),
     Input('S3', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
# create our callback function
def update_figure(selected_S5, selected_S2, selected_S3,selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (s5,s2,s3,p2,f2,s1,pr1)
    df = foo_p3(selected_S5, selected_S2, selected_S3,selected_P2, selected_F2, selected_S1, selected_Pr1)
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
     Input('S5', 'value'),
     Input('S2', 'value'),
     Input('S3', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
# create our callback function
def update_figure(selected_year, selected_S5, selected_S2, selected_S3, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (year,p2,p3,p4,f2,f4,f5,f6,s1,s2,s3,s5,s6,s8,pr1,ar1,ar2,ar3)
    df = func(selected_year, selected_P2, 0, 0, selected_F2, 0, 0, 0, selected_S1, selected_S2, selected_S3, selected_S5, 0, 0, selected_Pr1, 0, 0, 0)
    fig = px.bar(data_frame=df, x='показатель', y='значение', color='показатель', template='plotly')

    return (fig)


@app.callback(Output('textarea1', 'value'), [Input('S5', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2', 'value'), [Input('S2', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3', 'value'), [Input('S3', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4', 'value'), [Input('P2', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea5', 'value'), [Input('F2', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea6', 'value'), [Input('S1', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea7', 'value'), [Input('Pr1', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


if __name__ == '__main__':
    app.run_server(debug=True)
