import { Agenda } from "../models/agendaModel.js";

export async function crearAgenda(req, res) {
  const data = req.body;
  const usuarioId = req.user._id;
  try {
    const agendaCreada = await Agenda.create({ ...data, usuario: usuarioId });

    res.status(201).json({
      message: "Agenda creada exitosamente",
      content: agendaCreada,
    });
  } catch (error) {
    // aca ingresara si hay algun error ya sea por la validacion o por que el usuario no existe
    res.status(400).json({
      message: "Error al crear la agenda",
      content: error.message,
    });
  }
}
