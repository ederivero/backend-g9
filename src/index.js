import express from "express";
import mongoose from "mongoose";
import { usuarioRouter } from "./routes/usuarioRoute.js";
import { agendaRouter } from "./routes/agendaRoute.js";
const server = express();
const PORT = process.env.PORT ?? 5000;

// aca indicamos que la aplicacion entendera los json's provenientes del cliente
server.use(express.json());

// indicamos que usaremos un conjunto de rutas
server.use(usuarioRouter);
server.use(agendaRouter);

server.listen(PORT, async () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
  try {
    mongoose.set("strictQuery", false);
    await mongoose.connect(process.env.MONGO_URI, {});

    console.log("Conexion exitosa a la bd");
  } catch (error) {
    console.log("Error al conectarse a la base de datos");
  }
});
