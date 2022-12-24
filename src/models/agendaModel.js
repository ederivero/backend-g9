import mongoose from "mongoose";

const agendaSchema = new mongoose.Schema({
  asunto: {
    type: mongoose.Schema.Types.String,
    required: true,
    maxlength: 100,
  },
  dia: {
    type: mongoose.Schema.Types.Date,
    required: true,
  },
  horaInicio: {
    type: mongoose.Schema.Types.String,
    required: true,
    alias: "hora_inicio",
    validate: {
      validator: (valor) => {
        return /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/.test(valor);
      },
      message: "Error, el formato debe ser HH:MM",
    },
  },
  horaFin: {
    type: mongoose.Schema.Types.String,
    required: true,
    alias: "hora_fin",
    validate: {
      validator: (valor) => {
        return /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/.test(valor);
      },
      message: "Error, el formato debe ser HH:MM",
    },
  },
  // es una columna que servira para hacer la relacion a nivel de mongoose para poder vincular la agenda con el usuario
  usuario: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "Usuario",
  },
  imagen: {
    type: mongoose.Schema.Types.String,
  },
});

export const Agenda = mongoose.model("agendas", agendaSchema);
