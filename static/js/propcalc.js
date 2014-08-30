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
function formatMoney(input)
{
    return "$ " + input
};
function CleanNum(input1)
{
    var source = input1
    source = source.replace(/,/g,'');
    source = source.replace(/$/g,'')
    return source;
};
function MultInputs(input1, input2, outputName)
{
    var total = 1;
    var ele1 = document.getElementsByClassName(input1);
    var ele2 = document.getElementById(input2);
    total *= parseFloat(CleanNum(ele1[0].value));
    total *= parseFloat(CleanNum(ele2.innerHTML));
    var Display = document.getElementById(outputName);
    Display.innerHTML = (total).formatMoney(formatNumber(2,".",","));
};
