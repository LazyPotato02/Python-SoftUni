function employees(employees) {
    let obj = {}
    for (let info of employees) {
        obj.name = info;
        obj.num = info.length;
        console.log(`Name: ${obj.name} -- Personal Number: ${obj.num}`);
    }
}


employees([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ]
    )