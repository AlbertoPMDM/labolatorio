from dash import Dash, callback, Output, Input, no_update, State, ctx
import pandas as pd
from src.components import components
import dash_bootstrap_components as dbc
from src.database import Database
import time

db = Database("inventario.db")

app = Dash(external_stylesheets=[dbc.themes.FLATLY],suppress_callback_exceptions=True)

app.layout = components.layout

@callback(
    Output("form", "children"),
    Input("table_select", "value")
)
def update_form(value):
    return components.TABLES[value]

@callback(
    Output("materials_table", "data"),
    Output("materials_table", "columns"),
    Input("refresh_materials", "n_clicks")
)
def refresh_materials(n):
    return db.all_materials().to_dict("records"), Database.COLS_FOR_DASH

@callback(
    Output("material_add_message", "is_open"),
    Output("material_add_message", "children"),
    State("uid", "value"),
    State("activo", "value"),
    State("name", "value"),
    State("brand", "value"),
    State("qty", "value"),
    State("lab", "value"),
    State("place", "value"),
    State("cons", "value"),
    State("func", "value"),
    Input("submit_material", "n_clicks"),
    prevent_initial_call=True
)
def submit_material(uid, activo, name, brand, qty, lab, place, cons, func, n):
    if n==None:
        return False, ""
    else:
        try:
            print(uid, name, brand, qty, lab, place, cons, func)
            db.add_material(uid, activo, name, brand, qty, lab, place, cons, func)
            return True, "Se agregó correctamente"
        except Exception as e:
            return True, f"Hubo un error {e}"

@callback(
    Output("uid", "value"),
    Output("activo", "value"),
    Output("name", "value"),
    Output("brand", "value"),
    Output("qty", "value"),
    Output("lab", "value"),
    Output("place", "value"),
    Output("cons", "value"),
    Output("func", "value"),
    Input("clear_material", "n_clicks"),
    prevent_initial_call=True
)
def clear_material(n):
    if n == None:
        return no_update,no_update,no_update,no_update,no_update,no_update,no_update,no_update,no_update
    else:
        return None,None,None,None,None,None,None,None,None

@callback(
    Output("uid_e", "value"),
    Output("activo_e", "value"),
    Output("name_e", "value"),
    Output("brand_e", "value"),
    Output("qty_e", "value"),
    Output("lab_e", "value"),
    Output("place_e", "value"),
    Output("cons_e", "value"),
    Output("func_e", "value"),
    State('materials_table', 'data'),
    Input("clear_material_e", "n_clicks"),
    Input('materials_table', 'selected_rows'),
    prevent_initial_call=True
)
def mux_material_e(data,clear,selection):

    if clear != None:
        return None,None,None,None,None,None,None,None,None
    
    if selection != None:
        try:
            query = db.get_materials(data[selection[0]]["key"])
            print(query)
            return (
                query["uid"][0],
                query["activo"][0],
                query["nombre"][0],
                query["marca"][0],
                query["cantidad"][0],
                query["laboratorio"][0],
                query["lugar"][0],
                query["consumible"][0],
                query["funciona"][0]
            )
        except Exception as e:
            print(e)

@callback(
    Output("material_add_message_e", "is_open"),
    Output("material_add_message_e", "children"),
    Output("materials_table", "filtering_settings"),
    State("uid_e", "value"),
    State("activo_e", "value"),
    State("name_e", "value"),
    State("brand_e", "value"),
    State("qty_e", "value"),
    State("lab_e", "value"),
    State("place_e", "value"),
    State("cons_e", "value"),
    State("func_e", "value"),
    State('materials_table', 'data'),
    State('materials_table', 'selected_rows'),
    Input("edit_material", "n_clicks"),
    prevent_initial_call=True
)
def submit_material_e(uid, activo, name, brand, qty, lab, place, cons, func, data, selection, n):
    if n==None:
        return False, "", ""
    else:
        try:
            print("cambio", uid, name, brand, qty, lab, place, cons, func)
            db.set_materials(data[selection[0]]["key"], activo, name, brand, qty, lab, place, cons, func)
            return True, "Se guardó correctamente", ""
        except Exception as e:
            return True, f"Hubo un error {e}", ""

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)