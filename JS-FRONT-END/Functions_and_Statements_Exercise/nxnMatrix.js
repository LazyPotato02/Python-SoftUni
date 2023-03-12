function solve(num){
    let arr = new Array(num).fill(new Array(num).fill(num))
    return arr.forEach(row => console.log(row.join(' ')))
}
solve(3)