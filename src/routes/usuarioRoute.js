import { Router } from "express";
import { registro, login } from "../controllers/usuarioController.js";

export const usuarioRouter = Router();

usuarioRouter.post("/registro", registro);
usuarioRouter.post("/login", login);
