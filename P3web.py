import dash
from P1 import foo_p1_v
from P1_c import foo_p1_cv
from P2 import foo_p2_v
from P2_c import foo_p2_cv
from P3 import foo_p3
from P3_c import foo_p3_cv
from P4 import foo_p4_v
from P4_c import foo_p4_cv
from P5_c import foo_p5_cv
from P6 import foo_p6_v
from P6_c import foo_p6_cv
from P7_c import foo_p7_cv
from P8_c import foo_p8_cv

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
                                "СТУДКВАЛ", id='text1',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea1', className="textarea", readOnly=True,
                                         style={}),
                        ]),
                        dbc.CardBody([
                            dcc.Slider(id='S5', value=1000, min=1000, max=2500, step=1, marks=None,
                                       className="slider")])
                    ], className='container-fluid'),

                ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card1webP3'),
                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "СТУДБАК", id='text2',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea2', className="textarea", readOnly=True,
                                         style={}),

                        ]),
                        dbc.CardBody([
                            dcc.Slider(id='S2', value=8000, min=8000, max=15000, step=1, marks=None,
                                       className="slider")])
                    ], className='container-fluid')

                ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card2webP3'),
                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "Кол-во обучающихся", id='text3',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea3', className="textarea", readOnly=True,
                                         style={})
                        ]),

                    ], className='container-fluid'),
                    dbc.CardBody([
                        dcc.Slider(id='S1', value=20000, min=20000, max=30000, step=1, marks=None,
                                       className="slider")]),

                ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card3webP3'),

                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "НАУЧ РАБ", id='text4',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea4', className="textarea", readOnly=True,
                                         style={}),
                        ]),
                        dbc.CardBody([
                            dcc.Slider(id='P2', value=300, min=300, max=500, step=1, marks=None,
                                       className="slider")])
                    ], className='container-fluid'),

                ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card4webP3'),

                dbc.Row([
                    dbc.Card([
                        dbc.Container([
                            dbc.Row([
                                html.P(
                                    "ЗП_ППС_РЕАЛ", id='text5',
                                    className="card-text",
                                    style={'font-size': '16px',
                                           'font-family': 'Open Sans'}),
                                dcc.Textarea(id='textarea5', className="textarea", readOnly=True,
                                             style={}),

                            ]),
                            dbc.CardBody([
                                dcc.Slider(id='F2', value=400, min=400, max=750, step=1, marks=None,
                                           className="slider")])
                        ], className='container-fluid')

                    ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                        id='card5webP3'),
                    dbc.Card([
                        dbc.Container([
                            dbc.Row([
                                html.P(
                                    "СТУДСПЕЦ", id='text6',
                                    className="card-text",
                                    style={'font-size': '16px',
                                           'font-family': 'Open Sans'}),
                                dcc.Textarea(id='textarea6', className="textarea", readOnly=True,
                                             style={})
                            ]),

                        ], className='container-fluid'),
                        dbc.CardBody([
                            dcc.Slider(id='S3', value=1200, min=1200, max=1900, step=1, marks=None,
                                   className="slider")]),

                    ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                        id='card6webP3'),

                    dbc.Card([
                        dbc.Container([
                            dbc.Row([
                                html.P(
                                    "Кол-во программ", id='text7',
                                    className="card-text",
                                    style={'font-size': '16px',
                                           'font-family': 'Open Sans'}),
                                dcc.Textarea(id='textarea7', className="textarea", readOnly=True,
                                             style={})
                            ]),

                        ], className='container-fluid'),
                        dbc.CardBody([
                            dcc.Slider(id='Pr1', value=140, min=140, max=250, step=1, marks=None,
                                       className="slider")]),

                    ], style={"width": "22%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                        id='card7webP3'),
                ]),
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
            ], className='figosn')
        )

    ], style={'background-color': '#323436'}),
    dbc.Row([
        html.Div([
            dcc.Dropdown(
                ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'], '2023', searchable=False,
                clearable=False,
                id='dropdown',
                style={"width": "70px", "height": "40px"}),
        ], style={"width": "50%"}),
    ], id='dropdownrow', style={'background-color': '#323436'}),
    dbc.Row([
        html.Div([
            dcc.Graph(id='fig2', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),

        html.Div([
            dcc.Graph(id='fig3', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),

        html.Div([
            dcc.Graph(id='fig4', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),
        html.Div([
            dcc.Graph(id='fig5', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),

        html.Div([
            dcc.Graph(id='fig6', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),

    ], style={'background-color': '#323436'}),

    dbc.Row([
        html.Div([
            dcc.Graph(id='fig7', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),

        html.Div([
            dcc.Graph(id='fig8', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),

        html.Div([
            dcc.Graph(id='fig9', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),
        html.Div([
            dcc.Graph(id='fig10', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),

        html.Div([
            dcc.Graph(id='fig11', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),

    ], style={'background-color': '#323436'}),

    dbc.Row([
        html.Div([
            dcc.Graph(id='fig12', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),

        html.Div([
            dcc.Graph(id='fig13', config={
                'staticPlot': False,  # True, False
                'displayModeBar': False,  # True, False, 'hover'
                'watermark': True,
            }, )
        ], style={"width": "20%", "height": "10%"}, className='fig'),

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
    Output('fig2', 'figure'),
    [Input('dropdown', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
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
    Output('fig3', 'figure'),
    [Input('dropdown', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
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
    Output('fig4', 'figure'),
    [Input('dropdown', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
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
    Output('fig5', 'figure'),
    [Input('dropdown', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
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
    Output('fig6', 'figure'),
    [Input('dropdown', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
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
    Output('fig7', 'figure'),
    [Input('dropdown', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
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
    Output('fig8', 'figure'),
    [Input('dropdown', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
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
    Output('fig9', 'figure'),
    [Input('dropdown', 'value'),
     Input('P2', 'value')])
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
    Output('fig10', 'figure'),
    [Input('dropdown', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
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
    Output('fig11', 'figure'),
    [Input('dropdown', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
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
    Output('fig12', 'figure'),
    [Input('dropdown', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
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
    Output('fig13', 'figure'),
    [Input('dropdown', 'value'),
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
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


@app.callback(Output('textarea6', 'value'), [Input('S3', 'value')])
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


@app.callback(Output('textarea3', 'value'), [Input('S1', 'value')])
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
