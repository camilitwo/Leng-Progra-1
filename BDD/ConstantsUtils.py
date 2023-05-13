class ConstantesUtils:
    def __init__(self):
        self.TABLA = "alumno"
        self.CAMPOS = "id, nombre, apellido, edad"
        self.CAMPOS_INSERT = "nombre, apellido, edad"
        self.CAMPOS_INSERT_VALORES = "?, ?, ?"
        self.CAMPOS_UPDATE = "nombre=?, apellido=?, edad=?"
        self.CAMPOS_UPDATE_WHERE = "id=?"
        self.DRIVER_ACCESS = "Microsoft Access Driver (*.mdb, *.accdb)"
        self.RUTA_ACCESS = "c:/datos/udp.accdb"


    def getTabla(self):
        return self.TABLA

    def getCampos(self):
        return self.CAMPOS

    def getCamposInsert(self):
        return self.CAMPOS_INSERT

    def getCamposInsertValores(self):
        return self.CAMPOS_INSERT_VALORES

    def getCamposUpdate(self):
        return self.CAMPOS_UPDATE

    def getCamposUpdateWhere(self):
        return self.CAMPOS_UPDATE_WHERE