//Chapter 1, page 16

/* <Setting and Swapping>
Set myNumber to 42. Set myName to your name. Now Swap myNumber into myName
& vice versa
*/
function settingAndSwapping(){
    var myNumber = 42;
    var myName = 'Jian';
    var temp = myNumber;
    myNumber = myName;
    myName = temp;
    console.log(myNumber);
    console.log(myName);
}

/* <Print -52 to 1066>
Print integers from -52 to 1066 using for loop
*/
function printNum(){
    for (var i = -52; i < 1067; i++){
        console.log(i);
    }
}

/* <Don't Worry, Be Happy>
Create beCheerful(). Within it, console.log string "good morning!" Call it 98
times.
*/
function beCheerful(){
    for (var i = 1; i < 99; i++){
        console.log('good morning!');
    }
}

/* <Multiples of Three, but Not All>
Using for, print numbers of 3 from -300 to 0. Skip -3 and -6.
*/
function threeSkip(){
    for (var i = -300; i < -6; i += 3){
        console.log(i);
    }
    console.log(0);
}

/* <Printing Integers with While>
Printing integers from 2000 to 5280, using While
*/
function printWithWhile(){
    var i = 2000;
    while (i < 5281){
        console.log(i);
        i++;
    }
}

/* <You Say It's Your Birthday
If 2 given numbers represent your birth month and day in either order, log
"How did you know?", else log "Just another day...."
*/
function birthday(month, day){
    if (month == 8 && day == 29){
        console.log('How did you know?');
    }
    else if (month == 29 && day == 8){
        console.log('How did you know?');
    }
    else {
        console.log('Just another day....');
    }
}
console.log(birthday(8, 29));

/* <Leap Year>
Write a function that determines whether a given year is a leap year. If a
year is divisible year by four, it is a leap year, unless it is divisible
by 100. However if it is  divisible by 400, then it is.
*/
function leapYear(year){
    if (year % 4 === 0 && year % 100 !== 0 || year % 400 === 0){
      console.log(year + ' is a leap year');
    }
    else{
      console.log(year + ' is NOT a leap year');
    }
}
console.log(leapYear(4));
console.log(leapYear(400));
console.log(leapYear(800));
console.log(leapYear(2000));
console.log(leapYear(1));
console.log(leapYear(100));
console.log(leapYear(1800));

/* <Print and Count>
Print all integer multiples of 5, from 512 to 4096. Afterward, also log how
many there were.
*/
function printAndCount(){
    var counter = 0;
    for (var i = 515; i < 4096; i+=5){
        console.log(i);
        counter++;
    }
    console.log(counter);
}
console.log(printAndCount);

/* <Multiples of Six>
Print multiples of 6 up to 60,000, using a while
*/
function multiplesOfSix(){
    var num = 6;
    while (num < 60001){
        console.log(num);
        num+=6;
    }
}

/* <Counting, the Dojo Way>
Print integer 1 to 100. If divisible by 5, print "Coding" instead. If by 10,
also print " Dojo".
*/
function countingDojo(){
    for (var i = 1; i < 101; i++){
        if (i % 5 === 0 && i % 10 !== 0){
            console.log('Coding');
        }
        else if (i % 10 === 0){
            console.log('Coding Dojo');
        }
    }
}
console.log(countingDojo());

/* <What Do You Know?>
Your function will be give an input parameter 'incomning'. Please console log
this value.
*/
function printIncoming(x){
    console.log(x);
}
console.log(printIncoming('incoming'));

/* <Whoa, That Sucker's Huge>
Add odd integers from -300000 to 300000, and console.log the final sum. Is there
a short cut?
*/
function sumHuge(){
    var sum = 0;
    for (var i = -29; i < 30; i+=2){
        sum += i;
    }
    console.log(sum);
}
console.log(sumHuge());

/* <Count Down By Fours>
Log positive numbers starting at 2016, counting down by fours (excluding 0),
without a FOR loop.
*/
function countDownByFour(){
    var num = 2016;
    while (num > 0){
      console.log(num);
      num -=4;
    }
}
console.log(countDownByFour());

/* <Flexible Countdown>
Based on earlier "Count Down By Fours", given lowNum, highNum, mult, print
multiples of mult from highNum down to lowNum, using a FOR. For (2, 9, 3),
print 9 6 3 (on successive lines)
*/
function flexibleCountdown(lowNum, highNum, mult){
    while (highNum % mult !== 0){
        highNum--;
    }
    for (var i = highNum; i >= lowNum; i -= mult){
        console.log(i);
    }
}
console.log(flexibleCountdown(2, 10, 3));

/* <The Final Countdown>
This is based on "Flexible Countdown". The parameter names are not as helpful,
but the problem is essentially identical; don't be thrown off! Given 4 parameters
(param1, param2, param3, param4), print the multiples of param1, starting at
param2, and extending to param3. One exception: if a multiple is equals to
param4, then skip (don't print) that one. Do this during a WHILE. Given
(3, 5, 17, 9), print (6, 12, 15).
*/

function theFinalCountDown(p1, p2, p3, p4){
    while (p2 % p1 !== 0){
        p2++;
    }
    for (var i = p2; i < p4; i+=p1){
           console.log(i);
        }
    var p5 = p4 + 1;
    while (p5 % p1 !== 0){
        p5++;
    }
    for (var j = p5; j < p3; j+=p1){
        console.log(j);
    }
}
console.log(theFinalCountDown(4,1,17,12));




//Chapter 1, page 20


/* <Countdown>
Create a function that accepts a number as an input. Return a new array that
counts down by one, from the number (as array's "zero" element) down to 0
(the last element). How long is this array?
*/
function countdown(num)
{  var arr=[];
   for (var i = num; i >= 0; i--){
   arr.push(i);
   }
   return arr;
}
console.log(countdown(5));

/* <Print and Return>
Your function will receive an array with two numbers. Print the first one and
return the second.
*/
function printAndReturn(arr)
{  console.log(arr[0]);
   return arr[1];
}

/* <First Plus Length>
Given and array, return the sum of the first value in the array, plus the
array's length. What happens if the array's first value is not a number, but
a string (like "what?") or a boolean (like false)?
*/
function firstPlusLength(arr)
{  if (typeof arr[0] == 'number'){
       var sum = arr[0] + arr.length;
       return sum;
   }
   else{
       console.log('The first element in the array is not a number.');
   }
}
console.log(firstPlusLength(["good", 2, 5]));

/* <Values Greater than Second Generalized>
Write a function that accepts any array, and returns a new array with the array
values that are greater than its 2nd value. Print how many value this is. What
will you do if the array is only one element long?
*/
function greaterThanSecond(arr){
    var counter = 0;
    var newarr = [];
    if (arr.length > 1){
        if (arr[0] > arr[1]){
             counter++;
             newarr.push(arr[0]);
           }
        for (var i = 2; i < arr.length; i++){
           if (arr[i] > arr[1]){
             counter++;
             newarr.push(arr[i]);
           }
        }
        console.log(counter);
        return newarr;
    }
    else{
        return null;
    }
}
console.log(greaterThanSecond([2, 1, 3, 4, 5]));

/* <This Length, That Value>
Given two numbers, return array of length num1 with each value nume2. Print
"Jinx!" if they are the same.
*/
function thisLengthThatValue(num1, num2){
    var arr=[];
    for (var i = 0; i < num1; i++){
      arr.push(num2);
    }
    if (num1 == num2){
      console.log("Jinx!");
    }
    return arr;
}
console.log(thisLengthThatValue(4,4));


/* <Fit the First Value>
Your function should accept an array. If value at [0] is greater than array
length, print "Too Big!"; if value at [0] is less than array length, print
"Too Small!"; otherwise print "Just right!".
*/
function fitTheFirstValue(arr){
  if (arr[0] > arr.length){
    console.log("Too Big!")
  }
  else if (arr[0] < arr.length){
    console.log("Too Small!")
  }
  else
    console.log("Just Right!")
}
console.log(fitTheFirstValue([2,4,5]));


/* <Fahrenheit to Celsius>
*/
function fahrenheitToCelsius(fDegrees){
  var c = (fDegrees - 32) / 9 * 5;
  return c;
}
console.log(fahrenheitToCelsius(104));


/* <Celsius to Fahrenheit>
*/
function celsiusToFahrenheit(cDegrees){
  var f = cDegrees / 5 * 9 + 32;
  return f;
}
console.log(celsiusToFahrenheit(35));



//Chapter 1, page 22
/* <Biggie Size>
Given an array, write a function that changes all positive numbers in the array
to "big". Example, makeItBig([-1, 3, 5, -5]), return that same array, changed
to [-1, "big", "big", -5].
*/
function makeItBig(arr){
  for (var i = 0; i < arr.length; i++){
    if (arr[i] > 0){
      arr[i] = "big";
    }
  }
  return arr;
}
console.log(makeItBig([-1, 3, 5, -5]));

/* <Print Low, Return High>
Create an function that takes array of numbers. The function should print the
lowest value in the array, and return the highest value in the array.
*/
function printLowReturnHigh(arr){
  var max = arr[0];
  var min = arr[0];
  for (var i = 0; i < arr.length; i++){
    if (max < arr[i]){
      max = arr[i];
    }
    if (min > arr[i]){
      min = arr[i];
    }
  }
  console.log(min);
  return max;
}
console.log(printLowReturnHigh([1,2,3,4,5]));

/* <Print One, Return Another>
Build an array that takes array of numbers. The function should print Second
to last value in the array, and return first odd value in the array.
*/
function printOneReturnAnother(arr){
  console.log(arr[arr.length-2]);
  for (var i = 0; i < arr.length; i++){
    if (arr[i]%2 != 0){
      return arr[i];
      break;
    }
  }
}
console.log(printOneReturnAnother([1,2,3,4,5,6]));

/* <Double Vision>
Given an array, create a function to return a new array where each value in the
original has been doubled. Calling double([1,2,3]) should return [2,4,6] without
changing original.
*/
function double(arr){
  var newarr=[];
  for (var i = 0; i < arr.length; i++){
    arr[i] = arr[i] * 2;
    newarr.push(arr[i]);
  }
  return newarr;
}
console.log(double([1,2,3]));

/* <Count Positives>
Given an array of numbers, create a function to replace the last value with
number of positive values. Example, countPositives([-1,1,1,1]) changes array
to [-1,1,1,3] and returns it.
*/
function countPositives(arr){
  var counter = 0;
  for (var i = 0; i < arr.length; i++){
    if (arr[i] > 0){
      counter++;
    }
  }
  arr[arr.length-1] = counter;
  return arr;
}
console.log(countPositives([-1,1,1,1]));

/* <Evens and Odds>
Create a function that accepts an array. Every time that array has three odd
values in a row, print "That's odd!". Every time the array has three evens in a
row, print "Even more so!".
*/
function evensAndOdds(arr){
  var evens = 0;
  var odds = 0;
  for (var i = 0; i < arr.length; i++){
    if (arr[i] % 2 != 0){
      odds++;
      evens = 0;
      if (odds % 3 == 0){
        console.log("That's odd!")
      }
    }
    else {
      evens++;
      odds = 0;
      if (evens % 3  == 0){
        console.log("Even more so!")
      }
    }
  }
}
console.log(evensAndOdds([1,1,1,2,1,3,3,3,2,2,2,2,2,2]));

/* <Increment the Seconds>
Given arr, add 1 to odd elements ([1], [3], etc), console log all value and
return arr.
*/
function incrementTheSeconds(arr){
  for (var i = 0; i < arr.length; i++){
    if (arr[i] % 2 !== 0){
      arr[i]++;
    }
    console.log(arr[i]);
  }
  return arr;
}
console.log(incrementTheSeconds([1,2,3,4,5,6]));

/* <Previous Lengths>
You are passed array containing strings. Working within that same array, replace
each string with a number - the length of the string at previous array index -
and return the array.
*/
function previousLengths(arr){
    var temp = arr[arr.length-1].length;
    for (var i = arr.length-1; i > 0; i--){
        arr[i] = arr[i-1].length;
    }
    arr[0] = temp;
    return arr;
}
console.log(previousLengths(["jason", "is", "a", "good", "student"]));


/* <Add Seven to Most>
Build function that accepts array. Return a new array with all values except
first, adding 7 to each. Do not alter the original array.
*/
function addSevenToMost(arr){
  var newarr = [];
  for (var i = 1; i < arr.length; i++){
    newarr.push(arr[i] + 7);
  }
  return newarr;
}
console.log(addSevenToMost([1,2,3,4]));

/* <Reverse Array>
Given Array, write a function that reverses values, in-place. Example:
reverse([3,1,6,4,2]) returns same array, containing[2,4,6,1,3].
*/
function reverseArray(arr){
  for (var i = 0; i < arr.length/2; i++){
    var temp = arr[i];
    arr[i] = arr[arr.length - i -1];
    arr[arr.length - i -1] = temp;
  }
  return arr;
}
console.log(reverseArray([1,2,3,4,5]));

/* <Outlook Negative>
Given an array, create and return a new one containing all the values of the
provided array, made negative (not simply multiple by -1). Given [1,-3,5],
return [-1,-3,-5]
*/
function outlookNegative(arr){
  var newarr = [];
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < 0){
    newarr.push(arr[i]);
    }
    else if (arr[i] > 0){
      newarr.push(arr[i] * (-1));
    }
    else {
      newarr.push(0);
    }
  }
  return newarr;
}
console.log(outlookNegative([1,-3,5,0,2,-2]));

/* <Always Hungry>
Create a function that accepts an array, and prints "yummy" each time one of
the values equals to "food". If no array elements are "food", then print
"I am hungry" once.
*/
function alwayHungry(arr){
    var hungry = true;
    for (var i = 0; i < arr.length; i++){
      if (arr[i] == 'food'){
        console.log("Yummy!");
        hungry = false;
      }
    }
    if (hungry == true){
        console.log("I am hungry!");
    }
}
console.log(alwayHungry(['food','food',1,2]));

/* <Swap Toward the center>
Given an array, swap first and last, third and third-to-last, etc.
*/
function swapTowardTheCenter(arr){
  var temp1 = arr[0];
  arr[0] = arr[arr.length - 1];
  arr[arr.length - 1] = temp1;

  if (arr.length > 2){
      var temp2 = arr[2];
      arr[2] = arr[arr.length - 3];
      arr[arr.length - 3] = temp2;
  }
  else {
    console.log("The array has less than 3 elements.")
  }
}
console.log(swapTowardTheCenter([1,2,3,4,5,6]));

/* <Scale The Array>
Given array arr and number num, multiply each arr value by num, and return
the changed arr.
*/
function scaleTheArray(arr, num){
  for (var i = 0; i < arr.length; i++){
    arr[i] = arr[i] * num;
  }
  return arr;
}
console.log(scaleTheArray([1,2,3,4], 2));


//Chapter 1, page 25
/* <Only Keep the Last Few>
Stan learned something new today: that directly incrementing an array's
.length immediately shortens it by that amount. Given array arr and number
X, remove all except the last X element, and return arr (changed and shorter).
Given ([2,4,6,8,10],3), change the array to [6,8,10] and return it.*/
function onlyKeepTheLastFew(arr, num){
    for (var i = 0; i < arr.length + 1 - num; i++){
        arr.splice(0,1);
    }
    return arr;
}
console.log(onlyKeepTheLastFew([2,4,6,8,10],3));

/* <Math Help>
Cartman doesn't really like math; he needs help. You are given two numbers -
coefficents M and B in the equation Y = MX + B. Build a function to return the
X-incecept (his older cousin Fiaz wisely reminds him that X-incecept is the
value of X where Y equals to zero)
*/
function mathHelp(m, b){
    var y = 0;
    var x = (y - b) / m;
    return x;
}
console.log(mathHelp(1,10));

function removeRange(arr, s, e){

}

function pushFront(arr, num){
    for (var i = arr.length; i > 0; i--){
        arr[i] = arr[i-1];
    }
        arr[0] = num;
    return arr;
}
console.log(pushFront([1,2,3,4,5], 9));


function removeAt(arr, n){
    for (var i = 0; i < arr.length-1; i++){
        if (i == n - 1 && n !== 0){
            i++;
        }
        arr[i] = arr[i+1];
    }
    arr.pop();
    return arr;
}
console.log(removeAt([1,2,3,4,5], 2));
