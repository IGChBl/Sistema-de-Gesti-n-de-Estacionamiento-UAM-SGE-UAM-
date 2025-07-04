from datetime import datetime
from file_manager import cargar_parqueos, guardar_parqueos, cargar_usuarios, guardar_usuarios, cargar_historial, guardar_historial

class ParkingSystem:
    def __init__(self):
        self.fecha = datetime.now().strftime('%Y-%m-%d')
        self.parking = cargar_parqueos(self.fecha)
        self.users = cargar_usuarios()
        self.history = cargar_historial()

    def save_all(self):
        guardar_parqueos(self.parking, self.fecha)
        guardar_usuarios(self.users)
        guardar_historial(self.history)

    def register_user(self, username, info):
        self.users[username] = info
        self.save_all()

    def verify_user(self, username, password):
        return username in self.users and self.users[username]['password'] == password

    def occupy_space(self, username, section, spot):
        # Usuarios comunes pueden ocupar solo si no tienen espacio previo
        for sec, spots in self.parking.items():
            for sp, val in spots.items():
                if isinstance(val, dict) and val.get('user') == username:
                    return False
        if self.parking[section][spot] != 'disponible':
            return False
        now = datetime.now().isoformat()
        self.parking[section][spot] = {'status':'ocupado','user':username,'entry':now}
        self.history.append({'user':username,'spot':spot,'entry':now,'exit':None})
        self.save_all()
        return True

    def release_space(self, username, section, spot):
        data = self.parking[section][spot]
        if not isinstance(data, dict) or data.get('user') != username:
            return False
        now = datetime.now().isoformat()
        self.parking[section][spot] = 'disponible'
        for rec in reversed(self.history):
            if rec['spot'] == spot and rec['exit'] is None:
                rec['exit'] = now
                break
        self.save_all()
        return True

    def available_spots(self):
        return {sec: [s for s,v in spots.items() if v=='disponible']
                for sec,spots in self.parking.items()}

    def get_history(self):
        return self.history