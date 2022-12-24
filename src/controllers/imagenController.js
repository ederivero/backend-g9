import path from "path";
import fs from "fs";
import { v2 } from "cloudinary";

export async function subirImagen(req, res) {
  console.log(req.file);

  res.json({
    message: "Imagen subida exitosamente",
  });
}

export async function devolverImagen(req, res) {
  // query params http://localhost:5000/devolver-imagen?nombre=mi-imagen.png
  const { nombre, extension } = req.query;

  // devolvera la ubicacion de nuestro archivo package.json dentro del servidor o maquina
  const __dirname = path.resolve();
  console.log(__dirname);
  const nombreCompleto = `${nombre}.${extension}`;

  // el metodo join sirve para colocar la ubicacion que queremos y el se encargara de colocar el '/' o el '\' dependiendo del sistema operativo
  const rutaArchivo = path.join(__dirname, "imagenes", nombreCompleto);
  console.log(rutaArchivo);
  try {
    // Sirve para leer un archivo, si no lo encuentra emitira un error
    fs.readFileSync(rutaArchivo);

    res.sendFile(rutaArchivo);
  } catch (error) {
    res.status(404).json({
      message: "Archivo no existe",
    });
  }
}

export function eliminarImagen(req, res) {
  const { nombre, extension } = req.query;

  const __dirname = path.resolve();
  const nombreCompleto = `${nombre}.${extension}`;
  const rutaArchivo = path.join(__dirname, "imagenes", nombreCompleto);

  try {
    // Elimina el archivo de manera sincrona (lineal) si no lo encuentra emitira un error
    fs.unlinkSync(rutaArchivo);
    res.json({
      message: "Imagen eliminada exitosamente",
    });
  } catch (error) {
    res.status(404).json({
      message: "Archivo no existe",
    });
  }
}

//----------------------------------------- AHORA CON CLOUDINARY

export async function subirImagenCloudinary(req, res) {
  const archivo = req.file;
  const __dirname = path.resolve();
  const rutaArchivo = path.join(__dirname, archivo.path);
  console.log(archivo);
  try {
    const resultado = await v2.uploader.upload(
      archivo.path,
      {
        use_filename: true,
        unique_filename: false,
        overwrite: true,
      },
      (err) => {
        if (err) {
          console.log(err);
        }
      }
    );

    res.json({
      message: "Archivo subido exitosamente",
    });
  } catch (error) {
    console.log(error);
    res.json({
      message: "error al subir la imagen",
    });
  }
}
