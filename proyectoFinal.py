import json
import os
import tkinter
from tkinter import  Tk, messagebox, simpledialog, Toplevel, Frame, Label, Scrollbar, Text
from PIL import Image, ImageTk
import customtkinter 
 
# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
customtkinter.set_appearance_mode("System")     
 
# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
customtkinter.set_default_color_theme("blue")   

root_folder = os.path.dirname(os.path.abspath(__file__))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Sistema de Comidas Rápidas")
        self.geometry(f"{1100}x{540}")      
               
        # Ruta de la imagen de logo
        ruta_img = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
        logo_path = os.path.join(ruta_img, "hamburguesa.png")
        imagen1 = Image.open(os.path.join(ruta_img, 'lamina.png'))
        imagen1 = imagen1.resize((50, 50))  # Redimensionar la imagen al tamaño deseado
        imagen1_tk = ImageTk.PhotoImage(imagen1)
        imagen2 = Image.open(os.path.join(ruta_img, 'pizza.png'))
        imagen2 = imagen2.resize((50, 50))  # Redimensionar la imagen al tamaño deseado
        imagen2_tk = ImageTk.PhotoImage(imagen2)
        imagen3 = Image.open(os.path.join(ruta_img, 'corte.png'))
        imagen3 = imagen3.resize((50, 50))  # Redimensionar la imagen al tamaño deseado
        imagen3_tk = ImageTk.PhotoImage(imagen3)
        imagen4 = Image.open(os.path.join(ruta_img, 'contenedor-de-basura.png'))
        imagen4 = imagen4.resize((50, 50))  # Redimensionar la imagen al tamaño deseado
        imagen4_tk = ImageTk.PhotoImage(imagen4)
        imagen5 = Image.open(os.path.join(ruta_img, 'mezclador.png'))
        imagen5 = imagen5.resize((50, 50))  # Redimensionar la imagen al tamaño deseado
        imagen5_tk = ImageTk.PhotoImage(imagen5)
        imagen6 = Image.open(os.path.join(ruta_img, 'dolar.png'))
        imagen6 = imagen6.resize((50, 50))  # Redimensionar la imagen al tamaño deseado
        imagen6_tk = ImageTk.PhotoImage(imagen6)
        imagen7 = Image.open(os.path.join(ruta_img, 'galleta.png'))
        imagen7 = imagen7.resize((50, 50))  # Redimensionar la imagen al tamaño deseado
        imagen7_tk = ImageTk.PhotoImage(imagen7)
        imagen8 = Image.open(os.path.join(ruta_img, 'cesta.png'))
        imagen8 = imagen8.resize((50, 50))  # Redimensionar la imagen al tamaño deseado
        imagen8_tk = ImageTk.PhotoImage(imagen8)
        imagen9 = Image.open(os.path.join(ruta_img, 'ensalada.png'))
        imagen9 = imagen9.resize((50, 50))  # Redimensionar la imagen al tamaño deseado
        imagen9_tk = ImageTk.PhotoImage(imagen9)
        imagen10 = Image.open(os.path.join(ruta_img, 'torrencial.png'))
        imagen10 = imagen10.resize((50, 50))  # Redimensionar la imagen al tamaño deseado
        imagen10_tk = ImageTk.PhotoImage(imagen10)

        # Load and resize the image
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((100, 100))
        logo_photo = ImageTk.PhotoImage(logo_image)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=0)                              

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bienvenidos al sistema ¿Qué acción deseas realizar?", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.logo_image_label = customtkinter.CTkLabel(self.sidebar_frame, image=logo_photo, text=None)
        self.logo_image_label.image = logo_photo
        self.logo_image_label.grid(row=0, column=1, padx=20)
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Mostrar comidas rápidas", image=imagen2_tk, command=lambda:app.mostrar_comidas(menu))
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Agregar comida", image=imagen1_tk, command=lambda:app.agregar_comida(menu))
        self.sidebar_button_2.grid(row=2, column=1, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Modificar comida", image=imagen3_tk, command=lambda:app.modificar_comida(menu))
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Eliminar comida", image=imagen4_tk, command=lambda:app.eliminar_comida(menu))
        self.sidebar_button_4.grid(row=3, column=1, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Agregar pasos de elaboración", image=imagen5_tk, command=lambda:app.agregar_pasos_elaboracion(menu))
        self.sidebar_button_5.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, text="Buscar por precio", image=imagen6_tk, command=lambda:app.buscar_por_precio(menu))
        self.sidebar_button_6.grid(row=4, column=1, padx=20, pady=10)
        self.sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame, text="Buscar por calorías", image=imagen7_tk, command=lambda:app.buscar_por_calorias(menu))
        self.sidebar_button_7.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_8 = customtkinter.CTkButton(self.sidebar_frame, text="Buscar por ingrediente", image=imagen8_tk, command=lambda:app.buscar_por_ingrediente(menu))
        self.sidebar_button_8.grid(row=5, column=1, padx=20, pady=10)
        self.sidebar_button_9 = customtkinter.CTkButton(self.sidebar_frame, text="Mostrar comidas veganas", image=imagen9_tk, command=lambda:app.mostrar_comidas_veganas(menu))
        self.sidebar_button_9.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_10 = customtkinter.CTkButton(self.sidebar_frame, text="Mostrar comidas con pasos de elaboracion", image=imagen10_tk, command=lambda:app.mostrar_comidas_pasos(menu))
        self.sidebar_button_10.grid(row=6, column=1, padx=20, pady=10)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=0, column=3, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=1, column=3, padx=20, pady=(10, 10))
        
        # set default values
        self.appearance_mode_optionemenu.set("Dark")


    # Función para cargar los datos del archivo JSON
    def cargar_menu(self):
        json_path = os.path.join(root_folder, 'comidas_rapidas.json')
        with open(json_path, 'rt', encoding="utf-8") as json_file:
            return json.load(json_file)


    # Función para guardar los datos en el archivo JSON
    def escribir_json_comidas(self, menu):
        json_path = os.path.join(root_folder, 'comidas_rapidas.json')
        with open(json_path, "w") as file:
            json.dump(menu, file, indent=4)

    # Función para mostrar todas las comidas rápidas existentes
    def mostrar_comidas(self, menu):
            if len(menu) == 0:
                messagebox.showinfo("Comidas rápidas", "No hay comidas rápidas disponibles")
            else:
                dialog = Toplevel()
                dialog.title("Comidas rápidas disponibles")
                
                # Crear una barra de desplazamiento vertical
                scrollbar = Scrollbar(dialog)
                scrollbar.pack(side="right", fill="y")

                # Crear un widget Text para mostrar el contenido de las comidas
                text_widget = Text(dialog, yscrollcommand=scrollbar.set)
                text_widget.pack(side="left", fill="both", expand=True)

                # Configurar la barra de desplazamiento para controlar el widget Text
                scrollbar.configure(command=text_widget.yview)
                
                for comida in menu:
                    text_widget.insert("end", f"ID: {comida.get('id')}\n")
                    text_widget.insert("end", f"Descripción: {comida['descripcion']}\n")
                    text_widget.insert("end", f"Precio: {comida.get('precio')}\n")
                    text_widget.insert("end", f"Ingredientes: {', '.join(comida.get('ingredientes', []))}\n")
                    text_widget.insert("end", f"Tiempo de elaboración: {comida.get('tiempo')} minutos\n")
                    text_widget.insert("end", f"Calorías: {comida.get('calorias')}\n")
                    text_widget.insert("end", f"Vegana: {'Si' if comida.get('vegana', False) else 'No'}\n")
                    text_widget.insert("end", "---------------------------\n")

                # Desactivar la edición del widget Text
                text_widget.config(state="disabled")
                
                dialog.show()


    # Función para agregar una nueva comida rápida al menú
    def agregar_comida(self, menu):
        dialog = tkinter.Toplevel()
        dialog.geometry("400x300")
        dialog.title("Nueva comida rápida")

        descripcion_var = tkinter.StringVar()
        precio_var = tkinter.StringVar()
        ingredientes_var = tkinter.StringVar()
        tiempo_var = tkinter.StringVar()
        calorias_var = tkinter.StringVar()
        vegana_var = tkinter.StringVar()

        tkinter.Label(dialog, text="Descripción:", font=("Arial", 10)).pack()
        descripcion_entry = tkinter.Entry(dialog, textvariable=descripcion_var, width=30)
        descripcion_entry.pack()

        tkinter.Label(dialog, text="Precio:", font=("Arial", 10)).pack()
        precio_entry = tkinter.Entry(dialog, textvariable=precio_var, width=30)
        precio_entry.pack()

        tkinter.Label(dialog, text="Ingredientes: (separados por comas)", font=("Arial", 10)).pack()
        ingredientes_entry = tkinter.Entry(dialog, textvariable=ingredientes_var, width=50)
        ingredientes_entry.pack()

        tkinter.Label(dialog, text="Tiempo de elaboración:", font=("Arial", 10)).pack()
        tiempo_entry = tkinter.Entry(dialog, textvariable=tiempo_var, width=30)
        tiempo_entry.pack()

        tkinter.Label(dialog, text="Calorías:", font=("Arial", 10)).pack()
        calorias_entry = tkinter.Entry(dialog, textvariable=calorias_var, width=30)
        calorias_entry.pack()

        tkinter.Label(dialog, text="Vegana (Sí/No):", font=("Arial", 10)).pack()
        vegana_entry = tkinter.Entry(dialog, textvariable=vegana_var, width=30)
        vegana_entry.pack()

        tkinter.Label(dialog, text="").pack()  # Espacio adicional

        def guardar():
            descripcion = descripcion_var.get()
            precio_str = precio_var.get()
            ingredientes = [i.strip() for i in ingredientes_var.get().split(',')]
            tiempo_str = tiempo_var.get()
            calorias_str = calorias_var.get()
            vegana = vegana_var.get().lower() == 'si' or vegana_var.get().lower() == 'SI' or vegana_var.get().lower() == 'Si'

            if not descripcion or not precio_str or not ingredientes or not tiempo_str or not calorias_str:
                messagebox.showerror("Error", "Debe completar todos los campos")
                return

            try:
                precio = float(precio_str)
                tiempo = int(tiempo_str)
                calorias = int(calorias_str)
            except ValueError:
                messagebox.showerror("Error", "Ingrese valores numéricos válidos para el precio, tiempo y calorías")
                return

            nueva_comida = {
                'id': len(menu) + 1,
                'descripcion': descripcion,
                'precio': precio,
                'ingredientes': ingredientes,
                'tiempo': tiempo,
                'calorias': calorias,
                'vegana': vegana
            }

            menu.append(nueva_comida)
            self.escribir_json_comidas(menu)
            messagebox.showinfo("Nueva comida rápida", "La comida se ha agregado al menú correctamente")
            dialog.destroy()

        guardar_button = tkinter.Button(dialog, text="Guardar", command=guardar)
        guardar_button.pack()

    # Función para modificar los datos de una comida existente
    def modificar_comida(self, menu):
                id = simpledialog.askstring("Modificar comida", "Ingrese el ID de la comida que desea modificar:")
                id = int(id) if id else None

                for comida in menu:
                    if comida['id'] == id:
                        dialog = tkinter.Toplevel()
                        dialog.geometry("400x300")
                        dialog.title("Modificar comida")

                        descripcion_var = tkinter.StringVar(value=comida['descripcion'])
                        precio_var = tkinter.StringVar(value=comida['precio'])
                        ingredientes_var = tkinter.StringVar(value=', '.join(comida['ingredientes']))
                        tiempo_var = tkinter.StringVar(value=comida['tiempo'])
                        calorias_var = tkinter.StringVar(value=comida['calorias'])
                        vegana_var = tkinter.StringVar(value='Sí' if comida['vegana'] else 'No')

                        tkinter.Label(dialog, text="Descripción:", font=("Arial", 10)).pack()
                        descripcion_entry = tkinter.Entry(dialog, textvariable=descripcion_var, width=30)
                        descripcion_entry.pack()

                        tkinter.Label(dialog, text="Precio:", font=("Arial", 10)).pack()
                        precio_entry = tkinter.Entry(dialog, textvariable=precio_var, width=30)
                        precio_entry.pack()

                        tkinter.Label(dialog, text="Ingredientes: (separe los ingredientes mediante comas)",  font=("Arial", 10)).pack()
                        ingredientes_entry = tkinter.Entry(dialog, textvariable=ingredientes_var, width=50)
                        ingredientes_entry.pack()

                        tkinter.Label(dialog, text="Tiempo de elaboración:", font=("Arial", 10)).pack()
                        tiempo_entry = tkinter.Entry(dialog, textvariable=tiempo_var, width=30)
                        tiempo_entry.pack()

                        tkinter.Label(dialog, text="Calorías:", font=("Arial", 10)).pack()
                        calorias_entry = tkinter.Entry(dialog, textvariable=calorias_var, width=30)
                        calorias_entry.pack()

                        tkinter.Label(dialog, text="Vegana (Sí/No):", font=("Arial", 10)).pack()
                        vegana_entry = tkinter.Entry(dialog, textvariable=vegana_var, width=30)
                        vegana_entry.pack()

                        def guardar():
                            comida['descripcion'] = descripcion_var.get()
                            comida['precio'] = float(precio_var.get())
                            comida['ingredientes'] = [i.strip() for i in ingredientes_var.get().split(',')]
                            comida['tiempo'] = int(tiempo_var.get())
                            comida['calorias'] = int(calorias_var.get())
                            comida['vegana'] = vegana_var.get().lower() == 'si' or vegana_var.get().lower() == 'SI' or  vegana_var.get().lower() == 'Si'

                            self.escribir_json_comidas(menu)
                            messagebox.showinfo("Modificar comida", "La comida se ha modificado correctamente")
                            dialog.destroy()

                        guardar_button = tkinter.Button(dialog, text="Guardar", command=guardar)
                        guardar_button.pack()

                        break

                else:
                    messagebox.showerror("Modificar comida", "No se encontró ninguna comida con el ID ingresado")


    # Función para eliminar una comida del menú
    def eliminar_comida(self, menu):
            id = simpledialog.askstring("Eliminar comida", "Ingrese el ID de la comida que desea eliminar:")
            id = int(id) if id else None
            
            for comida in menu:
                if comida['id'] == id:
                    menu.remove(comida)
                    self.escribir_json_comidas(menu)
                    messagebox.showinfo("Eliminar comida", "La comida se ha eliminado del menú correctamente")
                    return
            
            messagebox.showerror("Eliminar comida", "No se encontró ninguna comida con el ID ingresado")


    # Función para buscar comidas por ingrediente
    def buscar_por_ingrediente(self, menu):
            ingrediente = simpledialog.askstring("Buscar por ingrediente", "Ingrese el ingrediente que desea buscar:")
            if ingrediente is None:
                return
            
            comidas_encontradas = []
            for comida in menu:
                if ingrediente.lower() in [ing.lower() for ing in comida['ingredientes']]:
                    comidas_encontradas.append(comida)
            
            if len(comidas_encontradas) == 0:
                messagebox.showinfo("Buscar por ingrediente", "No se encontraron comidas que contengan ese ingrediente")
            else:
                ventana_emergente = tkinter.Toplevel(app)
                ventana_emergente.title("Comidas que contienen el ingrediente: " + ingrediente)
                
                for comida in comidas_encontradas:
                    label_id = tkinter.Label(ventana_emergente, text=f"ID: {comida['id']}")
                    label_id.pack()
                    label_descripcion = tkinter.Label(ventana_emergente, text=f"Descripción: {comida['descripcion']}")
                    label_descripcion.pack()
                    label_precio = tkinter.Label(ventana_emergente, text=f"Precio: {comida['precio']}")
                    label_precio.pack()
                    label_ingredientes = tkinter.Label(ventana_emergente, text=f"Ingredientes: {', '.join(comida['ingredientes'])}")
                    label_ingredientes.pack()
                    label_tiempo = tkinter.Label(ventana_emergente, text=f"Tiempo de elaboración: {comida['tiempo']} minutos")
                    label_tiempo.pack()
                    label_calorias = tkinter.Label(ventana_emergente, text=f"Calorías: {comida['calorias']}")
                    label_calorias.pack()
                    label_vegana = tkinter.Label(ventana_emergente, text=f"Vegana: {'Sí' if comida['vegana'] else 'No'}")
                    label_vegana.pack()
                    
                    separador = tkinter.Label(ventana_emergente, text="---------------------------")
                    separador.pack()


    # Función para buscar comidas por precio
    def buscar_por_precio(self, menu):
            ventana_emergente = tkinter.Toplevel(self)
            ventana_emergente.title("Buscar por precio")
            ventana_emergente.geometry("300x100")

            precio_label = tkinter.Label(ventana_emergente, text="Ingrese el precio que desea buscar:")
            precio_label.pack()

            precio_entry = tkinter.Entry(ventana_emergente)
            precio_entry.pack()

            def buscar():
                precio_str = precio_entry.get()
                if not precio_str:
                    return

                try:
                    precio = float(precio_str)
                except ValueError:
                    messagebox.showerror("Error", "Ingrese un valor numérico válido para el precio")
                    return

                comidas_encontradas = []
                for comida in menu:
                    if comida['precio'] == precio:
                        comidas_encontradas.append(comida)

                if len(comidas_encontradas) == 0:
                    messagebox.showinfo("Buscar por precio", "No se encontraron comidas con el precio ingresado")
                else:
                    mensaje = "Comidas con el precio de {} pesos:\n\n".format(precio)
                    mensaje += "\n".join([
                        "ID: {}\nDescripción: {}\nPrecio: {}\nIngredientes: {}\nTiempo de elaboración: {} minutos\nCalorías: {}\nVegana: {}\n---------------------------".format(
                            comida['id'], comida['descripcion'], comida['precio'], ", ".join(comida['ingredientes']),
                            comida['tiempo'], comida['calorias'], 'Sí' if comida['vegana'] else 'No'
                        )
                        for comida in comidas_encontradas
                    ])
                    messagebox.showinfo("Comidas con el precio ingresado", mensaje)

            buscar_button = tkinter.Button(ventana_emergente, text="Buscar", command=buscar)
            buscar_button.pack()


    # Función para buscar comidas por calorías
    def buscar_por_calorias(self, menu):
            calorias = simpledialog.askinteger("Buscar por calorías", "Ingrese la cantidad de calorías que desea buscar:")
            
            if calorias is None:
                return
            
            comidas_encontradas = []
            for comida in menu:
                if comida['calorias'] == calorias:
                    comidas_encontradas.append(comida)
            
            if len(comidas_encontradas) == 0:
                messagebox.showinfo("Buscar por calorías", "No se encontraron comidas con las calorías ingresadas")
            else:
                dialog = tkinter.Toplevel()
                dialog.title("Comidas por debajo de las calorías")

                text_widget = tkinter.Text(dialog, width=60, height=30)
                text_widget.pack()

                for comida in comidas_encontradas:
                    text_widget.insert(tkinter.END, f"ID: {comida['id']}\n")
                    text_widget.insert(tkinter.END, f"Descripción: {comida['descripcion']}\n")
                    text_widget.insert(tkinter.END, f"Precio: {comida['precio']}\n")
                    text_widget.insert(tkinter.END, f"Ingredientes: {', '.join(comida['ingredientes'])}\n")
                    text_widget.insert(tkinter.END, f"Tiempo de elaboración: {comida['tiempo']} minutos\n")
                    text_widget.insert(tkinter.END, f"Calorías: {comida['calorias']}\n")
                    text_widget.insert(tkinter.END, f"Vegana: {'Sí' if comida['vegana'] else 'No'}\n")
                    text_widget.insert(tkinter.END, "---------------------------\n")

                text_widget.configure(state='disabled')

                dialog.transient(self)
                dialog.grab_set()
                self.wait_window(dialog)


    # Función para mostrar las comidas veganas disponibles
    def mostrar_comidas_veganas(self, menu): 
            comidas_veganas = [comida for comida in menu if comida['vegana']]
            
            if len(comidas_veganas) == 0:
                messagebox.showinfo("Comidas veganas disponibles", "No hay comidas veganas disponibles")
            else:
                messagebox.showinfo("Comidas veganas disponibles", "\n".join([f"ID: {comida['id']}\nDescripción: {comida['descripcion']}\n" +
                                                                            f"Precio: {comida['precio']} ARS\nIngredientes: {', '.join(comida['ingredientes'])}\n" +
                                                                            f"Tiempo de elaboración: {comida['tiempo']} minutos\nCalorías: {comida['calorias']} gramos\n" +
                                                                            "Vegana: Sí\n" +
                                                                            "---------------------------" for comida in comidas_veganas]))


    # Función para agregar los pasos de elaboración de una comida
    def agregar_pasos_elaboracion(self, menu):
            id = simpledialog.askstring("Agregar pasos de elaboración", "Ingrese el ID de la comida a la cual desea agregar los pasos de elaboración:")
            id = int(id) if id else None

            for comida in menu:
                if comida['id'] == id:
                    pasos = simpledialog.askstring("Agregar pasos de elaboración", "Ingrese los pasos de elaboración (separados por comas):").split(',')
                    comida['pasos_elaboracion'] = pasos
                    self.escribir_json_comidas(menu)
                    messagebox.showinfo("Agregar pasos de elaboración", "Los pasos de elaboración se han agregado correctamente.")
                    return
            
            messagebox.showerror("Agregar pasos de elaboración", "No se encontró ninguna comida con el ID ingresado")


    # Función para mostrar todas las comidas rápidas existentes con los pasos de elaboracion agregados
    def mostrar_comidas_pasos(self, menu):
            if len(menu) == 0:
                messagebox.showinfo("Mostrar comidas con pasos de elaboración", "No hay comidas rápidas disponibles")
            else:
                dialog = Toplevel()
                dialog.title("Comidas rápidas disponibles")
                
                # Crear una barra de desplazamiento vertical
                scrollbar = Scrollbar(dialog)
                scrollbar.pack(side="right", fill="y")

                # Crear un widget Text para mostrar el contenido de las comidas
                text_widget = Text(dialog, yscrollcommand=scrollbar.set)
                text_widget.pack(side="left", fill="both", expand=True)

                # Configurar la barra de desplazamiento para controlar el widget Text
                scrollbar.configure(command=text_widget.yview)
                
                for comida in menu:
                    text_widget.insert("end", f"ID: {comida.get('id')}\n")
                    text_widget.insert("end", f"Descripción: {comida['descripcion']}\n")
                    text_widget.insert("end", f"Precio: {comida.get('precio')}\n")
                    text_widget.insert("end", f"Ingredientes: {', '.join(comida.get('ingredientes', []))}\n")
                    text_widget.insert("end", f"Tiempo de elaboración: {comida.get('tiempo')} minutos\n")
                    text_widget.insert("end", f"Calorías: {comida.get('calorias')}\n")
                    text_widget.insert("end", f"Vegana: {'Si' if comida.get('vegana', False) else 'No'}\n")
                    text_widget.insert("end", f"Pasos de elaboración: {', '.join(comida.get('pasos_elaboracion', []))}\n")
                    text_widget.insert("end", "---------------------------\n")

                # Desactivar la edición del widget Text
                text_widget.config(state="disabled")

                dialog.mainloop()
                    

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)



    
    
if __name__ == "__main__":
    app = App()
    menu = app.cargar_menu()
    app.mainloop()