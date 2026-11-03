var num = "",
  operand1,
  operand2,
  op,
  n1,
  n2,
  ans;
function num1() {
  num = num + "1";
  document.getElementById("output").textContent = num;
}
function num2() {
  num = num + "2";
  document.getElementById("output").textContent = num;
}
function num3() {
  num = num + "3";
  document.getElementById("output").textContent = num;
}
function num4() {
  num = num + "4";
  document.getElementById("output").textContent = num;
}
function num5() {
  num = num + "5";
  document.getElementById("output").textContent = num;
}
function num6() {
  num = num + "6";
  document.getElementById("output").textContent = num;
}
function num7() {
  num = num + "7";
  document.getElementById("output").textContent = num;
}
function num8() {
  num = num + "8";
  document.getElementById("output").textContent = num;
}
function num9() {
  num = num + "9";
  document.getElementById("output").textContent = num;
}
function num0() {
  num = num + "0";
  document.getElementById("output").textContent = num;
}
function dot() {
  num = num + ".";
  document.getElementById("output").textContent = num;
}
function add() {
  operand1 = num;
  document.getElementById("output").textContent = "";
  num = "";
  op = "+";
}
function sub() {
  operand1 = num;
  document.getElementById("output").textContent = "";
  num = "";
  op = "-";
}
function mul() {
  operand1 = num;
  document.getElementById("output").textContent = "";
  num = "";
  op = "*";
}
function div() {
  operand1 = num;
  document.getElementById("output").textContent = "";
  num = "";
  op = "/";
}
function equal() {
  operand2 = num;
  document.getElementById("output").textContent = "";
  num = "";
  n1 = parseFloat(operand1);
  n2 = parseFloat(operand2);
  if (op == "+") {
    ans = n1 + n2;
  } else if (op == "-") {
    ans = n1 - n2;
  } else if (op == "*") {
    ans = n1 * n2;
  } else if (op == "/") {
    ans = n1 / n2;
  }
  document.getElementById("output").textContent = ans.toString();
}