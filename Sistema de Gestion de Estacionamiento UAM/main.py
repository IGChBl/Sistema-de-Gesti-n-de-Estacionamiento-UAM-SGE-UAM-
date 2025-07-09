import tkinter as tk    # Importa tkinter para crear la interfaz gráfica
from tkinter import ttk, messagebox, simpledialog   # Importa ttk para widgets mejorados, messagebox para diálogos y simpledialog para entradas de texto
from parking_system import ParkingSystem    # Importa la clase ParkingSystem que maneja la lógica del sistema de parqueo
from common_user import CommonUserUI    # Importa la clase CommonUserUI que maneja la interfaz de usuario común
from admin_user import AdminUserUI  # Importa la clase AdminUserUI que maneja la interfaz de usuario administrador

class MainApp:  # Clase principal que inicia la aplicación
    def __init__(self): # Inicializa la aplicación creando una instancia del sistema de parqueo y configurando la ventana principal
        self.sys = ParkingSystem()
        self.root = tk.Tk()
        self.root.title("SGE UAM")
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(fill='both', expand=True)
        self.show_main_menu()
        self.root.mainloop()

    def clear(self):    # Limpia el contenido del frame actual
        for w in self.frame.winfo_children():
            w.destroy()

    def show_main_menu(self):   # Muestra el menú principal de la aplicación
        self.clear()
        ttk.Label(self.frame, text="Sistema de Gestión de Estacionamiento UAM").pack(pady=5)
        ttk.Button(self.frame, text="Registrarse", command=self.show_register).pack(pady=2)
        ttk.Button(self.frame, text="Iniciar Sesión", command=self.show_login).pack(pady=2)
        ttk.Button(self.frame, text="Salir", command=self.root.quit).pack(pady=5)

    def show_register(self):    # Muestra el formulario de registro de usuario
        self.clear()
        ttk.Label(self.frame, text="Registrar Usuario").pack(pady=5)
        entries = {}
        fields = [
            ("Nombre", "name"),
            ("Apellido", "surname"),
            ("CIF", "cif"),
            ("Usuario", "username"),
            ("Contraseña", "password"),
            ("Rol", "role")
        ]
        for lbl, key in fields:
            ttk.Label(self.frame, text=f"{lbl}:").pack(pady=(5, 0))
            if key == 'role':
                var = tk.StringVar(value="estudiante")
                ttk.OptionMenu(
                    self.frame, var,
                    "estudiante", "estudiante", "docente", "administrativo", "administrador"
                ).pack(pady=(0, 5))
            else:
                var = tk.StringVar()
                show = '*' if key == 'password' else None
                ttk.Entry(self.frame, textvariable=var, show=show).pack(pady=(0, 5))
            entries[key] = var

        def do_register():  # Función que se ejecuta al hacer clic en el botón de guardar
            data = {k: entries[k].get().strip() for _, k in fields}
            # Validaciones
            if any(not data[k] for _, k in fields):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            if len(data['cif']) != 8 or not data['cif'].isdigit():
                messagebox.showerror("Error", "El CIF debe tener 8 dígitos numéricos")
                return
            if data['username'] in self.sys.users:
                messagebox.showerror("Error", "El usuario ya existe")
                return
            # Clave admin si rol administrador
            if data['role'] == 'administrador':
                key = simpledialog.askstring(
                    "Clave Admin", "Ingrese la clave de administrador:", show='*'
                )
                if key != 'ADMIN2025':
                    messagebox.showerror("Error", "Clave de administrador incorrecta")
                    return
            # Registrar y volver
            self.sys.register_user(data['username'], data)
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")
            self.show_main_menu()

        ttk.Button(self.frame, text="Guardar", command=do_register).pack(pady=10)
        ttk.Button(self.frame, text="Volver", command=self.show_main_menu).pack()

    def show_login(self):   # Muestra el formulario de inicio de sesión
        self.clear()
        ttk.Label(self.frame, text="Iniciar Sesión").pack(pady=5)
        ttk.Label(self.frame, text="Usuario:").pack()
        user_var = tk.StringVar()
        ttk.Entry(self.frame, textvariable=user_var).pack(pady=2)
        ttk.Label(self.frame, text="Contraseña:").pack()
        pass_var = tk.StringVar()
        ttk.Entry(self.frame, textvariable=pass_var, show='*').pack(pady=2)

        def do_login(): # Función que se ejecuta al hacer clic en el botón de entrar
            username = user_var.get().strip()
            password = pass_var.get().strip()
            if self.sys.verify_user(username, password):
                role = self.sys.users[username].get('role', 'estudiante')
                # Destruir frame de login
                self.frame.destroy()
                # Abrir interfaz según rol
                if role == 'administrador':
                    AdminUserUI(self.root, self.sys, username)
                else:
                    CommonUserUI(self.root, self.sys, username)
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")

        ttk.Button(self.frame, text="Entrar", command=do_login).pack(pady=5)
        ttk.Button(self.frame, text="Volver", command=self.show_main_menu).pack()

if __name__ == '__main__':
    MainApp()
