function towns(towns){

    for (const town of towns) {
        let city = {};
        let townString = town.split(' | ')
        city.town = townString[0]
        city.latitude = Number(townString[1]).toFixed(2)
        city.longitude = Number(townString[2]).toFixed(2)
        console.log(city)
    }
}

towns(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625']
)