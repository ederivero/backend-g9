const addUser = document.getElementById("addUser");
const getUser = document.getElementById("getUsers");
const correo = document.getElementById("correo");
const nombre = document.getElementById("nombre");
const apellido = document.getElementById("apellido");
const usuarios = document.getElementById("usuarios");

function addUserClick(e) {
  e.preventDefault();
  const data = {
    nombre: nombre.value,
    apellido: apellido.value,
    correo: correo.value,
  };
  console.log(data);

  fetch("http://127.0.0.1:5000/registrarse", {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((respuesta) => {
      // esto sucedera si todo esta bien
      console.log("Creacion exitosa");
      return respuesta.json();
    })
    .then((resultado) => {
      console.log(resultado);
    })
    .catch((error) => {
      // esto sucedera si hubo un error
      console.log(error);
    });

  getUser.click();
}

function getUserClick(e) {
  e.preventDefault();
  usuarios.innerHTML = ` <tr>
  <th>id</th>
  <th>correo</th>
  <th>nombre</th>
  <th>apellido</th>
</tr>`;
  const fila = document.createElement("tr");
  const columnaId = document.createElement("td");
  const columnaCorreo = document.createElement("td");
  const columnaNombre = document.createElement("td");
  const columnaApellido = document.createElement("td");
  columnaId.innerHTML = "1";
  columnaCorreo.innerHTML = "c@c.c";
  columnaNombre.innerHTML = "edu";
  columnaApellido.innerHTML = "de rivero";

  fila.appendChild(columnaId);
  fila.appendChild(columnaCorreo);
  fila.appendChild(columnaNombre);
  fila.appendChild(columnaApellido);
  console.log(fila);
  usuarios.innerHTML = usuarios.innerHTML + fila.innerHTML;

  fetch("http://127.0.0.1:5000/listar-usuarios", {
    method: "GET",
  })
    .then((respuesta) => {
      // esto sucedera si todo esta bien
      console.log("Todo bien");
      return respuesta.json();
    })
    .then((resultado) => {
      console.log(resultado.content);
      resultado.content.forEach((elemento) => {
        // TODO: realizar el llenado de la tabla con los usuarios devueltos por el backend
        console.log(elemento);
      });
    })
    .catch((error) => {
      // esto sucedera si hubo un error
      console.log(error);
    });
}

addUser.addEventListener("click", addUserClick);
getUser.addEventListener("click", getUserClick);
