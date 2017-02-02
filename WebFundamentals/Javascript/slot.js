function slot1(){
    var quarter = 100;
    var pick = 1;
    var num = 0;
    var reward = 0;
    while (quarter != 0){
        quarter--;
        num = Math.floor(Math.random() * 100);
        if (pick == num){
            reward = Math.trunc(Math.random() * 50) + 50;
            quarter = quarter + reward;
            console.log(quarter);
            break;
        }
    }
    return 0;
}
console.log(slot1());



function slot2(max){
    var quarter = 100;
    var pick = 1;
    var num = 0;
    var reward = 0;
    while (quarter < max){
        quarter--;
        num = Math.floor(Math.random() * 100);
        if (pick == num){
            reward = Math.trunc(Math.random() * 50) + 50;
            quarter = quarter + reward;
        }
        if (quarter == 0){
            console.log('The player is out of quarters.');
            break;
        }

    }
    console.log('The player left with ' + quarter + " quarters.")
}
console.log(slot2(200));





function slot3(){
    var quarter = 50;
    var pick = 1;
    var num = 0;
    var reward = 0;
    var counter1 = 0;
    var counter2 = 0;
    while (quarter != 0){
        quarter--;
        counter2++;
        num = Math.floor(Math.random() * 100);
        if (pick == num){
            reward = Math.trunc(Math.random() * 50) + 50;
            quarter = quarter + reward;
            counter1++;
        }
    }
    console.log('The player has played slot for ' + counter2 + ' times, and have won ' + counter1 + ' times.');
}
slot3();
