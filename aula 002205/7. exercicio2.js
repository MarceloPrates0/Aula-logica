const readlineSync = require('readline-sync')

let testArray = []

for (i = 1; i <= 3; i++) {
    let numero = parseInt(readlineSync.question("Insira um número: "))
    testArray.push(numero)
}

console.log(testArray)