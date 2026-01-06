# --- 1. MODELO CLIENTE ---
class Cliente:
    def __init__(self, id, nombre, ruc, telefono):
        self.datos = {
            'id': int(id),
            'nombre': nombre,
            'ruc': ruc,
            'telefono': telefono
        }

    def to_line(self):
        # Formato: id|nombre|ruc|telefono
        return f"{self.datos['id']}|{self.datos['nombre']}|{self.datos['ruc']}|{self.datos['telefono']}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split('|')
        return Cliente(parts[0], parts[1], parts[2], parts[3])

    def __getitem__(self, key):
        return self.datos[key]

# --- 2. MODELO EMPLEADO ---
class Empleado:
    def __init__(self, id, nombre, cargo):
        self.datos = {
            'id': int(id),
            'nombre': nombre,
            'cargo': cargo
        }

    def to_line(self):
        return f"{self.datos['id']}|{self.datos['nombre']}|{self.datos['cargo']}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split('|')
        return Empleado(parts[0], parts[1], parts[2])

    def __getitem__(self, key):
        return self.datos[key]

# --- 3. MODELO SERVICIO (SPA) ---
class Servicio:
    def __init__(self, id, nombre, precio, duracion):
        self.datos = {
            'id': int(id),
            'nombre': nombre,
            'precio': float(precio),
            'duracion': duracion  # ej: "60 min"
        }

    def to_line(self):
        return f"{self.datos['id']}|{self.datos['nombre']}|{self.datos['precio']}|{self.datos['duracion']}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split('|')
        return Servicio(parts[0], parts[1], parts[2], parts[3])

    def __getitem__(self, key):
        return self.datos[key]

# --- 4. MODELO CITA (CABECERA) ---
class Cita:
    def __init__(self, id, id_cliente, id_empleado, fecha, hora, total, estado):
        self.datos = {
            'id': int(id),
            'id_cliente': int(id_cliente),
            'id_empleado': int(id_empleado),
            'fecha': fecha,
            'hora': hora,
            'total': float(total),
            'estado': estado
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['id_cliente']}|{d['id_empleado']}|{d['fecha']}|{d['hora']}|{d['total']}|{d['estado']}"

    @staticmethod
    def from_line(line):
        p = line.strip().split('|')
        return Cita(p[0], p[1], p[2], p[3], p[4], p[5], p[6])

# --- 5. MODELO DETALLE_CITA ---
class DetalleCita:
    def __init__(self, id_cita, id_servicio, precio_cobrado):
        self.datos = {
            'id_cita': int(id_cita),
            'id_servicio': int(id_servicio),
            'precio_cobrado': float(precio_cobrado)
        }

    def to_line(self):
        return f"{self.datos['id_cita']}|{self.datos['id_servicio']}|{self.datos['precio_cobrado']}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split('|')
        return DetalleCita(parts[0], parts[1], parts[2])

    def __getitem__(self, key):
        return self.datos[key]

# --- 6. MODELO PAGO ---
class Pago:
    def __init__(self, id, id_cita, monto, metodo, fecha):
        self.datos = {
            'id': int(id),
            'id_cita': int(id_cita),
            'monto': float(monto),
            'metodo': metodo, # Efectivo, Tarjeta, Transferencia
            'fecha': fecha
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['id_cita']}|{d['monto']}|{d['metodo']}|{d['fecha']}"

    @staticmethod
    def from_line(line):
        p = line.strip().split('|')
        return Pago(p[0], p[1], p[2], p[3], p[4])