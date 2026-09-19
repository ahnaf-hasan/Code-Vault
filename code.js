let n = Number(prompt("Enter a number:"));
let isPrime = true;

if (n <= 1) {
    isPrime = false;
} else {
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            isPrime = false;
            break;
        }
    }
}

if (isPrime) {
    console.log(n + " is a Prime Number");
} else {
    console.log(n + " is Not a Prime Number");
}
