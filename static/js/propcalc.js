$(document).on("keyup", function() {
    putVal(mult(getVal('fldCompRent'),getVal('txtBldgSqft')),'txtSubt1');
    putVal(multA(getVal('fldVaca'),getVal('txtSubt1')),'txtSubt2');
    putVal(addr(getVal('txtSubt1'),getVal('txtSubt2')),'txtSubt3');
    putVal(multA(getVal('fldExp'),getVal('txtSubt3')),'txtSubt4');
    putVal(addr(getVal('txtSubt3'),getVal('txtSubt4')),'txtSubt5');
    putVal(diviA(getVal('fldCap'),getVal('txtSubt5')),'txtSubt6');
    putVal(divi(getVal('txtBldgSqft'),getVal('txtSubt6')),'txtSubt7');
});
Number.prototype.formatNumber = function(c, d, t)
{
    var n = this, 
    c = isNaN(c = Math.abs(c)) ? 2 : c, 
    d = d == undefined ? "." : d, 
    t = t == undefined ? "," : t, 
    s = n < 0 ? "-" : "", 
    i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "", 
    j = (j = i.length) > 3 ? j % 3 : 0;
    return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
};
function toMoney(input)
{
    return "$ " + input;
};
function toNum(input)
{
    var source = input;
    source = source.split('$').join('')
    source = source.split(',').join('')
    return source.trim();
};
function getVal(input)
{
    if (input.substring(0,3) == 'fld') {
        result = parseFloat(toNum(document.getElementById(input).value));
    }
    else {
        result = parseFloat(toNum(document.getElementById(input).innerHTML));
    }
    return result;
};
function putVal(source, input)
{
    var Display = document.getElementById(input);
    Display.innerHTML = toMoney(source.formatNumber(2,".",","));
};
function mult(input1, input2)
{
    return input1 * input2;
};
function multA(input1, input2)
{
    return -( input1 / 100 ) * input2;
    // return input2;
};
function divi(input1, input2)
{
    return input2 / input1;
}
function diviA(input1, input2)
{
    return input2 / (input1 / 100);
};
function addr(input1, input2)
{  
    return input1 + input2;
}

// function multInputs(inputField, inputText, outputName)
// {
//     var total = 1;
//     var ele1 = document.getElementById(inputField);
//     var ele2 = document.getElementById(inputText);
//     total *= parseFloat(CleanNum(ele1.value));
//     total *= parseFloat(CleanNum(ele2.innerHTML));
//     var Display = document.getElementById(outputName);
//     Display.innerHTML = formatMoney(total.formatNumber(2,".",","));
// };
