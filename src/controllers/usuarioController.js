import { Usuario } from "../models/usuarioModel.js";

export function registro(req, res) {
  const data = req.body;
  console.log(data);

  res.status(201).json({
    message: "Usuario creado exitosamente",
  });
}
