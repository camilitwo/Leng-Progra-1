import pyodbc
import ConstantsUtils as ConstantesUtils

class Conexion:
    def __init__(self):
        self.conn = None
        try:
            driver = ConstantesUtils().DRIVER_ACCESS
            ruta = ConstantesUtils().RUTA_ACCESS
            self.conn = pyodbc.connect("Driver={%s};DBQ=%s;" % (driver, ruta))
            print("Conectado")
        except Exception as e:
            print(e)
    def abrirConexion(self):
        return self.conn
    def ejecutar(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            print("Ejecutado")
        except Exception as e:
            print(e)
    def consultar(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    def buscarUno(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchone()
    def cerrar(self):
        self.conn.cursor().close()
        self.conexion.close()
