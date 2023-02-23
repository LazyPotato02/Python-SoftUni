function solve(revertPoint,arr){
    let result=[];
    for (let i = revertPoint -1; i >=0;i-- ){
        result.push(arr[i]);
    }
    console.log(result.join(' '))
}
solve(3, [10, 20, 30, 40, 50]
    )