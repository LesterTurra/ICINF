import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


class Profesor:
    def __init__(self, rut, nombre, ano_nacimiento, especialidad):
        self.rut = rut
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.especialidad = especialidad

    def to_dict(self):
        return {
            "rut": self.rut,
            "nombre": self.nombre,
            "ano_nacimiento": self.ano_nacimiento,
            "especialidad": self.especialidad
        }


class Apoderado:
    def __init__(self, rut, nombre, telefono):
        self.rut = rut
        self.nombre = nombre
        self.telefono = telefono

    def to_dict(self):
        return {
            "rut": self.rut,
            "nombre": self.nombre,
            "telefono": self.telefono
        }


class Estudiante:
    def __init__(self, rut, nombre, direccion, ano_nacimiento, posicion, ano_incorporacion, profesor, apoderado):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.ano_nacimiento = ano_nacimiento
        self.posicion = posicion
        self.ano_incorporacion = ano_incorporacion
        self.profesor = profesor
        self.apoderado = apoderado
        self.goles = 0  # Inicialmente sin goles

    def to_dict(self):
        return {
            "rut": self.rut,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "ano_nacimiento": self.ano_nacimiento,
            "posicion": self.posicion,
            "ano_incorporacion": self.ano_incorporacion,
            "profesor": self.profesor.nombre if self.profesor else "",
            "apoderado": self.apoderado.nombre if self.apoderado else "",
            "goles": self.goles
        }


class BarrabasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Barrabás")

        self.profesores = []
        self.apoderados = []
        self.estudiantes = []

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(padx=10, pady=10)

        # Crear pestañas
        self.crear_tab_profesores()
        self.crear_tab_estudiantes()
        self.crear_tab_apoderados()
        self.crear_tab_consultas()
        self.crear_tab_ranking()

        self.cargar_datos()

    def crear_tab_profesores(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Profesores")

        ttk.Label(tab, text="RUT:").grid(row=0, column=0, padx=5, pady=5)
        self.rut_profesor = ttk.Entry(tab)
        self.rut_profesor.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        self.nombre_profesor = ttk.Entry(tab)
        self.nombre_profesor.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Año Nacimiento:").grid(row=2, column=0, padx=5, pady=5)
        self.ano_nacimiento_profesor = ttk.Entry(tab)
        self.ano_nacimiento_profesor.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Especialidad:").grid(row=3, column=0, padx=5, pady=5)
        self.especialidad_profesor = ttk.Entry(tab)
        self.especialidad_profesor.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Agregar Profesor", command=self.agregar_profesor).grid(row=4, column=0, columnspan=2, pady=10)

        # Lista de profesores
        self.lista_profesores = ttk.Treeview(tab, columns=("RUT", "Nombre", "Año Nacimiento", "Especialidad"), show="headings")
        self.lista_profesores.grid(row=5, column=0, columnspan=2, pady=10)

        for col in self.lista_profesores["columns"]:
            self.lista_profesores.heading(col, text=col)

    def agregar_profesor(self):
        rut = self.rut_profesor.get()
        nombre = self.nombre_profesor.get()
        ano_nacimiento = self.ano_nacimiento_profesor.get()
        especialidad = self.especialidad_profesor.get()

        if rut and nombre and ano_nacimiento and especialidad:
            profesor = Profesor(rut, nombre, ano_nacimiento, especialidad)
            self.profesores.append(profesor)

            # Agregar el profesor a la lista
            self.lista_profesores.insert("", "end", values=(rut, nombre, ano_nacimiento, especialidad))

            messagebox.showinfo("Éxito", f"Profesor {nombre} agregado correctamente.")
            self.limpiar_campos_profesor()

            # Guardar datos en JSON
            self.guardar_datos()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def limpiar_campos_profesor(self):
        self.rut_profesor.delete(0, tk.END)
        self.nombre_profesor.delete(0, tk.END)
        self.ano_nacimiento_profesor.delete(0, tk.END)
        self.especialidad_profesor.delete(0, tk.END)

    def crear_tab_estudiantes(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Estudiantes")

        ttk.Label(tab, text="RUT:").grid(row=0, column=0, padx=5, pady=5)
        self.rut_estudiante = ttk.Entry(tab)
        self.rut_estudiante.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        self.nombre_estudiante = ttk.Entry(tab)
        self.nombre_estudiante.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Dirección:").grid(row=2, column=0, padx=5, pady=5)
        self.direccion_estudiante = ttk.Entry(tab)
        self.direccion_estudiante.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Año Nacimiento:").grid(row=3, column=0, padx=5, pady=5)
        self.ano_estudiante = ttk.Entry(tab)
        self.ano_estudiante.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Posición:").grid(row=4, column=0, padx=5, pady=5)
        self.posicion_estudiante = ttk.Entry(tab)
        self.posicion_estudiante.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Año Incorporación:").grid(row=5, column=0, padx=5, pady=5)
        self.incorporacion_estudiante = ttk.Entry(tab)
        self.incorporacion_estudiante.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Profesor:").grid(row=6, column=0, padx=5, pady=5)
        self.profesor_estudiante = ttk.Combobox(tab, values=[prof.nombre for prof in self.profesores])
        self.profesor_estudiante.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Apoderado:").grid(row=7, column=0, padx=5, pady=5)
        self.apoderado_estudiante = ttk.Combobox(tab, values=[a.nombre for a in self.apoderados])
        self.apoderado_estudiante.grid(row=7, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=8, column=0, columnspan=2, pady=10)

        # Lista de estudiantes
        self.lista_estudiantes = ttk.Treeview(tab, columns=("RUT", "Nombre", "Dirección", "Año Nacimiento", "Posición", "Año Incorporación", "Profesor", "Apoderado"), show="headings")
        self.lista_estudiantes.grid(row=9, column=0, columnspan=2, pady=10)

        for col in self.lista_estudiantes["columns"]:
            self.lista_estudiantes.heading(col, text=col)

    def agregar_estudiante(self):
        rut = self.rut_estudiante.get()
        nombre = self.nombre_estudiante.get()
        direccion = self.direccion_estudiante.get()
        ano = self.ano_estudiante.get()
        posicion = self.posicion_estudiante.get()
        incorporacion = self.incorporacion_estudiante.get()
        profesor_nombre = self.profesor_estudiante.get()
        apoderado_nombre = self.apoderado_estudiante.get()

        # Buscar el profesor y el apoderado por su nombre
        profesor = next((prof for prof in self.profesores if prof.nombre == profesor_nombre), None)
        apoderado = next((a for a in self.apoderados if a.nombre == apoderado_nombre), None)

        if not profesor:
            messagebox.showerror("Error", f"El profesor '{profesor_nombre}' no está registrado.")
            return
        if not apoderado:
            messagebox.showerror("Error", f"El apoderado '{apoderado_nombre}' no está registrado.")
            return

        if rut and nombre and direccion and ano and posicion and incorporacion:
            estudiante = Estudiante(rut, nombre, direccion, ano, posicion, incorporacion, profesor, apoderado)
            self.estudiantes.append(estudiante)

            # Agregar el estudiante a la lista
            self.lista_estudiantes.insert("", "end", values=(
                rut, nombre, direccion, ano, posicion, incorporacion, profesor.nombre, apoderado.nombre
            ))

            messagebox.showinfo("Éxito", f"Estudiante {nombre} agregado correctamente.")
            self.limpiar_campos_estudiante()

            # Guardar datos en JSON
            self.guardar_datos()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def limpiar_campos_estudiante(self):
        self.rut_estudiante.delete(0, tk.END)
        self.nombre_estudiante.delete(0, tk.END)
        self.direccion_estudiante.delete(0, tk.END)
        self.ano_estudiante.delete(0, tk.END)
        self.posicion_estudiante.delete(0, tk.END)
        self.incorporacion_estudiante.delete(0, tk.END)
        self.profesor_estudiante.set('')
        self.apoderado_estudiante.set('')

    def crear_tab_apoderados(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Apoderados")

        ttk.Label(tab, text="RUT:").grid(row=0, column=0, padx=5, pady=5)
        self.rut_apoderado = ttk.Entry(tab)
        self.rut_apoderado.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        self.nombre_apoderado = ttk.Entry(tab)
        self.nombre_apoderado.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Teléfono:").grid(row=2, column=0, padx=5, pady=5)
        self.telefono_apoderado = ttk.Entry(tab)
        self.telefono_apoderado.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Agregar Apoderado", command=self.agregar_apoderado).grid(row=3, column=0, columnspan=2, pady=10)

        # Lista de apoderados
        self.lista_apoderados = ttk.Treeview(tab, columns=("RUT", "Nombre", "Teléfono"), show="headings")
        self.lista_apoderados.grid(row=4, column=0, columnspan=2, pady=10)

        for col in self.lista_apoderados["columns"]:
            self.lista_apoderados.heading(col, text=col)

    def agregar_apoderado(self):
        rut = self.rut_apoderado.get()
        nombre = self.nombre_apoderado.get()
        telefono = self.telefono_apoderado.get()

        if rut and nombre and telefono:
            apoderado = Apoderado(rut, nombre, telefono)
            self.apoderados.append(apoderado)

            # Agregar el apoderado a la lista
            self.lista_apoderados.insert("", "end", values=(rut, nombre, telefono))

            messagebox.showinfo("Éxito", f"Apoderado {nombre} agregado correctamente.")
            self.limpiar_campos_apoderado()

            # Guardar datos en JSON
            self.guardar_datos()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def limpiar_campos_apoderado(self):
        self.rut_apoderado.delete(0, tk.END)
        self.nombre_apoderado.delete(0, tk.END)
        self.telefono_apoderado.delete(0, tk.END)

    def crear_tab_consultas(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Consultas")

        # Consultar estudiantes por profesor
        ttk.Label(tab, text="Profesor:").grid(row=0, column=0, padx=5, pady=5)
        self.profesor_consulta = ttk.Combobox(tab, values=[prof.nombre for prof in self.profesores])
        self.profesor_consulta.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Consultar Estudiantes", command=self.consultar_estudiantes_por_profesor).grid(row=1, column=0, columnspan=2, pady=10)

        # Resultados de la consulta
        self.resultados_consulta = ttk.Treeview(tab, columns=("RUT", "Nombre", "Profesor"), show="headings")
        self.resultados_consulta.grid(row=2, column=0, columnspan=2, pady=10)

        for col in self.resultados_consulta["columns"]:
            self.resultados_consulta.heading(col, text=col)

    def consultar_estudiantes_por_profesor(self):
        profesor_nombre = self.profesor_consulta.get()

        if profesor_nombre:
            estudiantes_filtrados = [estudiante for estudiante in self.estudiantes if estudiante.profesor.nombre == profesor_nombre]
            self.resultados_consulta.delete(*self.resultados_consulta.get_children())  # Limpiar la lista

            for estudiante in estudiantes_filtrados:
                self.resultados_consulta.insert("", "end", values=(estudiante.rut, estudiante.nombre, estudiante.profesor.nombre))

        else:
            messagebox.showerror("Error", "Seleccione un profesor para realizar la consulta.")

    def crear_tab_ranking(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Ranking")

        ttk.Button(tab, text="Generar Ranking de Goles", command=self.generar_ranking).grid(row=0, column=0, pady=10)

        # Ranking de goles
        self.ranking_goles = ttk.Treeview(tab, columns=("Nombre", "Goles"), show="headings")
        self.ranking_goles.grid(row=1, column=0, columnspan=2, pady=10)

        for col in self.ranking_goles["columns"]:
            self.ranking_goles.heading(col, text=col)

    def generar_ranking(self):
        # Ordenar estudiantes por goles
        estudiantes_ordenados = sorted(self.estudiantes, key=lambda e: e.goles, reverse=True)
        self.ranking_goles.delete(*self.ranking_goles.get_children())  # Limpiar la lista

        for estudiante in estudiantes_ordenados:
            self.ranking_goles.insert("", "end", values=(estudiante.nombre, estudiante.goles))

    def guardar_datos(self):
        # Guardar los datos en archivos JSON
        with open("profesores.json", "w") as f:
            json.dump([prof.to_dict() for prof in self.profesores], f)

        with open("apoderados.json", "w") as f:
            json.dump([a.to_dict() for a in self.apoderados], f)

        with open("estudiantes.json", "w") as f:
            json.dump([est.to_dict() for est in self.estudiantes], f)

    def cargar_datos(self):
        # Cargar datos desde archivos JSON
        if os.path.exists("profesores.json"):
            with open("profesores.json", "r") as f:
                data = json.load(f)
                self.profesores = [Profesor(**prof) for prof in data]

        if os.path.exists("apoderados.json"):
            with open("apoderados.json", "r") as f:
                data = json.load(f)
                self.apoderados = [Apoderado(**a) for a in data]

        if os.path.exists("estudiantes.json"):
            with open("estudiantes.json", "r") as f:
                data = json.load(f)
                self.estudiantes = [Estudiante(**est) for est in data]

# Crear la ventana principal
root = tk.Tk()
app = BarrabasApp(root)
root.mainloop()  



























