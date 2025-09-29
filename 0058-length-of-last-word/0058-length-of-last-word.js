/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLastWord = function(s) {
    let res = s.trim().split(" ")
    let ans = res[res.length - 1].length
    return ans;
};