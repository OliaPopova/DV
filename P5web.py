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
                                "ЦИФРСТУД", id='text1',
                                className="card-text",
                                style={'font-size': '16px',
                                       'font-family': 'Open Sans'}),
                            dcc.Textarea(id='textarea1', className="textarea", readOnly=True,
                                         style={}),
                        ]),
                        dbc.CardBody([
                            dcc.Slider(id='S6', value=3000, min=3000, max=6000, step=1, marks=None,
                                       className="slider")])
                    ], className='container-fluid'),

                ], style={"width": "25%", 'border-radius': '15px', "border": "1px #E0E0E0", "height": "80%"},
                    id='card1P5'),
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


], style={'height': '100vh', 'background-color': '#323436'}, fluid=True)


@app.callback(
    Output('fig1', 'figure'),
    [Input('S6', 'value')])
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

@app.callback(Output('textarea1', 'value'), [Input('S6', 'value')])
def textarea1input(normv):
    if normv:
        textareav = str(normv)
        return textareav

if __name__ == '__main__':
    app.run_server(debug=True)
