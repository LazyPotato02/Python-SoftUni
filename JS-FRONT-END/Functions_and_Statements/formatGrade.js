function solve(grade) {
    if (grade >= 5.50) {
        return `Excellent (${grade.toFixed(2)})`
    } else if (grade >= 4.50 && grade < 5.50) {
        return `Very good (${grade.toFixed(2)})`
    } else if(grade >= 3.50 && grade < 4.50){
        return `Good (${grade.toFixed(2)})`
    } else if(grade >= 3 && grade < 3.50){
        return `Poor (${grade.toFixed(2)})`
    } else{
        return `Fail (${grade})`
    }
}

console.log(solve(2.99))