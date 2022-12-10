import { Prisma } from "../prisma.js";

export const crearProducto = async (req, res) => {
  const data = req.body; // {nombre: '...', precio: ..., cantidad: ... , disponibilidad: ...}
  try {
    // Todas las operaciones que se realiza en Prisma son operaciones asincronas
    const nuevoProducto = await Prisma.producto.create({
      data, // data: data
      // {
      //   nombre: data.nombre,
      //   precio: data.precio,
      //   cantidad: data.cantidad,
      //   disponibilidad: data.disponibilidad,
      // },
    });

    console.log("hola");

    res.status(201).json({
      message: "producto creado exitosamente",
      content: nuevoProducto,
    });
  } catch (error) {
    res.status(400).json({
      message: "Error al crear el producto",
      error: error.message,
    });
  }
};

export const listarProductos = async (req, res) => {
  try {
    const productos = await Prisma.producto.findMany();
    return res.status(200).json({
      message: "Productos encontrados",
      content: productos,
    });
  } catch (error) {
    return res.status(500).json({
      message: "Error en el servidor",
      error: error.message,
    });
  }
};

export const traerProductoPorId = async (req, res) => {
  const { id } = req.params;
  try {
    const producto = await Prisma.producto.findUnique({
      where: {
        id: Number(id),
      },
    });
    if (!producto) {
      return res.status(404).json({
        message: "Producto no encontrado",
      });
    }
    return res.status(200).json({
      message: "Producto encontrado",
      content: producto,
    });
  } catch (error) {
    return res.status(500).json({
      message: "Error en el servidor",
      error: error.message,
    });
  }
};

export const actualizarProducto = async (req, res) => {
  const { id } = req.params;
  const data = req.body;
  try {
    const findProduct = await Prisma.producto.findUnique({
      where: {
        id: Number(id),
      },
    });
    if (!findProduct) {
      return res.status(404).json({
        message: "Producto no encontrado",
      });
    }
    const producto = await Prisma.producto.update({
      where: {
        id: Number(id),
      },
      data: {
        nombre: data.nombre,
        cantidad: data.cantidad,
        precio: data.precio,
        disponibilidad: data.disponibilidad,
      },
      select: {
        nombre: true,
        cantidad: true,
        precio: true,
      },
    });

    return res.status(201).json({
      message: "Producto actualizado",
      content: producto,
    });
  } catch (error) {
    return res.status(500).json({
      message: "Error en el servidor",
      error: error.message,
    });
  }
};
