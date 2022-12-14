import mongoose from "mongoose";
import express from "express";

const productoSchema = new mongoose.Schema({
  // todas las columnas que se guardaran en esta coleccion
  // https://mongoosejs.com/docs/schematypes.html#schematype-options
  nombre: {
    type: mongoose.Schema.Types.String,
    unique: true, // que el nombre jamas se puede repetir,
    maxLength: 50,
    required: true, // es requerido si o si
  },
  precio: {
    type: mongoose.Schema.Types.Decimal128,
    max: 100.0,
  },
});

const Producto = mongoose.model("productos", productoSchema);

const servidor = express();

const PORT = process.env.PORT ?? 5000;

servidor.listen(PORT, async () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
  try {
    await mongoose.connect("mongodb://127.0.0.1:27017/express");
    console.log("Conexion a la base de datos exitosa 🔌");
  } catch (e) {
    console.log(e);
    console.log("Error al conectarse a la base de datos");
  }
});
