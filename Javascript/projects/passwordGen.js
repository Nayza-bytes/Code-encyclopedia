//Password generator

const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
const specialChar = ['&', '@', '|', '/', '#', '"', "'", '(', ')', '{', '}', '[', ']', '^', '_', '-'];
var pw = '';
let passwordLenght = 30;

const char = alphabet.concat(specialChar);

for(let i = 0; i <= passwordLenght; i++){
    pw += char[Math.floor(Math.random() * char.length)];
}

console.log(pw);