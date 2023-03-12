function addAndSubtract(firstNum, secondNum, thirdNum) {

    function sum(num1, num2) {
        return num1 + num2
    }

    let result = sum(firstNum, secondNum)

    function subtract(result, num3) {
        return result - num3
    }

    result = subtract(result, thirdNum)
    console.log(result)
}

addAndSubtract(1,
17,
30)