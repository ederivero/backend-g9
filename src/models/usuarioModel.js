import mongoose from "mongoose";

const direccionSchema = new mongoose.Schema(
  {
    calle: mongoose.Schema.Types.String,
    numero: mongoose.Schema.Types.String,
    codigoPostal: {
      alias: "codigo_postal", // indicar como se llamara esta columna en la bd
      type: mongoose.Schema.Types.String,
    },
  },
  {
    _id: false, // esto solo se puede dar en sub documentos
  }
);

const usuarioSchema = new mongoose.Schema(
  {
    nombre: {
      type: mongoose.Schema.Types.String,
      required: true,
    },
    email: {
      type: mongoose.Schema.Types.String,
      unique: true,
      required: true,
    },
    password: {
      type: mongoose.Schema.Types.String,
      required: true,
    },
    direcciones: [direccionSchema],
  },
  {
    // https://mongoosejs.com/docs/guide.html#options
    timestamps: {
      createdAt: "fechaCreacion",
      updatedAt: "fechaActualizacion",
    },
  }
);

export const Usuario = mongoose.model("usuarios", usuarioSchema);
