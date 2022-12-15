import { Router } from "express";
import { registro } from "../controllers/usuarioController.js";

export const usuarioRouter = Router();

usuarioRouter.post("/registro", registro);
