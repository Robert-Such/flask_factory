from app import db
from app.models import Employee
from dash import dash, html, dcc, Input, Output, State
from dash import dash_table
import pandas as pd
from .layout import html_layout
from flask import flash




def dashboard_3(server):
    app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashboard_3/",
        external_stylesheets=['/static/main.css']
    )

    app.index_string = html_layout

    app.layout = html.Div(children=[
        html.Div([
            html.Label('First Name?'),
            dcc.Input(
                id='first_name',
                placeholder='Enter first name...',
                value='',
                style={'margin': 10, "width": "10%"}
            ),
            html.Label('Middle Name?'),
            dcc.Input(
                id='middle_name',
                placeholder='Enter middle name...',
                value='',
                style={'margin': 10, "width": "10%"}
            ),
            html.Label('Last Name?'),
            dcc.Input(
                id='last_name',
                placeholder='Enter last name...',
                value='',
                style={'margin': 10, "width": "10%"}
            ),
            html.Label('Initials?'),
            dcc.Input(
                id='initials',
                #placeholder='Enter initials...',
                value='',
                style={'margin': 10, "width": "3%"}
            ),
            html.Label('Role?'),
            dcc.Input(
                id='role',
                placeholder='Enter role...',
                value='',
                style={'margin': 10, "width": "10%"}
            ),
            html.Label('Department?'),
            dcc.Input(
                id='department',
                placeholder='Enter department...',
                value='',
                style={'margin': 10, "width": "10%"}
            ),
            html.Label('Reports to?'),
            dcc.Input(
                id='reports_to',
                # placeholder='Enter superior...',
                value='',
                style={'margin': 10, "width": "3%"}
            ),
            html.Button('Add Employee', id='btn', n_clicks=0),
            dash_table.DataTable(id='table', data=[], sort_by=[{'column_id': 'id', 'direction': 'desc'}],)

        ])])


    @app.callback(
        Output('table', 'data'), Output('table', 'columns'),
        [Input('btn', 'n_clicks')],
        [State('first_name', 'value'),
        State('last_name', 'value'),
         State('middle_name', 'value'),
        State('initials', 'value'),
         State('role', 'value'),
         State('department', 'value'),
         State('reports_to', 'value')],
    )
    def updateTable(n_clicks, first_name, middle_name, last_name, initials, role, department, reports_to):
        employees = Employee.query
        df = pd.read_sql(employees.statement, employees.session.bind).sort_values(by='id', ascending=False).head(10)
        if n_clicks > 0:
            drawing = Employee(first_name=first_name, middle_name=middle_name, last_name=last_name, initials=initials,
                               role=role, department=department, reports_to=reports_to)
            db.session.add(drawing)
            db.session.commit()
            flash('Your post has been created!', 'success')
            employees = Employee.query
            df = pd.read_sql(employees.statement, employees.session.bind).sort_values(by='id', ascending=False).head(10)
            return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]
        return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]



    return app.server