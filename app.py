from dash import Dash, callback, Output, Input, no_update, State
import pandas as pd
from src.components import components
import dash_bootstrap_components as dbc
from src.database import Database

db = Database("test.db")

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)

app.layout = components.layout

@callback(
    Output("form", "children"),
    Input("table_select", "value")
)
def update_form(value):
    return components.TABLES[value]

@callback(
    Output("materials_table", "data"),
    Input("refresh_materials", "n_clicks")
)
def refresh_materials(n):
    return db.all_materials().to_dict("records")

@callback(
    Output("material_add_message", "is_open"),
    Output("material_add_message", "children"),
    State("uid", "value"),
    State("name", "value"),
    State("qty", "value"),
    State("lab", "value"),
    State("place", "value"),
    State("cons", "value"),
    Input("submit_material", "n_clicks"),
    prevent_initial_call=True
)
def submit_material(uid, name, qty, lab, place, cons, n):
    if n==None:
        return False, ""
    else:
        try:
            print(uid, name, qty, lab, place, cons)
            db.add_material(uid, name, qty, lab, place, cons)
            return True, "Se agregó correctamente"
        except Exception as e:
            return True, f"Hubo un error {e}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)