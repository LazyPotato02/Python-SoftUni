function solve(number){
    for (let numberElement of number) {
        let numberString = String(numberElement).split('')
        let splittedNumber = numberString.map(function (item) {
            return parseInt(item)
        });
        let reversedNumber = Number(splittedNumber.reverse().join(''))
        if (numberElement === reversedNumber){
            console.log('true')
        }else{
            console.log('false')
        }
    }
}
solve([32,2,232,1010])