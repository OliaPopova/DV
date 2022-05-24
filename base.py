import dash
from P1 import foo_p1, foo_p1_v
from P1_c import foo_p1_c, foo_p1_cv
from P2 import foo_p2, foo_p2_v
from P2_c import foo_p2_c, foo_p2_cv
from P3 import foo_p3, foo_p3_v
from P3_c import foo_p3_c, foo_p3_cv
from P4 import foo_p4, foo_p4_v
from P4_c import foo_p4_c, foo_p4_cv
from P5 import foo_p5
from P5_c import foo_p5_c, foo_p5_cv
from P6 import foo_p6, foo_p6_v
from P6_c import foo_p6_c, foo_p6_cv
from P7_c import foo_p7_c, foo_p7_cv
from P8_c import foo_p8_c, foo_p8_cv
from dash import dcc, no_update
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

# git commit -m "Demo"
# git push heroku main
# heroku ps:scale web=1
# heroku logs --tail

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

server = app.server

app.layout = dbc.Container([
    dbc.Row([
        html.Div([
            dcc.Dropdown(
                ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P1_c', 'P2_c', 'P3_c', 'P4_c', 'P5_c', 'P6_c', 'P7_c', 'P8_c'],
                'P1', searchable=False,
                clearable=False,
                id='dropdownpriorty',
                style={"width": "70px", "height": "40px"}),
        ], style={"width": "50%"}),
    ], style={'background-color': '#323436'}),
    html.Div(id="P1container",
             children=[
                 dbc.Row([
                     dbc.Col(
                         html.P(
                             "P1",
                             style={'font-size': '26px', 'font-weight': 'normal',
                                    'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                         width={"size": 10, "offset": 2})
                 ]),
                 dbc.Row([
                     dbc.Col([
                         dbc.Row([
                             dbc.Card([
                                 dbc.Container([
                                     dbc.Row([
                                         html.P(
                                             "НАУЧ РАБ", id='text1P1',
                                             className="card-text",
                                             style={'font-size': '16px',
                                                    'font-family': 'Open Sans'}),
                                         dcc.Textarea(id='textarea1P1', className="textarea", readOnly=True,
                                                      style={}),
                                     ]),
                                     dbc.CardBody([
                                         dcc.Slider(id='P2P1', value=300, min=300, max=500, step=1, marks=None,
                                                    className="slider")])
                                 ], className='container-fluid'),

                             ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                       "height": "80%"},
                                 id='card1P1', className='card1webP1'),
                             dbc.Card([
                                 dbc.Container([
                                     dbc.Row([
                                         html.P(
                                             "ЗП_ППС_РЕАЛ", id='text2P1',
                                             className="card-text",
                                             style={'font-size': '16px',
                                                    'font-family': 'Open Sans'}),
                                         dcc.Textarea(id='textarea2P1', className="textarea", readOnly=True,
                                                      style={}),

                                     ]),
                                     dbc.CardBody([
                                         dcc.Slider(id='F2P1', value=400, min=400, max=750, step=1, marks=None,
                                                    className="slider")])
                                 ], className='container-fluid')

                             ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                       "height": "80%"},
                                 id='card2P1', className='card2webP1'),

                         ], align="center"),

                     ], width={'size': 12}),
                 ], style={'background-color': '#323436', 'margin-bottom': '0%'}),

                 dbc.Row([
                     dbc.Col([
                         dbc.Row([
                             dbc.Card([
                                 dbc.Container([
                                     dbc.Row([
                                         html.P(
                                             "Кол-во обучающихся", id='text3P1',
                                             className="card-text",
                                             style={'font-size': '16px',
                                                    'font-family': 'Open Sans'}),
                                         dcc.Textarea(id='textarea3P1', className="textarea", readOnly=True,
                                                      style={})
                                     ]),

                                 ], className='container-fluid'),
                                 dbc.CardBody([
                                     dcc.Slider(id='S1P1', value=20000, min=20000, max=30000, step=1,
                                                marks=None,
                                                className="slider")]),

                             ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                       "height": "80%"},
                                 id='card3P1', className='card3webP1'),
                             dbc.Card([
                                 dbc.Container([
                                     dbc.Row([
                                         html.P(
                                             "Кол-во программ", id='text4P1',
                                             className="card-text",
                                             style={'font-size': '16px',
                                                    'font-family': 'Open Sans'}),
                                         dcc.Textarea(id='textarea4P1', className="textarea", readOnly=True,
                                                      style={})
                                     ]),

                                 ], className='container-fluid'),
                                 dbc.CardBody([
                                     dcc.Slider(id='Pr1P1', value=140, min=140, max=250, step=1, marks=None,
                                                className="slider")]),

                             ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                       "height": "80%"},
                                 id='card4P1', className='card4webP1'),

                         ], align="center"),

                     ], width={'size': 12}),
                 ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                 dbc.Row([
                     dbc.Col(
                         html.Div([
                             dcc.Graph(id='fig1P1', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], className='figosn')
                     )

                 ], style={'background-color': '#323436'}),
                 dbc.Row([
                     html.Div([
                         dcc.Dropdown(
                             ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                             searchable=False, clearable=False,
                             id='dropdownP1',
                             style={"width": "70px", "height": "40px"}, className='dropdown'),
                     ], style={"width": "50%"}),
                 ], style={'background-color': '#323436'}, className='dropdownrow'),

                 dbc.Row([
                     html.Div([
                         dcc.Graph(id='fig2P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),

                     html.Div([
                         dcc.Graph(id='fig3P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),

                     html.Div([
                         dcc.Graph(id='fig4P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),
                     html.Div([
                         dcc.Graph(id='fig5P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),

                     html.Div([
                         dcc.Graph(id='fig6P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),

                 ], style={'background-color': '#323436'}),

                 dbc.Row([
                     html.Div([
                         dcc.Graph(id='fig7P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),

                     html.Div([
                         dcc.Graph(id='fig8P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),

                     html.Div([
                         dcc.Graph(id='fig9P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),
                     html.Div([
                         dcc.Graph(id='fig10P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),

                     html.Div([
                         dcc.Graph(id='fig11P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),

                 ], style={'background-color': '#323436'}),

                 dbc.Row([
                     html.Div([
                         dcc.Graph(id='fig12P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),

                     html.Div([
                         dcc.Graph(id='fig13P1', config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True,
                         }, )
                     ], style={"width": "20%", "height": "10%"}, className='fig'),

                 ], style={'background-color': '#323436'}),
             ]),
    html.Div(id="P1_ccontainer",
             children=[
                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P1_c",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "НАУЧ РАБ", id='text1P1_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P1_c', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P2P1_c', value=300, min=300, max=500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card1P1_c', className='card1webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ЗП_ППС_РЕАЛ", id='text2P1_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P1_c', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='F2P1_c', value=400, min=400, max=750, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2P1_c', className='card2webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во обучающихся", id='text3P1_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea3P1_c', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='S1P1_c', value=20000, min=20000, max=30000, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card3P1_c', className='card3webP1_c'),
                                 dbc.Row([
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "Кол-во программ", id='text4P1_c',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea4P1_c', className="textarea", readOnly=True,
                                                              style={})
                                             ]),

                                         ], className='container-fluid'),
                                         dbc.CardBody([
                                             dcc.Slider(id='Pr1P1_c', value=140, min=140, max=250, step=1, marks=None,
                                                        className="slider")]),

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card4P1_c', className='card4webP1_c'),
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "Web_of_Science", id='text5P1_c',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea5P1_c', className="textarea", readOnly=True,
                                                              style={}),

                                             ]),
                                             dbc.CardBody([
                                                 dcc.Slider(id='Ar1P1_c', value=1, min=1, max=500, step=1, marks=None,
                                                            className="slider")])
                                         ], className='container-fluid')

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card5P1_c', className='card5webP1_c'),
                                 ]),
                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P1_c', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP1_c',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], id='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig4P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig5P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig6P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig7P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig9P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig10P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig11P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig12P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig13P1_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),
             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P2container",
             children=[

                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P2",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ППС39", id='text1P2',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P2', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P3P2', value=500, min=500, max=750, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     # тоже 4 карточки как на P1
                                     id='card1P2', className='card1webP1'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ЗП_ППС_РЕАЛ", id='text2P2',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P2', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='F2P2', value=400, min=400, max=750, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2P2', className='card2webP1'),
                             ], align="center"),
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во обучающихся", id='text3P2',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea3P2', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='S1P2', value=20000, min=20000, max=30000, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card3P2', className='card3webP1'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во программ", id='text4P2',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea4P2', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='Pr1P2', value=140, min=140, max=250, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card4P2', className='card4webP1'),
                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P2', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP2',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], className='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P2', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P2', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig4P2', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig5P2', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig6P2', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig7P2', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P2', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig10P2', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig11P2', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig12P2', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([

                         html.Div([
                             dcc.Graph(id='fig13P2', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),
             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P2_ccontainer",
             children=[
                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P2_c",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "НАУЧ РАБ", id='text1P2_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P2_c', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P2P2_c', value=300, min=300, max=500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     # тоже 5 карточек как на P1_c
                                     id='card1P2_c', className='card1webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ЗП_ППС_РЕАЛ", id='text2P2_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P2_c', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='F2P2_c', value=400, min=400, max=750, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2P2_c', className='card2webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во обучающихся", id='text3P2_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea3P2_c', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='S1P2_c', value=20000, min=20000, max=30000, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card3P2_c', className='card3webP1_c'),
                                 dbc.Row([
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "Кол-во программ", id='text4P2_c',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea4P2_c', className="textarea", readOnly=True,
                                                              style={})
                                             ]),

                                         ], className='container-fluid'),
                                         dbc.CardBody([
                                             dcc.Slider(id='Pr1P2_c', value=140, min=140, max=250, step=1, marks=None,
                                                        className="slider")]),

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card4P2_c', className='card4webP1_c'),
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "SCOPUS", id='text5P2_c',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea5P2_c', className="textarea", readOnly=True,
                                                              style={}),

                                             ]),
                                             dbc.CardBody([
                                                 dcc.Slider(id='Ar2P2_c', value=1, min=1, max=700, step=1, marks=None,
                                                            className="slider")])
                                         ], className='container-fluid')

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card5P2_c', className='card5webP1_c'),
                                 ]),
                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P2_c', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP2_c',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], className='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig4P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig5P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig6P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig7P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig9P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig10P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig11P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig12P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig13P2_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),
             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P3container",
             children=[

                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P3",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "СТУДКВАЛ", id='text1P3',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P3', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='S5P3', value=1000, min=1000, max=2500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card1webP3'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "СТУДБАК", id='text2P3',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P3', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='S2P3', value=8000, min=8000, max=15000, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2webP3'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во обучающихся", id='text3P3',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea3P3', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='S1P3', value=20000, min=20000, max=30000, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card3webP3'),

                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "НАУЧ РАБ", id='text4P3',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea4P3', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P2P3', value=300, min=300, max=500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card4webP3'),

                                 dbc.Row([
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "ЗП_ППС_РЕАЛ", id='text5P3',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea5P3', className="textarea", readOnly=True,
                                                              style={}),

                                             ]),
                                             dbc.CardBody([
                                                 dcc.Slider(id='F2P3', value=400, min=400, max=750, step=1, marks=None,
                                                            className="slider")])
                                         ], className='container-fluid')

                                     ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card5webP3'),
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "СТУДСПЕЦ", id='text6P3',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea6P3', className="textarea", readOnly=True,
                                                              style={})
                                             ]),

                                         ], className='container-fluid'),
                                         dbc.CardBody([
                                             dcc.Slider(id='S3P3', value=1200, min=1200, max=1900, step=1, marks=None,
                                                        className="slider")]),

                                     ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card6webP3'),

                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "Кол-во программ", id='text7P3',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea7P3', className="textarea", readOnly=True,
                                                              style={})
                                             ]),

                                         ], className='container-fluid'),
                                         dbc.CardBody([
                                             dcc.Slider(id='Pr1P3', value=140, min=140, max=250, step=1, marks=None,
                                                        className="slider")]),

                                     ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card7webP3'),
                                 ]),
                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P3', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP3',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], className='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig4P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig5P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig6P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig7P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig9P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig10P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig11P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig12P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig13P3', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P3_ccontainer",
             children=[
                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P3_c",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "НАУЧ РАБ", id='text1P3_с',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P3_с', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P2P3_с', value=300, min=300, max=500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card1P3_с', className='card1webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ЗП_ППС_РЕАЛ", id='text2P3_с',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P3_с', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='F2P3_с', value=400, min=400, max=750, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2P3_с', className='card2webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во обучающихся", id='text3P3_с',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea3P3_с', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='S1P3_с', value=20000, min=20000, max=30000, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card3P3_с', className='card3webP1_c'),

                                 dbc.Row([
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "Кол-во программ", id='text4P3_с',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea4P3_с', className="textarea", readOnly=True,
                                                              style={})
                                             ]),

                                         ], className='container-fluid'),
                                         dbc.CardBody([
                                             dcc.Slider(id='Pr1P3_с', value=140, min=140, max=250, step=1, marks=None,
                                                        className="slider")]),

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card4P3_с', className='card4webP1_c'),
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "ARTICLE_HIGH", id='text5P3_с',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea5P3_с', className="textarea", readOnly=True,
                                                              style={}),

                                             ]),
                                             dbc.CardBody([
                                                 dcc.Slider(id='Ar3P3_с', value=1, min=1, max=100, step=1, marks=None,
                                                            className="slider")])
                                         ], className='container-fluid')

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card5P3_c', className='card5webP1_c'),
                                 ]),
                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P3_с', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP3_с',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], className='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig4P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig5P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig6P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig7P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig9P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig10P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig11P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig12P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig13P3_с', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),
             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P4container",
             children=[
                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P4",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "НАУЧ РАБ", id='text1P4',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P4', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P2P4', value=300, min=300, max=500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card1P4', className='card1webP1'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ЗП_ППС_РЕАЛ", id='text2P4',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P4', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='F2P4', value=400, min=400, max=750, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2P4', className='card2webP1'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во обучающихся", id='text3P4',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea3P4', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='S1P4', value=20000, min=20000, max=30000, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card3P4', className='card3webP1'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во программ", id='text4P4',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea4P4', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='Pr1P4', value=140, min=140, max=250, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card4P4', className='card4webP1'),

                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P4', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP4',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], className='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig4P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig5P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig6P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig7P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig9P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig10P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig11P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig12P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig13P4', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P4_ccontainer",
             children=[
                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P4_c",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "НАУЧ РАБ", id='text1P4_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P4_c', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P2P4_c', value=300, min=300, max=500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card1P4_c', className='card1webP1'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ИССЛЕД_МОЛ", id='text2P4_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P4_c', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P4P4_c', value=250, min=250, max=550, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2P4_c', className='card2webP1'),

                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P4_c', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP4_c',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], className='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P4_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P4_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig4P4_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig5P4_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig6P4_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([

                         html.Div([
                             dcc.Graph(id='fig7P4_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P4_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig9P4_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig10P4_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig11P4_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig12P4_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig12'),

                     ], style={'background-color': '#323436'}),
             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P5container",
             children=[
                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P5",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ЦИФРСТУД", id='text1P5',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P5', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='S6P5', value=3000, min=3000, max=6000, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card1P5'),
                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P5', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P5_ccontainer",
             children=[
                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P5_c",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "НАУЧ РАБ", id='text1P5_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P5_c', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P2P5_c', value=300, min=300, max=500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card1P5_c', className='card1webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ЗП_ППС_РЕАЛ", id='text2P5_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P5_c', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='F2P5_c', value=400, min=400, max=750, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2P5_c', className='card2webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во обучающихся", id='text3P5_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea3P5_c', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='S1P5_c', value=20000, min=20000, max=30000, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card3P5_c', className='card3webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во программ", id='text4P5_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea4P5_c', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='Pr1P5_c', value=140, min=140, max=250, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card4P5_c', className='card4webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Объём СГЗ НИОКР", id='text5P5_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea5P5_c', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='F5P5_c', value=100000, min=100000, max=500000, step=1,
                                                        marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card5P5_c', className='card5webP1_c'),

                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P5_c', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP5_c',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], className='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig4P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig5P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig6P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig7P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig9P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig10P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig11P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig12P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig13P5_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),
             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P6container",
             children=[
                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P6",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "НАУЧ РАБ", id='text1P6',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P6', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P2P6', value=300, min=300, max=500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card1P6', className='card1webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ЗП_ППС_РЕАЛ", id='text2P6',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P6', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='F2P6', value=400, min=400, max=750, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2P6', className='card2webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во обучающихся", id='text3P6',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea3P6', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='S1P6', value=20000, min=20000, max=30000, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card3P6', className='card3webP1_c'),
                                 dbc.Row([
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "Кол-во программ", id='text4P6',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea4P6', className="textarea", readOnly=True,
                                                              style={})
                                             ]),

                                         ], className='container-fluid'),
                                         dbc.CardBody([
                                             dcc.Slider(id='Pr1P6', value=140, min=140, max=250, step=1, marks=None,
                                                        className="slider")]),

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card4P6', className='card4webP1_c'),
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "ОБЪЕМ_СОБСТ_ИИР", id='text5P6',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea5P6', className="textarea", readOnly=True,
                                                              style={}),
                                             ]),
                                             dbc.CardBody([
                                                 dcc.Slider(id='F4P6', value=1000, min=1000, max=150000, step=1,
                                                            marks=None,
                                                            className="slider")])
                                         ], className='container-fluid'),

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card5P6', className='card5webP1_c'),
                                 ]),
                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P6', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP6',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], className='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig4P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig5P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig6P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig7P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig9P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig10P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig11P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig12P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig13P6', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P6_ccontainer",
             children=[
                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P6_c",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "НАУЧ РАБ", id='text1P6_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P6_c', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P2P6_c', value=300, min=300, max=500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card1P6_c', className='card1webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ЗП_ППС_РЕАЛ", id='text2P6_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P6_c', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='F2P6_c', value=400, min=400, max=750, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2P6_c', className='card2webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во обучающихся", id='text3P6_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea3P6_c', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='S1P6_c', value=20000, min=20000, max=30000, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card3P6_c', className='card3webP1_c'),
                                 dbc.Row([
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "Кол-во программ", id='text4P6_c',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea4P6_c', className="textarea", readOnly=True,
                                                              style={})
                                             ]),

                                         ], className='container-fluid'),
                                         dbc.CardBody([
                                             dcc.Slider(id='Pr1P6_c', value=140, min=140, max=250, step=1, marks=None,
                                                        className="slider")]),

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card4P6_c', className='card4webP1_c'),
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "ИСП_РЕЗ_ИНТ_ДЕЯТ", id='text5P6_c',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea5P6_c', className="textarea", readOnly=True,
                                                              style={}),

                                             ]),
                                             dbc.CardBody([
                                                 dcc.Slider(id='F6P6_c', value=1000, min=1000, max=9000, step=1,
                                                            marks=None,
                                                            className="slider")])
                                         ], className='container-fluid')

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card5P6_c', className='card5webP1_c'),
                                 ]),
                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P6_c', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP6_c',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], className='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig4P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig5P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig6P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig7P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig9P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig10P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig11P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig12P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig13P6_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P7_ccontainer",
             children=[
                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P7_c",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "НАУЧ РАБ", id='text1P7_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P7_c', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P2P7_c', value=300, min=300, max=500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card1webP7_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ЗП_ППС_РЕАЛ", id='text2P7_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P7_c', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='F2P7_c', value=400, min=400, max=750, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2webP7_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во обучающихся", id='text3P7_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea3P7_c', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='S1P7_c', value=20000, min=20000, max=30000, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card3webP7_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во программ", id='text4P7_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea4P7_c', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='Pr1P7_c', value=140, min=140, max=250, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card4webP7_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "СТУДБАК", id='text5P7_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea5P7_c', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='S2P7_c', value=8000, min=8000, max=15000, step=1,
                                                        marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card5webP7_c'),

                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "СТУДСПЕЦ", id='text6P7_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea6P7_c', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='S3P7_c', value=1200, min=1200, max=1900, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card6webP7_c'),

                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P7_c', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP7_c',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], className='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig4P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig5P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig6P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig7P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig9P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig10P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig11P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig12P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig13P7_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

             ], style={'height': '100vh', 'background-color': '#323436'}),
    html.Div(id="P8_ccontainer",
             children=[
                     dbc.Row([
                         dbc.Col(
                             html.P(
                                 "P8_c",
                                 style={'font-size': '26px', 'font-weight': 'normal',
                                        'font-family': 'Open Sans', 'color': 'white'}, className='dashname'),
                             width={"size": 10, "offset": 2})
                     ]),
                     dbc.Row([
                         dbc.Col([
                             dbc.Row([
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "НАУЧ РАБ", id='text1P8_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea1P8_c', className="textarea", readOnly=True,
                                                          style={}),
                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='P2P8_c', value=300, min=300, max=500, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid'),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card1P8_c', className='card1webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "ЗП_ППС_РЕАЛ", id='text2P8_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea2P8_c', className="textarea", readOnly=True,
                                                          style={}),

                                         ]),
                                         dbc.CardBody([
                                             dcc.Slider(id='F2P8_c', value=400, min=400, max=750, step=1, marks=None,
                                                        className="slider")])
                                     ], className='container-fluid')

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card2P8_c', className='card2webP1_c'),
                                 dbc.Card([
                                     dbc.Container([
                                         dbc.Row([
                                             html.P(
                                                 "Кол-во обучающихся", id='text3P8_c',
                                                 className="card-text",
                                                 style={'font-size': '16px',
                                                        'font-family': 'Open Sans'}),
                                             dcc.Textarea(id='textarea3P8_c', className="textarea", readOnly=True,
                                                          style={})
                                         ]),

                                     ], className='container-fluid'),
                                     dbc.CardBody([
                                         dcc.Slider(id='S1P8_c', value=20000, min=20000, max=30000, step=1, marks=None,
                                                    className="slider")]),

                                 ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                           "height": "80%"},
                                     id='card3P8_c', className='card3webP1_c'),
                                 dbc.Row([
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "Кол-во программ", id='text4P8_c',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea4P8_c', className="textarea", readOnly=True,
                                                              style={})
                                             ]),

                                         ], className='container-fluid'),
                                         dbc.CardBody([
                                             dcc.Slider(id='Pr1P8_c', value=140, min=140, max=250, step=1, marks=None,
                                                        className="slider")]),

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card4P8_c', className='card4webP1_c'),
                                     dbc.Card([
                                         dbc.Container([
                                             dbc.Row([
                                                 html.P(
                                                     "МАГА_ИНОСТР_СТУД_МОН", id='text5P8_c',
                                                     className="card-text",
                                                     style={'font-size': '16px',
                                                            'font-family': 'Open Sans'}),
                                                 dcc.Textarea(id='textarea5P8_c', className="textarea", readOnly=True,
                                                              style={})
                                             ]),

                                         ], className='container-fluid'),
                                         dbc.CardBody([
                                             dcc.Slider(id='S8P8_c', value=50, min=50, max=200, step=1, marks=None,
                                                        className="slider")]),

                                     ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0",
                                               "height": "80%"},
                                         id='card5P8_c', className='card5webP1_c'),
                                 ]),
                             ], align="center"),

                         ], width={'size': 12}),
                     ], style={'background-color': '#323436', 'margin-bottom': '2% '}),

                     dbc.Row([
                         dbc.Col(
                             html.Div([
                                 dcc.Graph(id='fig1P8_c', config={
                                     'staticPlot': False,  # True, False
                                     'displayModeBar': False,  # True, False, 'hover'
                                     'watermark': True,
                                 }, )
                             ], className='figosn')
                         )

                     ], style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Dropdown(
                                 ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023',
                                 searchable=False,
                                 clearable=False,
                                 id='dropdownP8_c',
                                 style={"width": "70px", "height": "40px"}),
                         ], style={"width": "50%"}),
                     ], className='dropdownrow', style={'background-color': '#323436'}),
                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig2P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig3P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig4P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig5P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig6P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig7P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig8P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig9P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),
                         html.Div([
                             dcc.Graph(id='fig10P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig11P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

                     dbc.Row([
                         html.Div([
                             dcc.Graph(id='fig12P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                         html.Div([
                             dcc.Graph(id='fig13P8_c', config={
                                 'staticPlot': False,  # True, False
                                 'displayModeBar': False,  # True, False, 'hover'
                                 'watermark': True,
                             }, )
                         ], style={"width": "20%", "height": "10%"}, className='fig'),

                     ], style={'background-color': '#323436'}),

             ], style={'height': '100vh', 'background-color': '#323436'}),

], id='container', style={'height': '100vh', 'background-color': '#323436'}, fluid=True)


@app.callback(
    Output('fig1P1', 'figure'),
    [Input('P2P1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure(selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1(selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.0f', template='plotly', title='P1')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure_p2(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_v(selected_year, 625, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )

    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

    return (fig)


@app.callback(
    Output('fig3P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('P2P1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, selected_F2, selected_S1, selected_Pr1)

    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('P2P1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('P2P1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('P2P1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('P2P1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('P2P1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('P2P1', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P4_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('P2P1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('P2P1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_cv(selected_year, selected_Pr1, selected_S1, 5000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('P2P1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p7_cv(selected_year, selected_Pr1, selected_S1, 11500, 1550, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P1', 'figure'),
    [Input('dropdownP1', 'value'),
     Input('P2P1', 'value'),
     Input('F2P1', 'value'),
     Input('S1P1', 'value'),
     Input('Pr1P1', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, selected_Pr1, selected_S1, 125, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#F0FFBB',
                     '2023': '#E4FC8F', '2024': '#E4FC8F', '2025': '#E4FC8F', '2026': '#E4FC8F', '2027': '#E4FC8F',
                     '2028': '#E4FC8F', '2029': '#E4FC8F', '2030': '#E4FC8F'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P1', 'value'), [Input('P2P1', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P1', 'value'), [Input('F2P1', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P1', 'value'), [Input('S1P1', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P1', 'value'), [Input('Pr1P1', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P1_c', 'figure'),
    [Input('Ar1P1_c', 'value'),
     Input('P2P1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure(selected_Ar1, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (ar1,p2,f2,s1,pr1)
    df = foo_p1_c(selected_Ar1, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.2f', template='plotly', title='P1_c')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('P2P1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure_p2(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_v(selected_year, 625, selected_F2, selected_S1, selected_Pr1)

    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('P2P1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, selected_F2, selected_S1, selected_Pr1)

    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('P2P1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('P2P1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('P2P1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('P2P1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('P2P1_c', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P4_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('P2P1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('P2P1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_cv(selected_year, selected_Pr1, selected_S1, 5000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('P2P1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p7_cv(selected_year, selected_Pr1, selected_S1, 11500, 1550, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P1_c', 'figure'),
    [Input('dropdownP1_c', 'value'),
     Input('P2P1_c', 'value'),
     Input('F2P1_c', 'value'),
     Input('S1P1_c', 'value'),
     Input('Pr1P1_c', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, selected_Pr1, selected_S1, 125, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#F0FFBB',
                     '2023': '#E4FC8F', '2024': '#E4FC8F', '2025': '#E4FC8F', '2026': '#E4FC8F', '2027': '#E4FC8F',
                     '2028': '#E4FC8F', '2029': '#E4FC8F', '2030': '#E4FC8F'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P1_c', 'value'), [Input('P2P1_c', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P1_c', 'value'), [Input('F2P1_c', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P1_c', 'value'), [Input('S1P1_c', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P1_c', 'value'), [Input('Pr1P1_c', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea5P1_c', 'value'), [Input('Ar1P1_c', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P2', 'figure'),
    [Input('P3P2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure(selected_P3, selected_F2, selected_S1, selected_Pr1):
    # (p3,f2,s1,pr1)
    df = foo_p2(selected_P3, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.2f', template='plotly', title='P2')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P2', 'figure'),
    [Input('dropdownP2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_v(selected_year, 400, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P2', 'figure'),
    [Input('dropdownP2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, 400, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P2', 'figure'),
    [Input('dropdownP2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, 400, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P2', 'figure'),
    [Input('dropdownP2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, 400, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P2', 'figure'),
    [Input('dropdownP2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, 400, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P2', 'figure'),
    [Input('dropdownP2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, 400, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P2', 'figure'),
    [Input('dropdownP2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, 400, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P2', 'figure'),
    [Input('dropdownP2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, 400)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P2', 'figure'),
    [Input('dropdownP2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_cv(selected_year, selected_Pr1, selected_S1, 5000, selected_F2, 400)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P2', 'figure'),
    [Input('dropdownP2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p7_cv(selected_year, selected_Pr1, selected_S1, 11500, 1550, selected_F2, 400)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P2', 'figure'),
    [Input('dropdownP2', 'value'),
     Input('F2P2', 'value'),
     Input('S1P2', 'value'),
     Input('Pr1P2', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_F2, selected_S1, selected_Pr1):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, selected_Pr1, selected_S1, 125, selected_F2, 400)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P2', 'value'), [Input('P3P2', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P2', 'value'), [Input('F2P2', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P2', 'value'), [Input('S1P2', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P2', 'value'), [Input('Pr1P2', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P2_c', 'figure'),
    [Input('Ar2P2_c', 'value'),
     Input('P2P2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure(selected_Ar2, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (ar2,p2,f2,s1,pr1)
    df = foo_p2_c(selected_Ar2, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.2f', template='plotly', title='P2_c')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('P2P2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure_p2(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_v(selected_year, 625, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('P2P2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('P2P2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('P2P2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('P2P2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('P2P2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('P2P2_c', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P4_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('P2P2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('P2P2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_cv(selected_year, selected_Pr1, selected_S1, 5000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('P2P2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p7_cv(selected_year, selected_Pr1, selected_S1, 11500, 1550, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P2_c', 'figure'),
    [Input('dropdownP2_c', 'value'),
     Input('P2P2_c', 'value'),
     Input('F2P2_c', 'value'),
     Input('S1P2_c', 'value'),
     Input('Pr1P2_c', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, selected_Pr1, selected_S1, 125, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#F0FFBB',
                     '2023': '#E4FC8F', '2024': '#E4FC8F', '2025': '#E4FC8F', '2026': '#E4FC8F', '2027': '#E4FC8F',
                     '2028': '#E4FC8F', '2029': '#E4FC8F', '2030': '#E4FC8F'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P2_c', 'value'), [Input('P2P2_c', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P2_c', 'value'), [Input('F2P2_c', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P2_c', 'value'), [Input('S1P2_c', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P2_c', 'value'), [Input('Pr1P2_c', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea5P2_c', 'value'), [Input('Ar2P2_c', 'value')])
def textarea5input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P3', 'figure'),
    [Input('S5P3', 'value'),
     Input('S2P3', 'value'),
     Input('S3P3', 'value'),
     Input('P2P3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure(selected_S5, selected_S2, selected_S3, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (s5,s2,s3,p2,f2,s1,pr1)
    df = foo_p3(selected_S5, selected_S2, selected_S3, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.2f', template='plotly', title='P3')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('P2P3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure_p2(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_v(selected_year, 625, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('P2P3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('P2P3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('P2P3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('P2P3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('P2P3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('P2P3', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('P2P3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('P2P3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_cv(selected_year, selected_Pr1, selected_S1, 5000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('P2P3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p7_cv(selected_year, selected_Pr1, selected_S1, 11500, 1550, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P3', 'figure'),
    [Input('dropdownP3', 'value'),
     Input('P2P3', 'value'),
     Input('F2P3', 'value'),
     Input('S1P3', 'value'),
     Input('Pr1P3', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, selected_Pr1, selected_S1, 125, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#F0FFBB',
                     '2023': '#E4FC8F', '2024': '#E4FC8F', '2025': '#E4FC8F', '2026': '#E4FC8F', '2027': '#E4FC8F',
                     '2028': '#E4FC8F', '2029': '#E4FC8F', '2030': '#E4FC8F'})
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P3', 'value'), [Input('S5P3', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P3', 'value'), [Input('S2P3', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea6P3', 'value'), [Input('S3P3', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P3', 'value'), [Input('P2P3', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea5P3', 'value'), [Input('F2P3', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P3', 'value'), [Input('S1P3', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea7P3', 'value'), [Input('Pr1P3', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P3_с', 'figure'),
    [Input('Ar3P3_с', 'value'),
     Input('P2P3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure(selected_Ar3, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (ar3,p2,f2,s1,pr1)
    df = foo_p3_c(selected_Ar3, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.2f', template='plotly', title='P3_c')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('P2P3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure_p2(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_v(selected_year, 625, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('P2P3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('P2P3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('P2P3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('P2P3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('P2P3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('P2P3_с', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P4_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('P2P3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('P2P3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_cv(selected_year, selected_Pr1, selected_S1, 5000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('P2P3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p7_cv(selected_year, selected_Pr1, selected_S1, 11500, 1550, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P3_с', 'figure'),
    [Input('dropdownP3_с', 'value'),
     Input('P2P3_с', 'value'),
     Input('F2P3_с', 'value'),
     Input('S1P3_с', 'value'),
     Input('Pr1P3_с', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, selected_Pr1, selected_S1, 125, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#F0FFBB',
                     '2023': '#E4FC8F', '2024': '#E4FC8F', '2025': '#E4FC8F', '2026': '#E4FC8F', '2027': '#E4FC8F',
                     '2028': '#E4FC8F', '2029': '#E4FC8F', '2030': '#E4FC8F'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P3_с', 'value'), [Input('P2P3_с', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P3_с', 'value'), [Input('F2P3_с', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P3_с', 'value'), [Input('S1P3_с', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P3_с', 'value'), [Input('Pr1P3_с', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea5P3_с', 'value'), [Input('Ar3P3_с', 'value')])
def textarea5input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P4', 'figure'),
    [Input('P2P4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure(selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (p2,f2,s1,pr1)
    df = foo_p4(selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.0f', template='plotly', title='P4')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('P2P4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure_p2(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_v(selected_year, 625, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('P2P4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('P2P4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('P2P4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('P2P4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('P2P4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('P2P4', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P4_C',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('P2P4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('P2P4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_cv(selected_year, selected_Pr1, selected_S1, 5000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('P2P4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p7_cv(selected_year, selected_Pr1, selected_S1, 11500, 1550, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P4', 'figure'),
    [Input('dropdownP4', 'value'),
     Input('P2P4', 'value'),
     Input('F2P4', 'value'),
     Input('S1P4', 'value'),
     Input('Pr1P4', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, selected_Pr1, selected_S1, 125, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#F0FFBB',
                     '2023': '#E4FC8F', '2024': '#E4FC8F', '2025': '#E4FC8F', '2026': '#E4FC8F', '2027': '#E4FC8F',
                     '2028': '#E4FC8F', '2029': '#E4FC8F', '2030': '#E4FC8F'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P4', 'value'), [Input('P2P4', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P4', 'value'), [Input('F2P4', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P4', 'value'), [Input('S1P4', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P4', 'value'), [Input('Pr1P4', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P4_c', 'figure'),
    [Input('P4P4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure(selected_P4, selected_P2):
    # (p4,p2)
    df = foo_p4_c(selected_P4, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.2f', template='plotly', title='P4_c')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P4_c', 'figure'),
    [Input('dropdownP4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_P2):
    df = foo_p1_v(selected_year, selected_P2, 575, 25000, 195)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P4_c', 'figure'),
    [Input('dropdownP4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_P2):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, 575, 25000, 195)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P4_c', 'figure'),
    [Input('dropdownP4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_P2):
    df = foo_p4_v(selected_year, selected_P2, 575, 25000, 195)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P4_c', 'figure'),
    [Input('dropdownP4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_P2):
    df = foo_p6_v(selected_year, 75000, selected_P2, 575, 25000, 195)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P4_c', 'figure'),
    [Input('dropdownP4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_P2):
    df = foo_p1_cv(selected_year, 250, selected_P2, 575, 25000, 195)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P4_c', 'figure'),
    [Input('dropdownP4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_P2):
    df = foo_p2_cv(selected_year, 350, selected_P2, 575, 25000, 195)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P4_c', 'figure'),
    [Input('dropdownP4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2):
    df = foo_p3_cv(selected_year, 50, selected_P2, 575, 25000, 195)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P4_c', 'figure'),
    [Input('dropdownP4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_P2):
    df = foo_p5_cv(selected_year, 195, 25000, 300000, 575, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P4_c', 'figure'),
    [Input('dropdownP4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_P2, ):
    df = foo_p6_cv(selected_year, 195, 25000, 5000, 575, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_C',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P4_c', 'figure'),
    [Input('dropdownP4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_P2):
    df = foo_p7_cv(selected_year, 195, 25000, 11500, 1550, 575, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P4_c', 'figure'),
    [Input('dropdownP4_c', 'value'),
     Input('P2P4_c', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_P2):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, 195, 25000, 125, 575, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P4_c', 'value'), [Input('P2P4_c', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P4_c', 'value'), [Input('P4P4_c', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P5', 'figure'),
    [Input('S6P5', 'value')])
# create our callback function
def update_figure(selected_S6):
    # (s6)
    df = foo_p5(selected_S6)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.2f', template='plotly', title='P1')
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P5', 'value'), [Input('S6P5', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P5_c', 'figure'),
    [Input('F5P5_c', 'value'),
     Input('P2P5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure(selected_F5, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (pr1,s1,f5,f2,p2)
    df = foo_p5_c(selected_Pr1, selected_S1, selected_F5, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.0f', template='plotly', title='P5_c')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('P2P5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure_p2(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_v(selected_year, 625, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('P2P5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('P2P5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('P2P5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('P2P5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('P2P5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('P2P5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('P2P5_c', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P4_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('P2P5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_cv(selected_year, selected_Pr1, selected_S1, 5000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('P2P5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p7_cv(selected_year, selected_Pr1, selected_S1, 11500, 1550, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P5_c', 'figure'),
    [Input('dropdownP5_c', 'value'),
     Input('P2P5_c', 'value'),
     Input('F2P5_c', 'value'),
     Input('S1P5_c', 'value'),
     Input('Pr1P5_c', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, selected_Pr1, selected_S1, 125, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#F0FFBB',
                     '2023': '#E4FC8F', '2024': '#E4FC8F', '2025': '#E4FC8F', '2026': '#E4FC8F', '2027': '#E4FC8F',
                     '2028': '#E4FC8F', '2029': '#E4FC8F', '2030': '#E4FC8F'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P5_c', 'value'), [Input('P2P5_c', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P5_c', 'value'), [Input('F2P5_c', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P5_c', 'value'), [Input('S1P5_c', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P5_c', 'value'), [Input('Pr1P5_c', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea5P5_c', 'value'), [Input('F5P5_c', 'value')])
def textarea5input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P6', 'figure'),
    [Input('F4P6', 'value'),
     Input('P2P6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure(selected_F4, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (f4,p2,f2,s1,pr1)
    df = foo_p6(selected_F4, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.2f', template='plotly', title='P1_c')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('P2P6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure_p2(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_v(selected_year, 625, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('P2P6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('P2P6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('P2P6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('P2P6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('P2P6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('P2P6', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P4_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('P2P6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('P2P6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_cv(selected_year, selected_Pr1, selected_S1, 5000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('P2P6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p7_cv(selected_year, selected_Pr1, selected_S1, 11500, 1550, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P6', 'figure'),
    [Input('dropdownP6', 'value'),
     Input('P2P6', 'value'),
     Input('F2P6', 'value'),
     Input('S1P6', 'value'),
     Input('Pr1P6', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, selected_Pr1, selected_S1, 125, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#F0FFBB',
                     '2023': '#E4FC8F', '2024': '#E4FC8F', '2025': '#E4FC8F', '2026': '#E4FC8F', '2027': '#E4FC8F',
                     '2028': '#E4FC8F', '2029': '#E4FC8F', '2030': '#E4FC8F'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P6', 'value'), [Input('P2P6', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P6', 'value'), [Input('F2P6', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P6', 'value'), [Input('S1P6', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P6', 'value'), [Input('Pr1P6', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea5P6', 'value'), [Input('F4P6', 'value')])
def textarea5input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P6_c', 'figure'),
    [Input('Pr1P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('F6P6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('P2P6_c', 'value')])
# create our callback function
def update_figure(selected_Pr1, selected_S1, selected_F6, selected_F2, selected_P2):
    # (pr1,s1,f6,f2,p2)
    df = foo_p6_c(selected_Pr1, selected_S1, selected_F6, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.2f', template='plotly', title='P1_c')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('P2P6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('Pr1P6_c', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('Pr1P6_c', 'value')])
# create our callback function
def update_figure_p2(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_v(selected_year, 625, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('P2P6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('Pr1P6_c', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('P2P6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('Pr1P6_c', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('P2P6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('Pr1P6_c', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('P2P6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('Pr1P6_c', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('P2P6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('Pr1P6_c', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('P2P6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('Pr1P6_c', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('P2P6_c', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P4_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('P2P6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('Pr1P6_c', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0s', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('P2P6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('Pr1P6_c', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p7_cv(selected_year, selected_Pr1, selected_S1, 11500, 1550, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P6_c', 'figure'),
    [Input('dropdownP6_c', 'value'),
     Input('P2P6_c', 'value'),
     Input('F2P6_c', 'value'),
     Input('S1P6_c', 'value'),
     Input('Pr1P6_c', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, selected_Pr1, selected_S1, 125, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#F0FFBB',
                     '2023': '#E4FC8F', '2024': '#E4FC8F', '2025': '#E4FC8F', '2026': '#E4FC8F', '2027': '#E4FC8F',
                     '2028': '#E4FC8F', '2029': '#E4FC8F', '2030': '#E4FC8F'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P6_c', 'value'), [Input('P2P6_c', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P6_c', 'value'), [Input('F2P6_c', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P6_c', 'value'), [Input('S1P6_c', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P6_c', 'value'), [Input('Pr1P6_c', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea5P6_c', 'value'), [Input('F6P6_c', 'value')])
def textarea5input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P8_c', 'figure'),
    [Input('Pr1P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('S8P8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('P2P8_c', 'value')])
# create our callback function
def update_figure(selected_Pr1, selected_S1, selected_S8, selected_F2, selected_P2):
    df = foo_p8_c(selected_Pr1, selected_S1, selected_S8, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.2f', template='plotly', title='P1_c')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('P2P8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('Pr1P8_c', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('Pr1P8_c', 'value')])
# create our callback function
def update_figure_p2(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_v(selected_year, 625, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('P2P8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('Pr1P8_c', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('P2P8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('Pr1P8_c', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('P2P8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('Pr1P8_c', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('P2P8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('Pr1P8_c', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('P2P8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('Pr1P8_c', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('P2P8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('Pr1P8_c', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('P2P8_c', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P4_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('P2P8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('Pr1P8_c', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('P2P8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('Pr1P8_c', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_cv(selected_year, selected_Pr1, selected_S1, 5000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P8_c', 'figure'),
    [Input('dropdownP8_c', 'value'),
     Input('P2P8_c', 'value'),
     Input('F2P8_c', 'value'),
     Input('S1P8_c', 'value'),
     Input('Pr1P8_c', 'value')])
# create our callback function
def update_figure_p7_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p7_cv(selected_year, selected_Pr1, selected_S1, 11500, 1550, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P7-c',
                 color_discrete_map={
                     '2022': '#F0FFBB',
                     '2023': '#E4FC8F', '2024': '#E4FC8F', '2025': '#E4FC8F', '2026': '#E4FC8F', '2027': '#E4FC8F',
                     '2028': '#E4FC8F', '2029': '#E4FC8F', '2030': '#E4FC8F'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P8_c', 'value'), [Input('P2P8_c', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P8_c', 'value'), [Input('F2P8_c', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P8_c', 'value'), [Input('S1P8_c', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P8_c', 'value'), [Input('Pr1P8_c', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea5P8_c', 'value'), [Input('S8P8_c', 'value')])
def textarea5input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('fig1P7_c', 'figure'),
    [Input('Pr1P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('S2P7_c', 'value'),
     Input('S3P7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('P2P7_c', 'value')])
# create our callback function
def update_figure(selected_Pr1, selected_S1, selected_S2, selected_S3, selected_F2, selected_P2):
    # (pr1,s1,s2,s3,f2,p2)
    df = foo_p7_c(selected_Pr1, selected_S1, selected_S2, selected_S3, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.2f', template='plotly', title='P1_c')
    fig.update_layout(
        plot_bgcolor='#515151',
        paper_bgcolor='#515151', font_color="#D4D4D4", xaxis_title=None,
        yaxis_title=None, title_x=0.5, margin=dict(b=10, pad=15))
    fig.update_traces(marker_color='#83C3FF')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig2P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('P2P7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('Pr1P7_c', 'value')])
# create our callback function
def update_figure_p1(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P1',
                 color_discrete_map={
                     '2022': '#6BBFFF',
                     '2023': '#027AD3', '2024': '#027AD3', '2025': '#027AD3', '2026': '#027AD3', '2027': '#027AD3',
                     '2028': '#027AD3', '2029': '#027AD3', '2030': '#027AD3'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig3P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('Pr1P7_c', 'value')])
# create our callback function
def update_figure_p2(selected_year, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_v(selected_year, 625, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2',
                 color_discrete_map={
                     '2022': '#76C5F9',
                     '2023': '#1584CE', '2024': '#1584CE', '2025': '#1584CE', '2026': '#1584CE', '2027': '#1584CE',
                     '2028': '#1584CE', '2029': '#1584CE', '2030': '#1584CE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig4P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('P2P7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('Pr1P7_c', 'value')])
# create our callback function
def update_figure_p3(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3',
                 color_discrete_map={
                     '2022': '#83CBF3',
                     '2023': '#298EC8', '2024': '#298EC8', '2025': '#298EC8', '2026': '#298EC8', '2027': '#298EC8',
                     '2028': '#298EC8', '2029': '#298EC8', '2030': '#298EC8'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig5P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('P2P7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('Pr1P7_c', 'value')])
# create our callback function
def update_figure_p4(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P4',
                 color_discrete_map={
                     '2022': '#8FD1EC',
                     '2023': '#3C99C2', '2024': '#3C99C2', '2025': '#3C99C2', '2026': '#3C99C2', '2027': '#3C99C2',
                     '2028': '#3C99C2', '2029': '#3C99C2', '2030': '#3C99C2'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig6P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('P2P7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('Pr1P7_c', 'value')])
# create our callback function
def update_figure_p6(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6',
                 color_discrete_map={
                     '2022': '#9BD7E6',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig7P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('P2P7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('Pr1P7_c', 'value')])
# create our callback function
def update_figure_p1_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P1_c',
                 color_discrete_map={
                     '2022': '#B7F3F8',
                     '2023': '#50A3BC', '2024': '#50A3BC', '2025': '#50A3BC', '2026': '#50A3BC', '2027': '#50A3BC',
                     '2028': '#50A3BC', '2029': '#50A3BC', '2030': '#50A3BC'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig8P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('P2P7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('Pr1P7_c', 'value')])
# create our callback function
def update_figure_p2_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P2_c',
                 color_discrete_map={
                     '2022': '#C4F6EE',
                     '2023': '#82D6CA', '2024': '#82D6CA', '2025': '#82D6CA', '2026': '#82D6CA', '2027': '#82D6CA',
                     '2028': '#82D6CA', '2029': '#82D6CA', '2030': '#82D6CA'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig9P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('P2P7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('Pr1P7_c', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P3_c',
                 color_discrete_map={
                     '2022': '#D2FFE8',
                     '2023': '#93DDBD', '2024': '#93DDBD', '2025': '#93DDBD', '2026': '#93DDBD', '2027': '#93DDBD',
                     '2028': '#93DDBD', '2029': '#93DDBD', '2030': '#93DDBD'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig10P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('P2P7_c', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P4_c',
                 color_discrete_map={
                     '2022': '#CBEECD',
                     '2023': '#93E0BE', '2024': '#93E0BE', '2025': '#93E0BE', '2026': '#93E0BE', '2027': '#93E0BE',
                     '2028': '#93E0BE', '2029': '#93E0BE', '2030': '#93E0BE'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig11P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('P2P7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('Pr1P7_c', 'value')])
# create our callback function
def update_figure_p5_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.0f', template='plotly', title='P5_c',
                 color_discrete_map={
                     '2022': '#DBFFC7',
                     '2023': '#A9EAB0', '2024': '#A9EAB0', '2025': '#A9EAB0', '2026': '#A9EAB0', '2027': '#A9EAB0',
                     '2028': '#A9EAB0', '2029': '#A9EAB0', '2030': '#A9EAB0'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig12P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('P2P7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('Pr1P7_c', 'value')])
# create our callback function
def update_figure_p6_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_cv(selected_year, selected_Pr1, selected_S1, 5000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P6_c',
                 color_discrete_map={
                     '2022': '#E4FAC0',
                     '2023': '#D6F8A1', '2024': '#D6F8A1', '2025': '#D6F8A1', '2026': '#D6F8A1', '2027': '#D6F8A1',
                     '2028': '#D6F8A1', '2029': '#D6F8A1', '2030': '#D6F8A1'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(
    Output('fig13P7_c', 'figure'),
    [Input('dropdownP7_c', 'value'),
     Input('P2P7_c', 'value'),
     Input('F2P7_c', 'value'),
     Input('S1P7_c', 'value'),
     Input('Pr1P7_c', 'value')])
# create our callback function
def update_figure_p8_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    # (year,pr1,s1,s8,f2,p2)
    df = foo_p8_cv(selected_year, selected_Pr1, selected_S1, 125, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2f', template='plotly', title='P8_c',
                 color_discrete_map={
                     '2022': '#F0FFBB',
                     '2023': '#E4FC8F', '2024': '#E4FC8F', '2025': '#E4FC8F', '2026': '#E4FC8F', '2027': '#E4FC8F',
                     '2028': '#E4FC8F', '2029': '#E4FC8F', '2030': '#E4FC8F'}
                 )
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      plot_bgcolor='#515151',
                      paper_bgcolor='#515151', font_color="#D4D4D4")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#708283",
            font_size=13,
            font_family="Open Sans"
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#85857d')
    for data in fig.data:
        data["width"] = 0.5
    fig.update_layout(showlegend=False)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return (fig)


@app.callback(Output('textarea1P7_c', 'value'), [Input('P2P7_c', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2P7_c', 'value'), [Input('F2P7_c', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3P7_c', 'value'), [Input('S1P7_c', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4P7_c', 'value'), [Input('Pr1P7_c', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea5P7_c', 'value'), [Input('S2P7_c', 'value')])
def textarea5input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea6P7_c', 'value'), [Input('S3P7_c', 'value')])
def textarea5input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(
    Output('P1container', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P1':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P1_ccontainer', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P1_c':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P2container', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P2':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P2_ccontainer', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P2_c':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P3container', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P3':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P3_ccontainer', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P3_c':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P4container', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P4':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P4_ccontainer', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P4_c':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P5container', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P5':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P5_ccontainer', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P5_c':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P6container', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P6':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P6_ccontainer', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P6_c':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P7_ccontainer', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P7_c':
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('P8_ccontainer', 'style'),
    [Input('dropdownpriorty', 'value')])
# create our callback function
def hide_graph(value):
    if value == 'P8_c':
        return {'display': 'block'}
    return {'display': 'none'}


if __name__ == '__main__':
    app.run_server(debug=True)
