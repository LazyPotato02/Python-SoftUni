function solve(percent) {
    let done = percent / 10
    let doneString = '%'
    let notDoneString = '.'
    let notDone = (100 - percent) / 10
    console.log(`${percent}% [${doneString.repeat(done)}${notDoneString.repeat(notDone)}]`)
    console.log('Still loading...')
}
solve(30)