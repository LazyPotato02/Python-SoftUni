function wordTracker(input) {
    let searchWords = input.shift().split(' ')
    let founds = {}
    for (const searchWord of searchWords) {
        founds[searchWord] = 0
    }
    for (const searchWord of searchWords) {
        for (const word of input) {
            if (searchWord === word) {
                founds[searchWord]++
            }
        }
    }
    const sortedObj = Object.fromEntries(
        Object.entries(founds)
            .sort(([, val1], [, val2]) => val2 - val1)
    );
    for (const sortedObjKey in sortedObj) {
        console.log(`${sortedObjKey} - ${sortedObj[sortedObjKey]}`)
    }
}

wordTracker([
    'this sentence',
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
])
wordTracker([
    'is the',
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence'])