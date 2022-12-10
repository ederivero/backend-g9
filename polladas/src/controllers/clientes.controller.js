import { Prisma } from "../prisma.js";

export const crearCliente = async (req, res) => {
  const data = req.body;
  try {
    const cliente = await Prisma.cliente.create({
      data,
    });
    return res.status(201).json({
      message: "Cliente creado",
      content: cliente,
    });
  } catch (error) {
    return res.status(500).json({
      message: "Error en el servidor",
      error: error.message,
    });
  }
};

export const listarClientes = async (req, res) => {
  try {
    const clientes = await Prisma.cliente.findMany();
    return res.status(200).json({
      message: "Lista clientes",
      content: clientes,
    });
  } catch (error) {
    return res.status(500).json({
      message: "Erro inesperado",
      error: error.message,
    });
  }
};

export const traerClientePorId = async (req, res) => {
  const { id } = req.params;
  try {
    const cliente = await Prisma.cliente.findUnique({
      where: {
        id: Number(id),
      },
    });
    if (!cliente) {
      return res.status(404).json({
        message: "Cliente no encontrado",
      });
    }

    return res.status(200).json({
      message: "Cliente encontrado",
      content: cliente,
    });
  } catch (error) {
    return res.status(500).json({
      message: "Erro inesperado",
      error: error.message,
    });
  }
};

export const actualizarCliente = async () => {
  const { id } = req.params;
  const data = req.body;
  try {
    const findCliente = await Prisma.cliente.findUnique({
      where: {
        id: Number(id),
      },
    });
    if (!findCliente) {
      return res.status(404).json({
        message: "Cliente no encontrado",
      });
    }

    const cliente = await Prisma.cliente.update({
      data,
    });
    return res.status(201).json({
      message: "Cliente actualizado",
      content: cliente,
    });
  } catch (error) {
    return res.status(500).json({
      message: "Erro inesperado",
      error: error.message,
    });
  }
};

export const eliminarCliente = async (req, res) => {
  const { id } = req.params;
  try {
    const findCliente = await Prisma.cliente.findUnique({
      where: {
        id: Number(id),
      },
    });
    if (!findCliente) {
      return res.status(404).json({
        message: "Cliente no encontrado",
      });
    }
    const cliente = await Prisma.cliente.delete({
      where: {
        id: Number(id),
      },
    });

    return res.status(200).json({
      message: "Cliente eliminado",
    });
  } catch (error) {
    return res.status(500).json({
      message: "Erro inesperado",
      error: error.message,
    });
  }
};
