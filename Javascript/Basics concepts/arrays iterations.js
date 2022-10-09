//The forEach() method calls a function (a callback function) once for each array element.

function myFunc(value){
    return value += 5;
}

function lessThan(value){
    return value < 20;
}
function MoreThan(value, index, array){  //index and array parameter can be put here but are not useful
    return value > 40;
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

//The reduce() method runs a function on each array element to produce (reduce it to) a single value.
let sum = myIntArray.reduce(myFunc);
console.log(sum);

//The every() method checks if all array values pass a test.
let Over40 = myIntArray.every(MoreThan);
console.log(Over40);

//The some() method checks if some array values pass a test.
let someOver40 = myIntArray.some(MoreThan);
console.log(someOver40);

//The indexOf() method searches an array for an element value and returns its position.
let position = myIntArray.indexOf(4);
console.log(position);

//Array.lastIndexOf() is the same as Array.indexOf(), but returns the position of the last occurrence of the specified element
let pos = myIntArray.lastIndexOf(18);
console.log(pos);

//The find() method returns the value of the first array element that passes a test function.
let first = myIntArray.find(MoreThan);
console.log(first);

//The findIndex() method returns the index of the first array element that passes a test function.
let firstIndex = myIntArray.findIndex(lessThan);
console.log(firstIndex);

//The Array.from() method returns an Array object from any object with a length property or any iterable object.
let stringArr = Array.from('GhJJklL');
console.log(stringArr);

//Array.includes() allows us to check if an element is present in an array
console.log(myIntArray.includes(4));
console.log(myIntArray.includes(210));

