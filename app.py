import dash
import dash_core_components as dbc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_table

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Header(className="site-header", children=[
        html.Div(className="wrapper site-header__wrapper", children=[
            html.Img(src="/assets/logo.jpg", className="logo"),
            html.H1(children="CoGhent:dashboard")
        ])
    ]),
    html.Div(children=[
        dash_table.DataTable(
            id="table_overal_count",
            columns=
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)