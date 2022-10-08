let mySentence = 'yesterday I eat a pizza with some friends, in a park';
let stringToConcat = 'And we met a very friendly cat'
let str = '    Some whitespace at start !'

var Name = 'Ronaldo'
var nickname = 'sui'

//The lastIndexOf() method returns the index of the last occurrence of a specified text in a string:
console.log(mySentence.lastIndexOf('park')); // can take seconde parameter, that is where the method is going to start searching

//The indexOf() method returns the index of (the position of) the first occurrence of a specified text in a string:
console.log(mySentence.indexOf('eat'));

//The search() method searches a string for a specified value and returns the position of the match:
console.log(mySentence.search('with'));

//The match() method searches a string for a match against a regular expression, and returns the matches, as an Array object.
console.log(mySentence.match(/zza/g)); // g modifier is for global else the match function will just return the first match

//The includes() method returns true if a string contains a specified value.
console.log(mySentence.includes('friends')); /*
                                                Syntax:
                                                string.includes(searchvalue, start)

                                                searchvalue	Required. The string to search for
                                                start	Optional. Default 0. Position to start the search
                                                Returns:	Returns true if the string contains the value, otherwise false
                                             */

//The startsWith() method returns true if a string begins with a specified value, otherwise false:
console.log(mySentence.startsWith('yesterday'));

//The endsWith() method returns true if a string ends with a specified value, otherwise false:
console.log(mySentence.endsWith('park'));

//Template literals
var text = `Welcome ${nickname} your name is ${Name} `;