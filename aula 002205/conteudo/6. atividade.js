const readlineSync = require('readline-sync')

let listName = []
let contadorSalario = 0
let contadorIdade = 0
for (i = 1; i <= 2; i++) {
    let nome = readlineSync.question("Insira seu nome: ")
    let idade = parseInt(readlineSync.question("Insira sua idade: "))
    let salario = parseFloat(readlineSync.question("Insira seu salário: "))
    contadorSalario = contadorSalario + salario
    contadorIdade = contadorIdade + idade
    listName.push(nome)
}

mediaIdade = contadorIdade / 2
mediaSalarial = contadorSalario / 2

for (nome of listName) {
    console.log(`Nomes: ${nome}`)
}
console.log(`A média salarial é: ${mediaSalarial}`)
console.log(`A média etária é: ${mediaIdade}`)