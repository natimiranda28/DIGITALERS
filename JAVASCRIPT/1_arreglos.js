/* 
A partir del siguiente array:
let nombres = ["Juan", "Pedro", "Maria", "Jose", "Rubén", "Kevin"];
Preguntar al usuario que ingrese un nuevo nombre.
Si ya existe en el array, mostrar un console.warn en la consola que diga "El nombre ya existe".
Si no existe, agregarlo al array y mostrar el array completo con console.table().
*/

let nombres = ["Juan", "Pedro", "Maria", "Jose", "Rubén", "Kevin"];
let nuevoNombre = prompt("Ingrese un nuevo nombre:");
if (nombres.includes(nuevoNombre)) {
    console.warn("El nombre ya existe");
}
else {
    nombres.push(nuevoNombre);
    console.table(nombres);
}       
