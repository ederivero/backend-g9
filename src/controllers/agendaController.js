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

export async function listarAgenda(req, res) {
  const usuarioId = req.user._id;

  // left outer join utilizando lo que vendria a hacer una clausula condicional cuando concuerde que solamente muestre las agendas de ese usuario
  const agendas = await Agenda.aggregate([
    {
      $match: { usuario: usuarioId },
    },
  ]).lookup({
    from: "usuarios", // aca va el nombre de la coleccion, NO EL NOMBRE DEL MODELO
    localField: "usuario", // la columna de la tabla agenda que usaremos
    foreignField: "_id", // la columna de la tabla usuarios que usaremos para la relacion
    as: "propietario", // en que columna se mostrara este join
  });

  console.log(agendas);
  res.json({
    content: agendas,
  });
}
