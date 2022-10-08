//Basics
//run to see what's happening
//Strings method
let mySentence = 'yesterday I eat a pizza with some friends, in a park';
let stringToConcat = 'And we met a very friendly cat'
let str = '    Some whitespace at start !'


//lenght of a string
let sentenceLenght = mySentence.length;
console.log(sentenceLenght);

//Slicing a string
let sentencePart = mySentence.slice(10, 23);
console.log(sentencePart);

//substr() function take two parameter: Where to start slicing and the lenght of the slice
let substring = mySentence.substr(8, 6);
console.log(substring);

//replace a string:
let newSentence = mySentence.replace('pizza', 'burger');
console.log(newSentence);

//Convert to upper case or lower case
console.log(mySentence.toUpperCase());
console.log(mySentence.toLowerCase());

//Concat two string together
concatenedString = mySentence.concat(' ', stringToConcat);
console.log(concatenedString);

//remove any whitespace or remove only whitespace at a start (trimStart())
console.log(mySentence.trim());
console.log(str.trimStart());




