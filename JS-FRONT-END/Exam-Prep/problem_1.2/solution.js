function solve(input) {
    let shoppingList = input.shift().split('!')

    let commandParser = {
        'Urgent': urgent,
        'Unnecessary': unnecessary,
        'Correct': correct,
        'Rearrange': rearrange,
    }

    while (true) {
        let commandInput = input.shift()


        if (commandInput === 'Go Shopping!') {
            break
        }
        commandInput = commandInput.split(' ')
        let command = commandInput.shift()
        let values = commandInput
        commandParser[command](values)
    }

    function urgent(input) {
        let value = input.toString()
        if (!(shoppingList.includes(value))) {
            shoppingList.unshift(value)
        }
    }

    function unnecessary(input) {
        let value = input.toString()
        if (shoppingList.includes(value)) {
            let valueIndex = shoppingList.indexOf(value)
            shoppingList = shoppingList.filter(object => {
                return object !== value
            })
        }
    }

    function correct(input) {
        let value = input.shift()
        let replaceValue = input.shift()
        if (shoppingList.includes(value)) {
            let index = shoppingList.indexOf(value)
            shoppingList[index] = replaceValue
        }

    }

    function rearrange(input) {
        let value = input.toString()

        if (shoppingList.includes(value)) {
            let valueIndex = shoppingList.indexOf(value)
            shoppingList = shoppingList.filter(object => {
                return object !== value
            })
            shoppingList.push(value)
        }
    }

    console.log(shoppingList.join(', '))
}

// solve(
//     (
//         ["Tomatoes!Potatoes!Bread",
//             "Urgent Milk",
//             "Unnecessary Milk",
//             "Urgent Tomatoes",
//             "Go Shopping!"]
//     )
// )
solve((["Milk!Pepper!Salt!Water!Banana",
    "Urgent Salt",
    "Unnecessary Grapes",
    "Correct Pepper Onion",
    "Rearrange Grapes",
    "Correct Tomatoes Potatoes",
    "Go Shopping!"])
)