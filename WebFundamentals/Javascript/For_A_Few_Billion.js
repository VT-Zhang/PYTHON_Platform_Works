function forAFewBillon(){
    var reward = 0.01;
    for (var i = 1; i < 31; i++){
        reward = reward * 2;
    }
    return reward;
}
console.log(forAFewBillon());


function makeAFortune(money){
    var reward = 0.01;
    var day = 1;
    while (reward <= money){
        reward = reward * 2;
        day++;
    }
    return day;
}
console.log(makeAFortune(10000));
console.log(makeAFortune(1000000000));
console.log(makeAFortune(Infinity));
