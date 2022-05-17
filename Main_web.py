import dash_bootstrap_components as dbc
import dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server

app.layout =  dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Active", active=True, href="file:///D:\Job_projects\PY_dv\P1web.py")),
        #D:\Job_projects\PY_dv
        dbc.NavItem(dbc.NavLink("A link", href="#")),
        dbc.NavItem(dbc.NavLink("Another link", href="#")),
        dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
    ],
    vertical="md",
)

if __name__ == '__main__':
    app.run_server(debug=True)