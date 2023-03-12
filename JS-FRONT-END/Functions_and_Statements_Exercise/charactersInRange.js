function solve(...chars) {
    let codes = [];
    chars.forEach((chars) => {
        let index = chars.charCodeAt()
        codes.push(index)
    });
    let result = [];
    if(codes[0] < codes[1]){
        for (let i = codes[0] + 1; i < codes[1]; i++) {
            let char = String.fromCharCode(i)
            result.push(char)
        }
    }else{
        for (let i = codes[1] + 1; i < codes[0]; i++) {
            let char = String.fromCharCode(i)
            result.push(char)
        }
    }
    console.log(result.join(' '))
}

solve('C',
'#')