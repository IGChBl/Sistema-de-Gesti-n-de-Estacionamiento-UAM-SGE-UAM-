import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from parking_system import ParkingSystem

class CommonUserUI:
    def __init__(self, root, system, username):
        self.root = root
        self.system = system
        self.username = username
        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(fill='both', expand=True)
        self.draw()

    def clear(self):
        for w in self.frame.winfo_children(): w.destroy()

    def draw(self):
        self.clear()
        ttk.Label(self.frame, text=f"Usuario: {self.username}").pack(pady=5)
        ttk.Button(self.frame, text="Ocupar Espacio", command=self.show_section_menu).pack(pady=2)
        ttk.Button(self.frame, text="Liberar Espacio", command=self.show_release_menu).pack(pady=2)
        ttk.Button(self.frame, text="Ver Disponibilidad", command=self.show_view_menu).pack(pady=2)
        ttk.Button(self.frame, text="Historial", command=self.show_history).pack(pady=2)
        ttk.Button(self.frame, text="Cerrar Sesión", command=self.root.quit).pack(pady=5)

    def show_section_menu(self):
        self.clear()
        ttk.Label(self.frame, text="Selecciona Sección para Ocupar").pack(pady=5)
        for sec in ['A','B','C']:
            ttk.Button(self.frame, text=f"Sección {sec}", command=lambda s=sec: self._show_grid(s,'occupy')).pack(pady=2)
        ttk.Button(self.frame, text="Volver", command=self.draw).pack(pady=5)

    def show_release_menu(self):
        self.clear()
        ttk.Label(self.frame, text="Selecciona Sección para Liberar").pack(pady=5)
        for sec in ['A','B','C']:
            ttk.Button(self.frame, text=f"Sección {sec}", command=lambda s=sec: self._show_grid(s,'release')).pack(pady=2)
        ttk.Button(self.frame, text="Volver", command=self.draw).pack(pady=5)

    def show_view_menu(self):
        self.clear()
        ttk.Label(self.frame, text="Selecciona Sección para Ver Disponibilidad").pack(pady=5)
        for sec in ['A','B','C']:
            ttk.Button(self.frame, text=f"Sección {sec}", command=lambda s=sec: self._show_grid(s,'readonly')).pack(pady=2)
        ttk.Button(self.frame, text="Volver", command=self.draw).pack(pady=5)

    def _show_grid(self, section, action):
        self.clear()
        ttk.Label(self.frame, text=f"Parqueo {section}").grid(row=0,column=0,columnspan=10,pady=5)
        spots = sorted(self.system.parking[section].keys(), key=lambda x:int(x[1:]))
        style = ttk.Style(self.root)
        style.configure('Green.TButton', background='green')
        style.configure('Red.TButton', background='red')
        for idx, spot in enumerate(spots):
            r,c = divmod(idx, 10)
            btn = ttk.Button(self.frame, text=spot, width=4)
            state = self.system.parking[section][spot]
            btn.config(style='Green.TButton' if state=='disponible' else 'Red.TButton')
            if action=='occupy' and state=='disponible': btn.config(command=lambda s=spot: self._do_occupy(section,s))
            elif action=='release' and isinstance(state,dict) and state.get('user')==self.username: btn.config(command=lambda s=spot: self._do_release(section,s))
            else: btn.state(['disabled'])
            btn.grid(row=r+1, column=c, padx=2, pady=2)
        back_row = len(spots)//10 + 2
        ttk.Button(self.frame, text="Volver", command=self.draw).grid(row=back_row,column=0,columnspan=10,pady=10)

    def _do_occupy(self, section, spot):
        if self.system.occupy_space(self.username, section, spot): messagebox.showinfo("Éxito",f"{spot} ocupado")
        else: messagebox.showerror("Error","Debe liberar antes o espacio no disponible")
        self.draw()

    def _do_release(self, section, spot):
        if self.system.release_space(self.username, section, spot): messagebox.showinfo("Éxito",f"{spot} liberado")
        else: messagebox.showerror("Error","No es tu espacio o ya libre")
        self.draw()

    def show_history(self):
        self.clear()
        ttk.Label(self.frame, text="Historial").pack(pady=5)
        for rec in self.system.get_history():
            ttk.Label(self.frame, text=f"{rec['user']} - {rec['spot']} - Entrada: {rec['entry']} - Salida: {rec.get('exit','-')}\n").pack()
        ttk.Button(self.frame, text="Volver", command=self.draw).pack(pady=10)