<<<<<<< HEAD
function tellTime(hour, minute, period){
    var min = 'just after';
    var prd = 'in the morning';

    if (period == 'AM'){
        if (minute > 30){
            min = 'almost';
            hour++;
        }
    }
    if (period == 'PM'){
        prd = 'in the evening';
        if (minute > 30){
            min = 'almost';
            hour++;
        }
    }
    console.log("It's " + min + " " + hour + " " + prd + ".");
}
console.log(tellTime(8,50,'AM'));
=======


function tellTime(hour, minute, period){
    var min = '';
    var prd = '';

    //Directly output midnight and noon
    if (period == 'AM' && hour == 12 && minute == 0){
        console.log("It's midnight.");
        return;
    }
    if (period == 'PM' && hour == 12 && minute == 0){
        console.log("It's noon.");
        return;
    }

    //Define period
    if (period == 'AM' && hour > 0 && hour < 12){
        prd = 'in the morning';
    }
    else if (period == 'PM' && hour > 0 && hour < 6){
        prd = 'in the afternoon';
    }
    else if (period == 'PM' && hour >= 6 && hour < 12){
        prd = 'at night';
    }

    //Define minutes
    if (minute > 0 && minute <15 || minute > 15 && minute < 30){
        min = ' after';
    }
    else if (minute > 30 && minute <45 || minute > 45 && minute < 61){
        min = ' to';
        minute = 60 - minute;
        hour++;
    }

    //Directly output quarter past, half past, quarter to..
    else if (minute == 15){
        min = 'quarter past';
        console.log("It's " + min + " " + hour + " " + prd + ".");
        return;
    }
    else if (minute == 30){
        min = 'half past';
        console.log("It's " + min + " " + hour + " " + prd + ".");
        return;
    }
    else if (minute == 45){
        min = ' quarter to';
        minute = 60 - minute;
        hour++;
        console.log("It's " + min + " " + hour + " " + prd + ".");
        return;
    }

    console.log("It's " + minute + min + " " + hour + " " + prd + ".");

}



console.log(tellTime(12,00,'PM'));
console.log(tellTime(12,00,'AM'));
console.log(tellTime(11,50,'AM'));
console.log(tellTime(11,45,'AM'));
console.log(tellTime(4,15,'AM'));
console.log(tellTime(6,30,'PM'));
console.log(tellTime(2,11,'PM'));
>>>>>>> 99a0cae3f87bc92016d1bae3197809a0bf9862c8
