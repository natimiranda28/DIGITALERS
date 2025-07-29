
/* 
Crear un programa que pida al usuario ingresar su nombre
Si el nombre es el mismo que el tuyo, saludarlo con un alert().
Si no, decirle "No conozco a " + nombre. 
*/

let myName = "Natalia"; 
let userName = prompt("Por favor, ingresa tu nombre:");
if (userName === myName) {
    alert("¡Hola " + myName + "!");
}   else {
    alert("No conozco a " + userName + ".");
}                                                               

