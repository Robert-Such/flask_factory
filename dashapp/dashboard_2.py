from app import db
from app.models import Drawing
from dash import dash, html, dcc, Input, Output, State
from dash import dash_table
import pandas as pd
from .layout import html_layout
from flask import flash




def dashboard_2(server):
    app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashboard_2/",
        external_stylesheets=['/static/main.css']
    )

    app.index_string = html_layout

    app.layout = html.Div(children=[
        html.Div([
            html.Label('Drawing Type?'),
            dcc.Dropdown(
                id='type',
                options=[
                    {'label': 'Part', 'value': 200},
                    {'label': 'Outline', 'value': 210},
                ],
                value=None
            ),
            html.Label('Size?'),
            dcc.Dropdown(
                id='size',
                options=[
                    {'label': 'A', 'value': 'A'},
                    {'label': 'B', 'value': 'B'},
                ],
                value=None
            ),
            html.Label('Drawn By?'),
            dcc.Dropdown(
                id='drawn',
                options=[
                    {'label': 'Robert Such', 'value': 'RS'},
                    {'label': 'Mike Jones', 'value': 'MJ'},
                ],
                value=None
            ),
            html.Button('Reserve Number', id='btn', n_clicks=0),
            dash_table.DataTable(id='table', data=[], sort_by=[{'column_id': 'id', 'direction': 'desc'}],)

        ])])


    @app.callback(
        Output('table', 'data'), Output('table', 'columns'),
        [Input('btn', 'n_clicks')],
        [State('type', 'value'),
        State('size', 'value'),
        State('drawn', 'value')],
    )
    def updateTable(n_clicks, type, size, drawn):
        drawings = Drawing.query
        df = pd.read_sql(drawings.statement, drawings.session.bind).sort_values(by='id', ascending=False).head(10)
        if n_clicks > 0:
            drawing = Drawing(type=type, size=size, drawn=drawn)
            db.session.add(drawing)
            db.session.commit()
            flash('Your post has been created!', 'success')
            drawings = Drawing.query
            df = pd.read_sql(drawings.statement, drawings.session.bind).sort_values(by='id', ascending=False).head(10)
            return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]
        return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]



    return app.server
