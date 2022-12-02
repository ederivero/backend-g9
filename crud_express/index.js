import express, { json } from "express";

const servidor = express();
// use > sirve para agregar un middleware que validara la informacion dependiendo el orden en el que lo coloquemos
// llegue informacion en formato JSON este middleware lo pueda convertir en una informacion legible y lo almacene en el req.body
servidor.use(json());
const productos = [
  {
    nombre: "pollada",
    precio: 15.5,
    disponible: true,
  },
  {
    nombre: "adobada",
    precio: 15.5,
    disponible: true,
  },
  {
    nombre: "chichorranada",
    precio: 17.5,
    disponible: true,
  },
  {
    nombre: "chuleteada",
    precio: 12.5,
    disponible: false,
  },
];

servidor.get("/", (req, res) => {
  console.log("Entro aqui");

  res.status(200).json({
    message: "Bienvenido a mi API de express",
  });
});

servidor
  .route("/productos")
  .get((req, res) => {
    // devuelve todos los productos que esten disponible solo puedes utilizar el metodo filter
    const productoDisponibles = productos.filter((producto) => {
      return producto.disponible === true;
    });

    res.status(200).json({
      content: productoDisponibles,
    });
  })
  .post((req, res) => {
    console.log(req.body);
    const data = req.body;

    productos.push(data);

    res.status(201).json({
      message: "Producto creado exitosamente",
    });
  });

servidor.listen(5000, () => {
  console.log(`Servidor corriendo exitosamente en el puerto 5000`);
});
