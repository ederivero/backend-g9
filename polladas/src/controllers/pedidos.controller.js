import { Prisma } from "../prisma.js";

export const crearPedido = async (req, res) => {
  const data = req.body;
  try {
    const pedidos = await Prisma.cabeceraPedido.create({
      data: {
        clienteId: data.clienteId,
        fechaEmision: data.fechaEmision,
        detalles: {
          create: data.pedidoDetalle,
        },
      },
      select: {
        clienteId: true,
        fechaEmision: true,
        detalles: {
          select: {
            id: true,
            cantidad: true,
            producto: {
              select: {
                id: true,
                nombre: true,
              },
            },
            valorVenta: true,
          },
        },
      },
    });

    return res.status(201).json({
      message: "Pedido registrado",
      content: pedidos,
    });
  } catch (error) {
    return res.status(500).json({
      message: "Error en el servidor",
      error: error.message,
    });
  }
};
