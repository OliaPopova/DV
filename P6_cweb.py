import dash
import numpy
import plotly.graph_objects as go
from P1 import foo_p1_v
from P1_c import foo_p1_cv
from P2 import foo_p2_v
from P2_c import foo_p2_cv
from P3 import foo_p3_v
from P3_c import foo_p3_cv
from P4 import foo_p4_v
from P4_c import foo_p4_cv
from P5_c import foo_p5_cv
from P6 import foo_p6_v
from P6_c import foo_p6_c
from P7_c import foo_p7_cv
from P8_c import foo_p8_cv

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
                "P6_c",
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
                                "P2", id='text1',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea1', className="textarea", readOnly=True,
                                         style={}),
                        ]),
                        dbc.CardBody([
                            dcc.Slider(id='P2', value=300, min=300, max=500, step=1, marks=None,
                                       className="P2slider")])
                    ], className='container-fluid'),

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card1webP1_c'),
                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "F2", id='text2',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea2', className="textarea", readOnly=True,
                                         style={}),

                        ]),
                        dbc.CardBody([
                            dcc.Slider(id='F2', value=400, min=400, max=750, step=1, marks=None,
                                       className="F2slider")])
                    ], className='container-fluid')

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card2webP1_c'),
                dbc.Card([
                    dbc.Container([
                        dbc.Row([
                            html.P(
                                "S1", id='text3',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea3', className="textarea", readOnly=True,
                                         style={})
                        ]),

                    ], className='container-fluid'),
                    dbc.CardBody([
                        dcc.Slider(id='S1', value=20000, min=20000, max=30000, step=1, marks=None,
                                   className="S1slider")]),

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card3webP1_c'),
                dbc.Row([
                    dbc.Card([
                        dbc.Container([
                            dbc.Row([
                                html.P(
                                    "Pr1", id='text4',
                                    className="card-text",
                                    style={'font-size': '16px',
                                           'font-family': 'Open Sans'}),
                                dcc.Textarea(id='textarea4', className="textarea", readOnly=True,
                                             style={})
                            ]),

                        ], className='container-fluid'),
                        dbc.CardBody([
                            dcc.Slider(id='Pr1', value=140, min=140, max=250, step=1, marks=None,
                                       className="Pr1slider")]),

                    ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                        id='card4webP1_c'),
                    dbc.Card([
                        dbc.Container([
                            dbc.Row([
                                html.P(
                                    "F6", id='text5',
                                    className="card-text",
                                    style={'font-size': '16px',
                                           'font-family': 'Open Sans'}),
                                dcc.Textarea(id='textarea5', className="textarea", readOnly=True,
                                             style={}),

                            ]),
                            dbc.CardBody([
                                dcc.Slider(id='F6', value=1000, min=1000, max=9000, step=1, marks=None,
                                           className="F6slider")])
                        ], className='container-fluid')

                    ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                        id='card5webP1_c'),
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
    [Input('Pr1', 'value'),
     Input('S1', 'value'),
     Input('F6', 'value'),
     Input('F2', 'value'),
     Input('P2', 'value')])
# create our callback function
def update_figure(selected_Pr1, selected_S1, selected_F6, selected_F2, selected_P2):
    # (pr1,s1,f6,f2,p2)
    df = foo_p6_c(selected_Pr1, selected_S1, selected_F6, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', text_auto='.4s', template='plotly', title='P1_c')
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
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P1')
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
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P2')
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
def update_figure_p3(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_v(selected_year, 1750, 11500, 1550, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P3')
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
def update_figure_p4(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p4_v(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P4')
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
def update_figure_p6(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p6_v(selected_year, 75000, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P6')
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
def update_figure_p1_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p1_cv(selected_year, 250, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P1_c')
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
def update_figure_p2_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p2_cv(selected_year, 350, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P2_c')
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
     Input('P2', 'value'),
     Input('F2', 'value'),
     Input('S1', 'value'),
     Input('Pr1', 'value')])
# create our callback function
def update_figure_p3_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p3_cv(selected_year, 50, selected_P2, selected_F2, selected_S1, selected_Pr1)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P3_c')
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
     Input('P2', 'value')])
# create our callback function
def update_figure_p4_с(selected_year, selected_P2):
    df = foo_p4_cv(selected_year, 400, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P4_c')
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
def update_figure_p5_с(selected_year, selected_P2, selected_F2, selected_S1, selected_Pr1):
    df = foo_p5_cv(selected_year, selected_Pr1, selected_S1, 300000, selected_F2, selected_P2)
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P5_c')
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
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P7_c')
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
    fig = px.bar(data_frame=df, x='год', y='значение', color='год', text_auto='.2s', template='plotly', title='P8_c')
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


@app.callback(Output('textarea1', 'value'), [Input('P2', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea2', 'value'), [Input('F2', 'value')])
def textarea2input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea3', 'value'), [Input('S1', 'value')])
def textarea3input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea4', 'value'), [Input('Pr1', 'value')])
def textarea4input(normv):
    if normv:
        textareav = str(normv)
        return textareav


@app.callback(Output('textarea5', 'value'), [Input('F6', 'value')])
def textarea5input(normv):
    if normv:
        textareav = str(normv)
        return textareav


if __name__ == '__main__':
    app.run_server(debug=True)
