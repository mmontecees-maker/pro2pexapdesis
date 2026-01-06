import os

# --- CLASE BASE PARA EVITAR REPETIR CÓDIGO ---
class FileManagerBase:
    def __init__(self, filename, counter_file):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w", encoding="utf-8") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r", encoding="utf-8") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w", encoding="utf-8") as f:
            f.write(str(new_id))
        return new_id

    def _write_file(self, items):
        with open(self.filename, "w", encoding="utf-8") as f:
            for item in items.values():
                f.write(item.to_line() + "\n")

# --- 1. GESTIÓN DE CLIENTES ---
class FileManagerCliente(FileManagerBase):
    def __init__(self):
        super().__init__("data/clientes.txt", "data/cont_clientes.txt")

    def _read_file(self):
        from models import Cliente
        clientes = {}
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    obj = Cliente.from_line(line)
                    clientes[obj['id']] = obj
        return clientes

    def get_all(self):
        return [c.datos for c in self._read_file().values()]

    def insert(self, nombre, ruc, telefono):
        from models import Cliente
        new_id = self._get_next_id()
        c = Cliente(new_id, nombre, ruc, telefono)
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(c.to_line() + "\n")
        return c.datos

    def update(self, id_entidad, nombre, ruc, telefono):
        items = self._read_file()
        if id_entidad in items:
            from models import Cliente
            items[id_entidad] = Cliente(id_entidad, nombre, ruc, telefono)
            self._write_file(items)
            return True
        return False

    def delete(self, id_entidad):
        items = self._read_file()
        if id_entidad in items:
            del items[id_entidad]
            self._write_file(items)
            return True
        return False

# --- 2. GESTIÓN DE EMPLEADOS ---
class FileManagerEmpleado(FileManagerBase):
    def __init__(self):
        super().__init__("data/empleados.txt", "data/cont_empleados.txt")

    def _read_file(self):
        from models import Empleado
        empleados = {}
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    obj = Empleado.from_line(line)
                    empleados[obj['id']] = obj
        return empleados

    def get_all(self):
        return [e.datos for e in self._read_file().values()]

    def insert(self, nombre, cargo):
        from models import Empleado
        new_id = self._get_next_id()
        e = Empleado(new_id, nombre, cargo)
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(e.to_line() + "\n")
        return e.datos

    def update(self, id_entidad, nombre, cargo):
        items = self._read_file()
        if id_entidad in items:
            from models import Empleado
            items[id_entidad] = Empleado(id_entidad, nombre, cargo)
            self._write_file(items)
            return True
        return False

# --- 3. GESTIÓN DE SERVICIOS ---
class FileManagerServicio(FileManagerBase):
    def __init__(self):
        super().__init__("data/servicios.txt", "data/cont_servicios.txt")

    def _read_file(self):
        from models import Servicio
        servicios = {}
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    obj = Servicio.from_line(line)
                    servicios[obj['id']] = obj
        return servicios

    def get_all(self):
        return [s.datos for s in self._read_file().values()]

    def insert(self, nombre, precio, duracion):
        from models import Servicio
        new_id = self._get_next_id()
        s = Servicio(new_id, nombre, precio, duracion)
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(s.to_line() + "\n")
        return s.datos

# --- 4. GESTIÓN DE CITAS Y DETALLES ---
class FileManagerCita(FileManagerBase):
    def __init__(self):
        self.d_file = "data/detalle_citas.txt"
        super().__init__("data/citas.txt", "data/cont_citas.txt")
        if not os.path.exists(self.d_file):
            with open(self.d_file, "w", encoding="utf-8") as f: f.write("")

    def registrar_cita(self, id_cliente, id_empleado, fecha, hora, lista_servicios):
        from models import Cita, DetalleCita
        id_cita = self._get_next_id()
        total = sum(float(s['precio']) for s in lista_servicios)
        
        cita = Cita(id_cita, id_cliente, id_empleado, fecha, hora, total, "Programada")
        
        # Guardar cabecera
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(cita.to_line() + "\n")
            
        # Guardar detalles
        with open(self.d_file, "a", encoding="utf-8") as f:
            for s in lista_servicios:
                det = DetalleCita(id_cita, s['id'], s['precio'])
                f.write(det.to_line() + "\n")
        
        return cita.datos

    def get_all_citas(self):
        from models import Cita
        citas = []
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    citas.append(Cita.from_line(line).datos)
        return citas

# --- 5. GESTIÓN DE PAGOS ---
class FileManagerPago(FileManagerBase):
    def __init__(self):
        super().__init__("data/pagos.txt", "data/cont_pagos.txt")

    def registrar_pago(self, id_cita, monto, metodo, fecha):
        from models import Pago
        new_id = self._get_next_id()
        pago = Pago(new_id, id_cita, monto, metodo, fecha)
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(pago.to_line() + "\n")
        return pago.datos

    def get_all(self):
        from models import Pago
        pagos = []
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    pagos.append(Pago.from_line(line).datos)
        return pagos