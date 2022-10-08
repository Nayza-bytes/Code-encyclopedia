//The forEach() method calls a function (a callback function) once for each array element.

function myFunc(value){
    return value += 5;
}

function lessThan(value){
    return value < 20;
}

const myIntArray = [
    1,
    48,
    230,
    4,
    18,
];

myIntArray.forEach(myFunc);
console.log(myIntArray);

//The map() method creates a new array by performing a function on each array element.
const numbers = myIntArray.map(myFunc);
console.log(numbers);

//The filter() method creates a new array with array elements that pass a test.
const over20 = myIntArray.filter(lessThan);
console.log(over20);

//To finish