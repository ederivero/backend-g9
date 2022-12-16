import { Usuario } from "../models/usuarioModel.js";
import bcryptjs from "bcryptjs";
import jwt from "jsonwebtoken";

export async function registro(req, res) {
  const data = req.body;
  console.log(data);

  try {
    // generamos el hash de la contraseña del usuario
    const password = bcryptjs.hashSync(data.password, 10);

    const nuevoUsuario = await Usuario.create({ ...data, password });

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

export async function login(req, res) {
  const data = req.body; // {email: '...', password: '...'}
  const usuarioEncontrado = await Usuario.findOne({ email: data.email });

  if (!usuarioEncontrado) {
    return res.status(404).json({
      message: "El usuario no existe",
    });
  }

  if (bcryptjs.compareSync(data.password, usuarioEncontrado.password)) {
    // es la contraseña del usuario
    const payload = {
      jti: usuarioEncontrado._id,
      nombre: usuarioEncontrado.nombre,
    };

    const token = jwt.sign(payload, process.env.JWT_SECRET, {
      expiresIn: "1h",
    });

    res.json({
      message: "Bienvenido",
      content: token,
    });
  } else {
    res.json({
      message: "Error al ingresar, la contraseña no es valida",
    });
  }
}

export async function perfil(req, res) {
  console.log(req.user);
  // seleccionamos solamente el nombre del usuario indicando las columnas separadas por espacio y la que no se le coloca un signo negativo (-)
  const usuarioEncontrado = await Usuario.findById(req.user._id).select(
    "nombre email direcciones" // -_id"
  );

  res.json({
    content: usuarioEncontrado,
  });
}
