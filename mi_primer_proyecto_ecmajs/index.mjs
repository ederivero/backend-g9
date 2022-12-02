// Formato de importacion usando ECMAscript
import isodd from "is-odd";
import { edad, nacionalidad, saludar } from "./herramientas.mjs";

const resultado = isodd(15);
console.log(resultado);

console.log(edad);

const saludo = saludar("juan");
console.log(saludo);
