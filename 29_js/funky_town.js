//Team Neatle - Emily Lee and Stefan Tan
//SoftDev1 pd06
//K29 -- Sequential Progression II: Electric Boogaloo
//2018-12-19

var fibonacci = function(n) {
    if (n == 0){
	return 0;
    }
    if (n == 1){
	return 1;
    }
    return (fibonacci(n - 1) + fibonacci(n - 2));
};

var gcd = function(a,b){
    if(a == 0)
	return b;
    return gcd(b%a,a);
};

var students = ["Bob", "Steve", "Kevin", "Tim", "Wally", "Tom", "Jane"];

var randomStudent = function() {
    rand = Math.floor(Math.random()*students.length);
    return students[rand];
};

var ans = document.getElementById("ans");

var fibbut = document.getElementById("a");

var fib7 = function() {
    var result = fibonacci(7);
    console.log(result);
    ans.innerHTML = result;
};

var gcdbut = document.getElementById("b");

var gcd32_24 = function() {
    var result = gcd(32, 24);
    console.log(result);
    ans.innerHTML = result;
};

var rsbut = document.getElementById("c");

var randstud = function() {
    var result = randomStudent();
    console.log(result);
    ans.innerHTML = result;
};

fibbut.addEventListener('click', fib7);
gcdbut.addEventListener('click', gcd32_24);
rsbut.addEventListener('click', randstud);


