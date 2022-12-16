import { Router } from "express";
import { registro, login, perfil } from "../controllers/usuarioController.js";
import { vigilante } from "../utils/wachiman.js";
export const usuarioRouter = Router();

usuarioRouter.post("/registro", registro);
usuarioRouter.post("/login", login);
usuarioRouter.get("/perfil", vigilante, perfil);
