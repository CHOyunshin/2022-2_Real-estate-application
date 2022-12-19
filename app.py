import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import Input, Output, State, dcc, html

from layout.mapboxgl.test02 import *
from layout.mapboxgl.output.convert import *
# import pandas as pd

# import page contents as dash-html components 
from layout import *
from layout.dash_html_pages import *
import chart_studio.tools as tls
token = 'pk.eyJ1IjoieXVuc2hpbmNobyIsImEiOiJjbGJxNWMyaXQwZmJ5M3FyN3drYjlsenQwIn0.EhOKGEak-6G4vqj--BxC5w'
from mapboxgl.utils import create_numeric_stops


app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # these meta_tags ensure content is scaled correctly on different devices
    # see: https://www.w3schools.com/css/css_rwd_viewport.asp for more
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

# we use the Row and Col components to construct the sidebar header

# it consists of a title, and a toggle, the latter is hidden on large screens

sidebar_header = dbc.Row(
    [
        # Page 제목과 class로 사이즈 조절 
        dbc.Col(html.H1("REPO", className="display-1")),
        dbc.Col(html.H3("Real Estate Portfolio Optimization", className="display-10")),  
        dbc.Col(
            html.Button(
                # use the Bootstrap navbar-toggler classes to style the toggle
                html.Span(className="navbar-toggler-icon"),
                className="navbar-toggler",
                # the navbar-toggler classes don't set color, so we do it here
                style={
                    "color": "rgba(0,0,0,.5)",
                    "border-color": "rgba(0,0,0,.1)",
                },
                id="toggle",
            ),
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "Category "
                    "links",
                    className="lead",
                ),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Page 1", href="/page-1", active="exact"),
                    dbc.NavLink("Geo - Data", href="/page-2", active="exact"),
                    dbc.NavLink("Geo - Data2", href="/page-3", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)

content = html.Div(id="page-content")
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div([
                    html.H1('Hello Dash'),
                    html.Div([
                    html.P('Dash converts Python classes into HTML'),
                    html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ])
])
    # page layout test 
    elif pathname == "/page-1":
        return page01_dash_html_layout()

    elif pathname == "/page-2":
        # 지도 설정은 https://plotly.com/python/reference/layout/mapbox/ 에서 가능하다. 
        fig = page02_dash_html_layout()
        # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.update_layout(width = 1500, height = 1000, mapbox_style="light", mapbox_accesstoken=token,
                            mapbox_zoom=10.5)
        fig.update_mapboxes(pitch=45, bearing = 15)
        return html.Div(
            # html.H1(children='Seoul Map as '),
            children=[
                html.Div(
                    [dcc.Graph(figure= fig),
                    # page01_dash_html_layout()]
                    ]
                ),
                html.Div(
                    [dcc.Graph(figure= fig),
                    # page01_dash_html_layout()]
                    ]
                ),
            ]
        )
    elif pathname == "/page-3":
        return html.Div(
            [
            
            ]
        )

    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

@app.callback(
    Output("collapse", "is_open"),
    [Input("toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server(port=8880, debug=True)
