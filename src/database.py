import sqlite3
from contextlib import closing
from collections.abc import Callable
import pandas as pd

class Database:

    # columnas para poder filtrar en dash, lo puse acá porque no se puede inferir el tipo de datos
    # y aqui viene eso definido para actualizarlo con cambios, no es necesario poner la columna de 
    # key porque no quiero que aparezca
    COLS_FOR_DASH = [
        {"name":"   uid", "id":"uid", "type":"numeric"},
        {"name":"activo", "id":"activo", "type":"numeric"},
        {"name":"nombre", "id":"nombre", "type":"text"},
        {"name":"marca", "id":"marca", "type":"text"},
        {"name":"cantidad", "id":"cantidad", "type":"numeric"},
        {"name":"laboratorio", "id":"laboratorio", "type":"text"},
        {"name":"lugar", "id":"lugar", "type":"text"},
        {"name":"consumible", "id":"consumible", "type":"text"},
        {"name":"funciona", "id":"funciona", "type":"text"}
    ]

    def __init__(self, path) -> None:
        self.db = path

    def create_materials_table(self, callback:Callable[..., None] = lambda _:None) -> None:
        '''
        crea la tabla de materiales
        '''
        try:
            with closing(sqlite3.connect(self.db)) as conn:
                with closing(conn.cursor()) as cur:
                    cur.execute(
                        '''
                        CREATE TABLE IF NOT EXISTS "materiales" (
                            "key" INTEGER,
                            "uid"	INTEGER UNIQUE,
                            "activo" INTEGER,
                            "nombre"	TEXT,
                            "marca"	TEXT,
                            "cantidad"	INTEGER,
                            "laboratorio"	TEXT,
                            "lugar" TEXT,
                            "consumible"    TEXT,
                            "funciona" TEXT,
                            PRIMARY KEY (key AUTOINCREMENT)
                        )
                        '''
                    )
        except sqlite3.IntegrityError:
            callback()

    def add_material(self, 
                     uid:int, 
                     activo:int,
                     nombre:str, 
                     marca:str,
                     cantidad:int, 
                     laboratorio:str = None, 
                     lugar:str = None, 
                     consumible:str = None, 
                     funciona:str = None,
                     callback:Callable[..., None] = lambda _:None) -> None:
        '''
        añade un material a la tabla de materiales, se quitó para manejar los errores para hacerlo desde la gui
        '''
        self.create_materials_table()
        # try:
        with closing(sqlite3.connect(self.db)) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(
                    '''
                    INSERT INTO "materiales" (
                    "uid",
                    activo,
                    "nombre",
                    "marca",
                    "cantidad",
                    "laboratorio",
                    "lugar",
                    "consumible",
                    "funciona"
                    ) VALUES (?,?,?,?,?,?,?,?,?)
                    ''',(uid, activo,nombre, marca,cantidad,laboratorio,lugar,consumible, funciona)
                )
            conn.commit()
        # except sqlite3.IntegrityError:
        #     callback()

    def all_materials(self) -> pd.DataFrame:
        '''
        regresa todos los materiales, utilizando pandas
        '''
        self.create_materials_table()
        try:
            with closing(sqlite3.connect(self.db)) as conn:
                return pd.read_sql('''SELECT * FROM materiales''', conn)
        except:
            ...

    def get_materials(self, key:int) -> pd.DataFrame:
        '''
        regresa todos los materiales, utilizando pandas
        se manejan las excepciones desde la gui
        ! hay que verificar que no se este ejecutando sql en un futuro
        '''
        self.create_materials_table()
        # try:
        with closing(sqlite3.connect(self.db)) as conn:
            return pd.read_sql(f'''SELECT "uid",
                "activo",
                "nombre",
                "marca",
                "cantidad",
                "laboratorio",
                "lugar",
                "consumible",
                "funciona" FROM materiales WHERE key LIKE {key}''', conn)
        # except:
        #     ...
    
    def set_materials(self, 
                     key:int, 
                     activo:int,
                     nombre:str, 
                     marca:str,
                     cantidad:int, 
                     laboratorio:str, 
                     lugar:str, 
                     consumible:str, 
                     funciona:str) -> None:
        '''
        regresa todos los materiales, utilizando pandas
        se manejan las excepciones desde la gui
        ! hay que verificar que no se este ejecutando sql en un futuro
        '''
        self.create_materials_table()
        # try:
        with closing(sqlite3.connect(self.db)) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(
                    '''
                    UPDATE materiales
                    SET (activo,nombre,marca,cantidad,laboratorio,lugar,consumible,funciona) =
	                    (VALUES(?, ?, ?, ?, ?, ?, ?, ?))
                    WHERE
                        key = ?
                    ''',(activo, nombre, marca, cantidad, laboratorio, lugar, consumible, funciona, key)
                )
            conn.commit()
        # except:
        #     ...
                
# def materials():
#     uid = input("uid:  ")
#     nombre = input("nombre: ")
#     cantidad = input("cantidad: ")
#     laboratorio = input("laboratorio: ")
#     lugar = input("lugar: ")
#     consumible = input("consumible: ")

#     db = Database("test.db")
#     db.create_materials_table()
#     db.add_material(uid, nombre, cantidad, laboratorio, lugar, consumible)

# materials()