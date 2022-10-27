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
}

addUser.addEventListener("click", addUserClick);
getUser.addEventListener("click", getUserClick);
