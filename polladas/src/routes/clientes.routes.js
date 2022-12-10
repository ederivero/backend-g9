import { Router } from "express";
import {
  actualizarCliente,
  crearCliente,
  eliminarCliente,
  listarClientes,
  traerClientePorId,
} from "../controllers/clientes.controller.js";

export const clientesRouter = Router();

clientesRouter.post("/cliente", crearCliente);
clientesRouter.get("/cliente", listarClientes);
clientesRouter.get("/cliente/:id", traerClientePorId);
clientesRouter.put("/cliente/:id", actualizarCliente);
clientesRouter.delete("/cliente/:id", eliminarCliente);
