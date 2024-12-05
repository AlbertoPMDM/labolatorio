from dash import  html, dash_table
import dash_bootstrap_components as dbc

input_style = {"font-size": "inherit"}

# Entrada para el uid
uid_input = dbc.Input(
    id="uid",
    type="number",
    placeholder="uid",
    style=input_style
)

# Entrada para el nombre
name_input = dbc.Input(
    id="name",
    type="text",
    placeholder="nombre",
    style=input_style
)

# Entrada para la cantidad
qty_input = dbc.Input(
    id="qty",
    type="number",
    placeholder="cantidad",
    style=input_style
)

# Entrada para el lab
lab_input = dbc.Input(
    id="lab",
    type="text",
    placeholder="laboratorio o salón",
    style=input_style
)

# Entrada para el lugar
place_input = dbc.Input(
    id="place",
    type="text",
    placeholder="mueble o lugar",
    style=input_style
)

# Entrada para si es consumible o no
cons_input = html.Div([
    "Consumible?",
    dbc.RadioItems(
    ["sí", "no"],
    "no",
    inline=True,
    style=input_style,
    id="cons"
)
])

# Selector de tabla
table_select = dbc.Select(
    ["Agregar Material", "Materiales"],
    'Agregar Material', 
    id='table_select',
    style=input_style
)

# Botón para submitir
submit_material = html.Button(
    id="submit_material",
    children="añadir",
    style=input_style
)

# Botón para recargar la tabla
refresh_materials = html.Button(
    id="refresh_materials",
    children="recargar",
    style=input_style
)

# Menú para la sección de materiales
materials_menu = dbc.Stack([
    uid_input,
    name_input,
    qty_input,
    lab_input,
    place_input,
    cons_input,
    submit_material
], gap=3)

materials_table = dash_table.DataTable(
    [],
    id="materials_table"
)


materials_table_view = dbc.Stack([
    refresh_materials,
    materials_table
])


# Espacio para la forma a llenar
form = html.Div(
    id="form",
    children=materials_menu,
)

material_add_message = dbc.Modal(
    [
    dbc.ModalBody("Se añadió correctamente")
    ],
    id="material_add_message",
    is_open=False,
)

# Arreglo general
layout = html.Div([
    table_select,
    form,
    material_add_message
], style={"height":"100vh", "width":"100vw", "font-size": "100%"})

# Diccionario para elegir las formas
TABLES = {
    "Agregar Material":materials_menu,
    "Materiales":materials_table_view
}