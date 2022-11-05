const agregar = document.getElementById("btn_agregar");
const nombre = document.getElementById("nombre");
const ape_paterno = document.getElementById("ape_paterno");
const ape_materno = document.getElementById("ape_materno");
const correo = document.getElementById("correo");
const num_emergencia = document.getElementById("num_emergencia");

const agregarEvento = (e) => {
  e.preventDefault();
  const data = {
    nombre: nombre.value,
    ape_paterno: ape_paterno.value,
    ape_materno: ape_materno.value,
    correo: correo.value,
    num_emergencia: num_emergencia.value,
  };

  fetch("/agregar-alumno", {
    method: "POST",
    body: JSON.stringify(data),
    headers: { "Content-Type": "application/json" },
  })
    .then((request) => {
      return request.json();
    })
    .then((data) => {
      console.log(data);
      // window.location.href = "/mostrar-alumnos";
    })
    .catch((error) => {
      console.log("error al crear el alumno");
    });
};

agregar.addEventListener("click", agregarEvento);
