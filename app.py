from flask import Flask, request, jsonify, render_template

import json

import os

 

app = Flask(__name__)

ARCHIVO = "datos.json"

 

 

@app.route("/")

def inicio():

    return render_template("index.html")

 

 

@app.route("/registrar", methods=["POST"])

def registrar():

    datos = request.get_json()

    nombre      = datos.get("nombre", "").strip()

    edad_texto = datos.get("edad", "")

 

    # --- Validaciones ---

    if not nombre:

        return jsonify({"mensaje": "El nombre esta vacio", "total": 0}), 400

 

    try:

        edad = int(edad_texto)

    except ValueError:

        return jsonify({"mensaje": "La edad debe ser un numero", "total": 0}), 400

 

    if edad < 0 or edad > 120:

        return jsonify({"mensaje": "Edad fuera de rango (0-120)", "total": 0}), 400

 

    # --- Calculo mayor / menor de edad ---

    categoria = "mayor de edad" if edad >= 18 else "menor de edad"

 

    # --- Leer lo existente ---

    if os.path.exists(ARCHIVO):

        with open(ARCHIVO, "r", encoding="utf-8") as f:

            registros = json.load(f)

    else:

        registros = []

 

    # --- Guardar el nuevo registro ---

    registros.append({"nombre": nombre, "edad": edad, "categoria": categoria})

 

    with open(ARCHIVO, "w", encoding="utf-8") as f:

        json.dump(registros, f, ensure_ascii=False, indent=2)

 

    # --- Responder ---

    return jsonify({

        "mensaje": f"{nombre} tiene {edad} anos: es {categoria}",

        "total": len(registros)

    })

 

 

if __name__ == "__main__":

    app.run(debug=True)