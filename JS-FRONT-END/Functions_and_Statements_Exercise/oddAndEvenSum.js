function solve(number) {
    let numberString = String(number).split('')
    let splittedNumber = numberString.map(function (item) {
        return parseInt(item)
    });
    // console.log(splittedNumber)
    let oddSum = 0;
    let evenSum = 0;

    for (const numberElement of splittedNumber) {
        if (Number((numberElement) % 2 === 0)){
            evenSum += numberElement
        }else{
            oddSum += numberElement
        }
    }
    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`)
}

solve(3495892137259234)