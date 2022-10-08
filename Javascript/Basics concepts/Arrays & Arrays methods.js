/*
In javascript, arrays can be objects, functions or another arrays
Like this:
cosnt doubleArrays = [[1, 2, 3], [4, 5, 6]]
 */


const cars = ['Volvo', 'Audi', 'Volswagen', 'Lamborghini'];
const otherCars = ['Opel', 'renault'];
const food = [
    'French fries',
    'Salad',                //You can declare variable like the first one
    'Pasta'                 //Or like the second one!
];

//This example also create an array
const names = new Array('Philipe', 'Nathan', 'Mike', 'Alex');



console.log(cars);
console.log(food);
console.log(names);

//Accesing arrays elements:

console.log('the second element of the cars array: \n');
console.log(cars[1]);
console.log(food[food.length - 1]); //Accessing the last element of the array

//changing array element
const newCars = cars;       

newCars[2] = 'Mercedes';
console.log(newCars);

//looping through the array
for(let i = 0; i < names.length; i++){
    console.log(food[i]);
}

//adding an element into an array
food.push('beef');
food.push('chicken');
console.log(food);

//remove the last element from an array
food.pop();

//recognize an array
console.log(Array.isArray(food));


/*

Arrays Property Methods

*/

//Lenght method
let carsLenght = cars.length;
console.log(carsLenght);

//Sort method
console.log(cars.sort());

//The JavaScript method toString() converts an array to a string of (comma separated) array values.
console.log(cars.toString());

//The join() method also joins all array elements into a string. It behaves just like toString(), but in addition you can specify the separator:
console.log(names.join(' | '));

//The shift() method removes the first array element and "shifts" all other elements to a lower index.
names.shift();

//The unshift() method adds a new element to an array (at the beginning), and "unshifts" older elements:
names.unshift('alex');

//merging two arrays
console.log(cars.concat(otherCars));

//The splice() method can be used to add new items to an array:
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.splice(2, 0, "Lemon", "Kiwi");
console.log(fruits);

//The slice() method slices out a piece of an array into a new array. This example slices out a part of an array starting from array element 1 ("Orange"):
console.log(cars.slice(1));

//reversing an array
cars.reverse();
console.log(cars);



