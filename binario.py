import tkinter as tk

def generar_denuncia():
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()
    contacto = entry_contacto.get()
    hechos = texto_hechos.get("1.0", tk.END)
    dependencia = entry_dependencia.get()

    resultado = f"""
Tenancingo de Degollado, Estado de México
[Fecha]

A la Oficialía de Partes del H. Ayuntamiento de Tenancingo
Presente:

Yo, {nombre}, con domicilio en {direccion}, y número de contacto {contacto}, me permito presentar la siguiente denuncia:

HECHOS:
{hechos.strip()}

PETICIÓN:
Solicito respetuosamente que se tomen las medidas correspondientes conforme a la normatividad municipal, y que se me informe del seguimiento que se dará a esta denuncia. 
Adjunto los documentos que respaldan lo expuesto.

Sin otro particular, agradezco su atención y quedo en espera de una respuesta formal.

Atentamente,
[Firma]
{nombre}
"""

    texto_resultado.delete("1.0", tk.END)
    texto_resultado.insert(tk.END, resultado)

# Interfaz
root = tk.Tk()
root.title("Generador de Denuncias Municipales")

tk.Label(root, text="Nombre completo:").pack()
entry_nombre = tk.Entry(root, width=50)
entry_nombre.pack()

tk.Label(root, text="Dirección:").pack()
entry_direccion = tk.Entry(root, width=50)
entry_direccion.pack()

tk.Label(root, text="Contacto (teléfono o correo):").pack()
entry_contacto = tk.Entry(root, width=50)
entry_contacto.pack()

tk.Label(root, text="Área o dependencia a la que va dirigida:").pack()
entry_dependencia = tk.Entry(root, width=50)
entry_dependencia.pack()

tk.Label(root, text="Narración de los hechos:").pack()
texto_hechos = tk.Text(root, height=6, width=60)
texto_hechos.pack()

tk.Button(root, text="Generar Denuncia", command=generar_denuncia).pack(pady=10)

tk.Label(root, text="Resultado:").pack()
texto_resultado = tk.Text(root, height=15, width=80)
texto_resultado.pack()

root.mainloop()
