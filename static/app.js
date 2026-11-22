const boton = document.getElementById("btn");

const respuesta = document.getElementById("respuesta");

 

boton.addEventListener("click", async () => {

  const nombre = document.getElementById("nombre").value;

  const edad    = document.getElementById("edad").value;

 

  const res = await fetch("/registrar", {

    method: "POST",

    headers: { "Content-Type": "application/json" },

    body: JSON.stringify({ nombre: nombre, edad: edad })

  });

 

  const datos = await res.json();

  respuesta.textContent = datos.mensaje + " (total: " + datos.total + ")";

});
