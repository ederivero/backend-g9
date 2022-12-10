import { Router } from "express";
import { crearPedido } from "../controllers/pedidos.controller.js";

export const pedidosRouter = Router();

pedidosRouter.post("/pedido", crearPedido);
