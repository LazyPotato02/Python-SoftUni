function solve(dayType, age) {
    let result;

    if (age >= 0 && age <= 18) {
        switch (dayType) {
            case 'Weekday': result = 12; break;
            case 'Weekend': result = 15; break;
            case 'Holiday': result = 5; break;
        }
    } else if (age > 18 && age <= 64) {
        switch (dayType) {
            case 'Weekday': result = 18; break;
            case 'Weekend': result = 20; break;
            case 'Holiday': result = 12; break;
        }
    } else if (age > 64 && age <= 122) {
        switch (dayType) {
            case 'Weekday': result = 12; break;
            case 'Weekend': result = 15; break;
            case 'Holiday': result = 10; break;
        }
    }
    if(result){
        console.log(`${result}$`)
    }else{
        console.log('Error!')
    }
}
solve(
    'Holiday', -12
    )