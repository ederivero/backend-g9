import { Router } from "express";
import {
  subirImagen,
  devolverImagen,
  eliminarImagen,
  subirImagenCloudinary,
} from "../controllers/imagenController.js";
import Multer from "multer";

// es un middleware que agarra y vera si hay archivos y si los hay los agregara al req.file o req.files
const multer = Multer({
  storage: Multer.diskStorage({
    destination: (req, file, cb) => {
      cb(null, "./imagenes");
    },
    filename: (req, file, cb) => {
      const horaActual = new Date().getTime();
      cb(null, `${horaActual}-${file.originalname}`);
    },
  }),
  limits: {
    // sirve para indicar el tamaño maximo de los archivos se expresa en bytes
    // 1 byte * 1024 = 1 kilobyte * 1024 = 1 megabyte (Mb) * 1024 = 1 Gigabyte (Gb)
    fileSize: 5 * 1024 * 1024,
  },
});
export const imagenRouter = Router();

// single(nombre) > acepta un solo archivo con el nombre de la llave como parametro
// array(nombre) > acepta un array de archivos (osea varios) mediante el nombre de la llave y en este caso se guardara en req.files en todos lo demas casos se guardara en req.file
// fields(nombre) > acepta una mezcla de archivos especificados por las llaves y se le puede colocar cuantos archivos como maximo me puede enviar
// none() > No acepta archivos sino solamente puro texto si se le envia un archivo entonces lanzara un error
// any() > acepta todos los archivos que puedan venir en cualquier llave y estos seran almacenados en req.files

imagenRouter.post("/subir-imagen", multer.single("imagen"), subirImagen);

imagenRouter.get("/devolver-imagen", devolverImagen);

imagenRouter.delete("/eliminar-imagen", eliminarImagen);

imagenRouter.post(
  "/subir-imagen-cd",
  multer.single("imagen"),
  subirImagenCloudinary
);
