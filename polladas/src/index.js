import express, { json } from "express";
import { clientesRouter } from "./routes/clientes.routes.js";
import { pedidosRouter } from "./routes/pedidos.routes.js";
import { productosRouter } from "./routes/productos.routes.js";

const servidor = express();
// para que cuando me envien Body en formato JSON express lo pueda leer y transformar a un formato legible
servidor.use(json());
// variable de entorno en formato JSON
// Nullish coalescing operator > https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing
const PORT = process.env.PORT ?? 5000;

servidor.use(productosRouter);
servidor.use(clientesRouter);
servidor.use(pedidosRouter);

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
