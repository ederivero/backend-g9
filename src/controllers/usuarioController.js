import { Usuario } from "../models/usuarioModel.js";

export async function registro(req, res) {
  const data = req.body;
  console.log(data);

  try {
    const nuevoUsuario = await Usuario.create(data);
    console.log(nuevoUsuario);

    res.status(201).json({
      message: "Usuario creado exitosamente",
    });
  } catch (error) {
    res.status(500).json({
      message: "Error al crear el usuario",
      content: error.message,
    });
  }
}
