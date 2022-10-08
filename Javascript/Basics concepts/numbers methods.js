let myInt = 100;
let myInt2 = 48;
let result = myInt + myInt2;
let myFloat = 9.25487631;

//toString method convert a number into an integer
console.log(result.toString());

//toExponential() returns a string, with a number rounded and written using exponential notation
console.log(myInt.toExponential(4));

//toFixed() returns a string, with the number written with a specified number of decimals
console.log(myFloat.toFixed(2));
console.log(myFloat.toFixed(5));
console.log(myFloat.toFixed(4));
console.log(myFloat.toFixed(7));

//toPrecision() returns a string, with a number written with a specified length:
console.log(myFloat.toPrecision(4));

//valueOf() returns a number as a number.
console.log(myInt2.valueOf());

//Number() can be used to convert JavaScript variables to numbers:
let myBool = true;
console.log(Number(myBool));

Number(new Date("1970-01-01"))

//parseInt() parses a string and returns a whole number. Spaces are allowed. Only the first number is returned:
console.log(parseInt(myInt));

//parseFloat() parses a string and returns a number. Spaces are allowed. Only the first number is returned:
console.log(parseFloat(myFloat));

/*
Number Properties

Property	Description
MAX_VALUE	Returns the largest number possible in JavaScript
MIN_VALUE	Returns the smallest number possible in JavaScript
POSITIVE_INFINITY	Represents infinity (returned on overflow)
NEGATIVE_INFINITY	Represents negative infinity (returned on overflow)
NaN	Represents a "Not-a-Number" value
*/

let maxNumber = Number.MAX_VALUE;
let minNumber = Number.MIN_VALUE;
let not_a_number = Number.NaN;

console.log(maxNumber);
console.log(minNumber);
console.log(not_a_number);


