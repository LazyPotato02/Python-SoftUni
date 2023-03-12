function movieShows(movies) {
    let movieDict = {};
    for (const movie of movies) {
        if (movie.includes('addMovie')) {
            let mov = movie.split(' ')
            mov.shift()
            mov = mov.join(' ')
            movieDict[mov] = {}
            movieDict[mov].name = mov
        } else if (movie.includes('directedBy')) {
            let indexOfCommand = movie.indexOf('directedBy') // + 9
            let movieName = movie.slice(0, indexOfCommand - 1)
            let directorName = movie.slice(indexOfCommand + 11)
            if (movieName in movieDict) {
                movieDict[movieName].director = directorName
            }
        } else if (movie.includes('onDate')) {
            let indexOfCommand = movie.indexOf('onDate') // + 5
            let movieName = movie.slice(0, indexOfCommand - 1)
            let movieDate = movie.slice(indexOfCommand + 7)
            if (movieName in movieDict) {
                movieDict[movieName].date = movieDate
            }
        }
    }
    for (const movieDictKey in movieDict) {
        let movie = movieDict[movieDictKey]
        if (movie.name && movie.director && movie.date)
            console.log(JSON.stringify(movieDict[movieDictKey]))
    }
    // console.log(movieDict)
}

movieShows([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
])
movieShows(
    [
        'addMovie The Avengers',
        'addMovie Superman',
        'The Avengers directedBy Anthony Russo',
        'The Avengers onDate 30.07.2010',
        'Captain America onDate 30.07.2010',
        'Captain America directedBy Joe Russo'
    ]
)