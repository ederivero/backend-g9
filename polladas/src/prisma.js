import prisma from "@prisma/client";
// La conexion a nuestra base de datos

// Usando el patron singleton solamente generamos una conexion para todo nuestro proyecto
export const Prisma = new prisma.PrismaClient();
