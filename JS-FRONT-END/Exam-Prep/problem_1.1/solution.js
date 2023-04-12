function solve(input) {
    let index = input.shift()
    let piecesCollection = {}

    let commandParser = {
        'Add': add,
        'Remove': remove,
        'ChangeKey': changeKey,
    }

    for (let i = 0; i < index; i++) {
        let pieceInput = input.shift().split('|')
        let pieceName = pieceInput[0]
        let compositorName = pieceInput[1]
        let key = pieceInput[2]
        piecesCollection[pieceName] = {compositorName, key}
    }
    while (true) {
        let values = input.shift()


        if (values === 'Stop') {
            break
        }
        values = values.split('|')
        let command = values.shift()
        let value = [...values]


        commandParser[command](value)
    }

    function add(input) {
        let pieceName = input[0]
        let compositorName = input[1]
        let key = input[2]

        if (pieceName in piecesCollection) {
            console.log(`${pieceName} is already in the collection!`)
        } else {
            console.log(`${pieceName} by ${compositorName} in ${key} added to the collection!`)
            piecesCollection[pieceName] = {compositorName, key}
        }

    }

    function remove(input) {
        let pieceName = input[0]

        if (pieceName in piecesCollection) {
            delete piecesCollection[pieceName]
            console.log(`Successfully removed ${pieceName}!`)
        } else {
            console.log(`Invalid operation! ${pieceName} does not exist in the collection.`)
        }
    }

    function changeKey(input) {
        let pieceName = input[0]
        let key = input[1]

        if (pieceName in piecesCollection) {
            piecesCollection[pieceName].key = key
            console.log(`Changed the key of ${pieceName} to ${key}!`)
        } else {
            console.log(`Invalid operation! ${pieceName} does not exist in the collection.`)
        }

    }

    for (const piecesCollectionElement in piecesCollection) {
        console.log(`${piecesCollectionElement} -> Composer: ${piecesCollection[piecesCollectionElement].compositorName}, Key: ${piecesCollection[piecesCollectionElement].key}`)
    }
}

solve([
    '3',
    'Fur Elise|Beethoven|A Minor',
    'Moonlight Sonata|Beethoven|C# Minor',
    'Clair de Lune|Debussy|C# Minor',
    'Add|Sonata No.2|Chopin|B Minor',
    'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
    'Add|Fur Elise|Beethoven|C# Minor',
    'Remove|Clair de Lune',
    'ChangeKey|Moonlight Sonata|C# Major',
    'Stop'
])