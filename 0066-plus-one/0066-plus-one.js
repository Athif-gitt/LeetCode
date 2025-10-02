var plusOne = function(digits) {
    const num = BigInt(digits.join(''));
    const incremented = num + 1n; 
    return incremented.toString().split('').map(Number);
}
