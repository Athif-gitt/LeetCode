/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    for (let i = 0; i < s.length; i++){
        let element = s.charAt(i);
        switch(element) {
            case "(" : stack.push(")");
            break;
            case "[" : stack.push("]");
            break;
            case "{" : stack.push("}");
            break
            default: 
            if (element !== stack.pop()){
                return false
            } 
        }
    }
    return stack.length === 0;
};