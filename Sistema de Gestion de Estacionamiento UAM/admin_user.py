import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
from common_user import CommonUserUI

class AdminUserUI(CommonUserUI):
    def draw(self):
        self.clear()
        ttk.Label(self.frame, text=f"Administrador: {self.username}").pack(pady=5)
        ttk.Button(self.frame, text="Agregar Espacios", command=self.add_spaces).pack(pady=2)
        ttk.Button(self.frame, text="Eliminar Espacios", command=self.remove_spaces).pack(pady=2)
        ttk.Button(self.frame, text="Ocupar Espacio", command=lambda: self._show_admin_grid('occupy')).pack(pady=2)
        ttk.Button(self.frame, text="Liberar Espacio", command=lambda: self._show_admin_grid('release')).pack(pady=2)
        ttk.Button(self.frame, text="Ver Disponibilidad", command=lambda: self._show_admin_grid('readonly')).pack(pady=2)
        ttk.Button(self.frame, text="Cerrar Sesión", command=self.root.quit).pack(pady=5).pack(pady=5)

    def add_spaces(self):
        sec = simpledialog.askstring("Agregar","Sección (A/B/C):")
        if not sec: return
        sec = sec.upper()
        n = simpledialog.askinteger("Agregar","# espacios a agregar:",minvalue=1,maxvalue=20)
        if not n: return
        current = len(self.system.parking[sec])
        for i in range(current+1, current+n+1):
            self.system.parking[sec][f"{sec}{i}"] = 'disponible'
        self.system.save_all()
        messagebox.showinfo("Éxito","Espacios agregados")
        self.draw()

    def remove_spaces(self):
        sec = simpledialog.askstring("Eliminar","Sección (A/B/C):")
        if not sec: return
        sec = sec.upper()
        n = simpledialog.askinteger("Eliminar","# espacios a eliminar:",minvalue=1,maxvalue=20)
        if not n: return
        total = len(self.system.parking[sec])
        for i in range(total, total-n, -1):
            self.system.parking[sec].pop(f"{sec}{i}", None)
        self.system.save_all()
        messagebox.showinfo("Éxito","Espacios eliminados")
        self.draw()

    def _show_admin_grid(self, action):
        self.clear()
        sections = ['A','B','C']
        for sec in sections:
            ttk.Button(self.frame, text=f"Sección {sec}", command=lambda s=sec: self._admin_grid(s, action)).pack(pady=2)
        ttk.Button(self.frame, text="Volver", command=self.draw).pack(pady=5)

    def _admin_grid(self, section, action):
        self.clear()
        ttk.Label(self.frame, text=f"Parqueo {section} (Admin)").grid(row=0,column=0,columnspan=10,pady=5)
        spots = sorted(self.system.parking[section].keys(), key=lambda x:int(x[1:]))
        style = ttk.Style(self.root)
        style.configure('Green.TButton', background='green')
        style.configure('Red.TButton', background='red')
        for idx, spot in enumerate(spots):
            r,c = divmod(idx,10)
            state = self.system.parking[section][spot]
            btn = ttk.Button(self.frame, text=spot, width=4)
            if state == 'disponible':
                btn.config(style='Green.TButton')
                if action=='occupy': btn.config(command=lambda s=spot, sec=section: self._do_occupy_admin(sec, s))
            else:
                btn.config(style='Red.TButton')
                if action=='release': btn.config(command=lambda s=spot, sec=section: self._do_release_admin(sec, s))
            btn.grid(row=r+1, column=c, padx=2, pady=2)
        back_row = len(spots)//10 + 2
        ttk.Button(self.frame, text="Volver", command=self.draw).grid(row=back_row, column=0, columnspan=10, pady=10)

    def _do_occupy_admin(self, section, spot):
        now = datetime.now().isoformat()
        self.system.parking[section][spot] = {'status':'ocupado','user':self.username,'entry':now}
        self.system.history.append({'user':self.username,'spot':spot,'entry':now,'exit':None})
        self.system.save_all()
        messagebox.showinfo("Éxito",f"{spot} ocupado por admin")
        self.draw()

    def _do_release_admin(self, section, spot):
        now = datetime.now().isoformat()
        self.system.parking[section][spot] = 'disponible'
        for rec in reversed(self.system.history):
            if rec['spot']==spot and rec['exit'] is None:
                rec['exit']=now
                break
        self.system.save_all()
        messagebox.showinfo("Éxito",f"{spot} liberado por admin")
        self.draw()
