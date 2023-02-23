function solve(arr) {
    let evenSum = 0;
    let oddSum = 0
    for (let i = 0; i < arr.length; i++) {
        let n = Number(arr[i])
        if (n % 2 === 0){
            evenSum += n
        }else{
            oddSum += n
        }
    }; 
    let result = evenSum - oddSum

    console.log(result)
}
solve([3,5,7,9])