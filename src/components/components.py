from dash import  html, dash_table
import dash_bootstrap_components as dbc

# Estilo para todos los campos a llenar
INPUT_STYLE = {"font-size": "inherit"}

SALONES = [
    "almacen",
    "lab fisica i",
    "lab fisica ii",
    "lab fisica iii",
    "lab termo",
    "lab optica"
]
########################## AGREGAR ########################

# Entrada para el uid
uid_input = dbc.Input(
    id="uid",
    type="number",
    placeholder="uid",
    style=INPUT_STYLE
)

# Entrada para el activo
activo_input = dbc.Input(
    id="activo",
    type="number",
    placeholder="activo",
    style=INPUT_STYLE
)

# Entrada para el nombre
name_input = dbc.Input(
    id="name",
    type="text",
    placeholder="nombre",
    style=INPUT_STYLE
)

# Entrada para la marca
brand_input = dbc.Input(
    id="brand",
    type="text",
    placeholder="marca",
    style=INPUT_STYLE
)

# Entrada para la cantidad
qty_input = dbc.Input(
    id="qty",
    type="number",
    placeholder="cantidad",
    style=INPUT_STYLE
)

# Entrada para el lab
lab_input = dbc.Select(
    SALONES,
    'almacen', 
    id='lab',
    style=INPUT_STYLE
)


# Entrada para el lugar
place_input = dbc.Input(
    id="place",
    type="text",
    placeholder="lugar dentro del laboratorio o salón",
    style=INPUT_STYLE
)

# Entrada para si es consumible o no
cons_input = html.Div([
    "Consumible?",
    dbc.RadioItems(
    ["si", "no"],
    "no",
    inline=True,
    style=INPUT_STYLE,
    id="cons"
)
])

# Entrada para si es funciona o no
func_input = html.Div([
    "Funciona?",
    dbc.RadioItems(
    ["si", "no"],
    "no",
    inline=True,
    style=INPUT_STYLE,
    id="func"
)
])

# Botón para submitir materiales
submit_material = html.Button(
    id="submit_material",
    children="añadir",
    style=INPUT_STYLE
)

# Botón para limpiar materiales
clear_material = html.Button(
    id="clear_material",
    children="limpiar",
    style=INPUT_STYLE
)

# Menú para la sección de materiales
materials_menu = dbc.Stack([
    uid_input,
    activo_input,
    name_input,
    brand_input,
    qty_input,
    "laboratorio",
    lab_input,
    place_input,
    cons_input,
    func_input,
    submit_material,
    clear_material
], gap=3)

# Mensaje que sale al añadir un material
material_add_message = dbc.Modal(
    [
    dbc.ModalBody("Se añadió correctamente")
    ],
    id="material_add_message",
    is_open=False,
)

################################### Editar ############################################

# Entrada para el uid
uid_input_e = dbc.Input(
    id="uid_e",
    type="number",
    placeholder="uid",
    style=INPUT_STYLE
)

# Entrada para el activo
activo_input_e = dbc.Input(
    id="activo_e",
    type="number",
    placeholder="activo",
    style=INPUT_STYLE
)

# Entrada para el nombre
name_input_e = dbc.Input(
    id="name_e",
    type="text",
    placeholder="nombre",
    style=INPUT_STYLE
)

# Entrada para la marca
brand_input_e = dbc.Input(
    id="brand_e",
    type="text",
    placeholder="marca",
    style=INPUT_STYLE
)

# Entrada para la cantidad
qty_input_e = dbc.Input(
    id="qty_e",
    type="number",
    placeholder="cantidad",
    style=INPUT_STYLE
)

# Entrada para el lab
lab_input_e = dbc.Select(
    SALONES,
    'almacen', 
    id='lab_e',
    style=INPUT_STYLE
)

# Entrada para el lugar
place_input_e = dbc.Input(
    id="place_e",
    type="text",
    placeholder="lugar dentro del laboratorio o salón",
    style=INPUT_STYLE
)

# Entrada para si es consumible o no
cons_input_e = html.Div([
    "Consumible?",
    dbc.RadioItems(
    ["si", "no"],
    "no",
    inline=True,
    style=INPUT_STYLE,
    id="cons_e"
)
])

# Entrada para si es funciona o no
func_input_e = html.Div([
    "Funciona?",
    dbc.RadioItems(
    ["si", "no"],
    "no",
    inline=True,
    style=INPUT_STYLE,
    id="func_e"
)

])
# Botón para limpiar materiales
clear_material_e = html.Button(
    id="clear_material_e",
    children="limpiar",
    style=INPUT_STYLE
)

# Botón para editar materiales
edit_material = html.Button(
    id="edit_material",
    children="guardar",
    style=INPUT_STYLE
)

# Botón para buscar materiales en la pagina de editar
search_material_e = html.Button(
    id="search_material_e",
    children="buscar uid",
    style=INPUT_STYLE
)

# Menú para editar un material
edit_materials_menu = dbc.Stack([
    uid_input_e,
    activo_input_e,
    name_input_e,
    brand_input_e,
    qty_input_e,
    "laboratorio",
    lab_input_e,
    place_input_e,
    cons_input_e,
    func_input_e,
    search_material_e,
    edit_material,
    clear_material_e
], gap=3)

# mensaje que sale al editar un material
material_add_message_e = dbc.Modal(
    [
    dbc.ModalBody("Se añadió correctamente")
    ],
    id="material_add_message_e",
    is_open=False,
)

############################ vista de tabla de materiales ######################

# Botón para recargar la tabla de materiales
refresh_materials = html.Button(
    id="refresh_materials",
    children="recargar",
    style=INPUT_STYLE
)

# Tabla de los materiales
materials_table = dash_table.DataTable(
    [],
    id="materials_table"
)

# Tabla de materiales pero con botón para recargarla
materials_table_view = dbc.Stack([
    refresh_materials,
    materials_table
])

############################ misc ########################################

# Selector de tabla, debe tener un elemento para cada valor, asociado en la variable TABLES
table_select = dbc.Select(
    ["Agregar Material", "Materiales", "Buscar y Editar Material"],
    'Agregar Material', 
    id='table_select',
    style=INPUT_STYLE
)

# Espacio para la forma a llenar
form = html.Div(
    id="form",
    children=materials_menu,
)

# Arreglo general
layout = html.Div([
    table_select,
    form,
    material_add_message,
    material_add_message_e
], style={"height":"100vh", "width":"100vw", "font-size": "100%"})

# Diccionario para elegir las formas, debe tener una entrada correspondiente en table_select
TABLES = {
    "Agregar Material":materials_menu,
    "Materiales":materials_table_view,
    "Buscar y Editar Material":edit_materials_menu
}