function birthdayCountDown(){
    var day = 60;
    while (day > 30){
        console.log(day + " days until my birthday. Such a long time... :(");
        day--;
    }
    while (day > 5){
        console.log(day + " days until my birthday. Amost my Birthday!!");
        day--;
    }
    while (day >= 1){
        console.log(day + " DAYS UNTIL MY BIRTHDAY!!!!");
        day--;
    }
    console.log("HAPPY BIRTHDAY!!!!!!!");
}

console.log(birthdayCountDown());
