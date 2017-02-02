function numbersOnly(arr){
    var newarr = [];
    for (var i = 0; i < arr.length; i++){
        if (typeof arr[i] == 'number'){
            newarr.push(arr[i]);
        }
    }
    return newarr;
}
console.log(numbersOnly([1, "apple", -3, "orange", 0.5]));


function numbersOnlyRemove(arr){
    for (var i = 0; i < arr.length; i++){
        if (typeof arr[i] !== 'number'){
            arr.splice(i,1);
        }
    }
    return arr;
}
console.log(numbersOnlyRemove([1, "apple", -3, "orange", 0.5]));
