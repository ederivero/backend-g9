import express, { json } from "express";

const servidor = express();
// para que cuando me envien Body en formato JSON express lo pueda leer y transformar a un formato legible
servidor.use(json());
// variable de entorno en formato JSON
// Nullish coalescing operator > https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing
const PORT = process.env.PORT ?? 5000;

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
