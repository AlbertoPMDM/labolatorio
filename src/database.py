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
                            "uid"	INTEGER UNIQUE,
                            "activo" INTEGER,
                            "nombre"	TEXT,
                            "marca"	TEXT,
                            "cantidad"	INTEGER,
                            "laboratorio"	TEXT,
                            "lugar" TEXT,
                            "consumible"    TEXT,
                            "funciona" TEXT
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
                return pd.read_sql('SELECT * FROM materiales', conn)
        except:
            ...

    def get_materials(self, uid:int) -> pd.DataFrame:
        '''
        regresa todos los materiales, utilizando pandas
        se manejan las excepciones desde la gui
        ! hay que verificar que no se este ejecutando sql en un futuro
        '''
        self.create_materials_table()
        # try:
        with closing(sqlite3.connect(self.db)) as conn:
            return pd.read_sql(f'SELECT * FROM materiales WHERE uid LIKE {uid}', conn)
        # except:
        #     ...
    
    def set_materials(self, 
                     uid:int, 
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
                        uid = ?
                    ''',(activo, nombre, marca, cantidad, laboratorio, lugar, consumible, funciona, uid)
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