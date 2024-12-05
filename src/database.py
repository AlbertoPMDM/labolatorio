import sqlite3
from contextlib import closing
from collections.abc import Callable
import pandas as pd

class Database:
    
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
                            "uid"	INTEGER,
                            "nombre"	TEXT,
                            "cantidad"	INTEGER,
                            "laboratorio"	TEXT,
                            "lugar" TEXT,
                            "consumible"    TEXT
                        )
                        '''
                    )
        except sqlite3.IntegrityError:
            callback()

    def add_material(self, 
                     uid:int, 
                     nombre:str, 
                     cantidad:int, 
                     laboratorio:str = None, 
                     lugar:str = None, 
                     consumible:str = None, callback:Callable[..., None] = lambda _:None) -> None:
        '''
        añade un material a la tabla de materiales
        '''
        self.create_materials_table()
        # try:
        with closing(sqlite3.connect(self.db)) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(
                    '''
                    INSERT INTO "materiales" (
                    "uid",
                    "nombre",
                    "cantidad",
                    "laboratorio",
                    "lugar",
                    "consumible"
                    ) VALUES (?,?,?,?,?,?)
                    ''',(uid,nombre,cantidad,laboratorio,lugar,consumible)
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
                return pd.read_sql('SELECT * FROM materiales', conn)
        except:
            ...
                


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