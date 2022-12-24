import express from "express";
import mongoose from "mongoose";
mongoose.set("strictQuery", false);
mongoose.connect(process.env.MONGO_URI, {});

import { Usuario } from "./models/usuarioModel.js";
import { Agenda } from "./models/agendaModel.js";
import { agendaRouter } from "./routes/agendaRoute.js";
import { usuarioRouter } from "./routes/usuarioRoute.js";
import { imagenRouter } from "./routes/imagenRoute.js";
import { v2 } from "cloudinary";

v2.config({
  secure: true,
});
console.log(v2.config());
const server = express();
const PORT = process.env.PORT ?? 5000;

// aca indicamos que la aplicacion entendera los json's provenientes del cliente
server.use(express.json());

// indicamos que usaremos un conjunto de rutas
server.use(usuarioRouter);
server.use(agendaRouter);
server.use(imagenRouter);

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
