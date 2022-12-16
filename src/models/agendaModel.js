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
  },
  horaFin: {
    type: mongoose.Schema.Types.String,
    required: true,
    alias: "hora_fin",
  },
});
