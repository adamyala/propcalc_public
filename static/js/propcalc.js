$(document).on("keyup", function() {
    putVal(getVal('fldCompRent') * getVal('txtBldgSqft'),'txtSubt1');
    putVal(getVal('fldVaca')/-100 * getVal('txtSubt1'),'txtSubt2');
    putVal(getVal('txtSubt1') + getVal('txtSubt2'),'txtSubt3');
    putVal(getVal('fldExp')/-100 * getVal('txtSubt3'),'txtSubt4');
    putVal(getVal('txtSubt3') + getVal('txtSubt4'),'txtSubt5');
    putVal(getVal('txtSubt5') / (getVal('fldCap') / 100),'txtSubt6');
    putVal(getVal('txtSubt6') / getVal('txtBldgSqft'),'txtSubt7');
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
