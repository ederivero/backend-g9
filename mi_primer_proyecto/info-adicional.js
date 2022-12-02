const nombre = "eduardo";
const edad = 30;

const saludar = (nombre) => {
  return `Hola ${nombre}`;
};

// Esta es la forma de exportar variables, funciones, lo que sea usando el formato CommonJs
module.exports = {
  nombre: nombre,
  edad: edad,
  saludar: saludar,
};
