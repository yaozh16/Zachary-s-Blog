# 2018-2-1 JavaScript Note(3)
## 闭包
```
'use strict';

function create_counter(initial) {
    var x = initial || 0;
    return {
        inc: function () {
            x += 1;
            return x;
        }
    }
}
```
它用起来像这样：
```
var c1 = create_counter();
c1.inc(); // 1
c1.inc(); // 2
c1.inc(); // 3

var c2 = create_counter(10);
c2.inc(); // 11
c2.inc(); // 12
c2.inc(); // 13
```
## 箭头函数 
```
//返回一个数字
var functionName= (x,y)=>x*x+y*y;
(x,y)=>x*x+y*y;
//返回一个对象(注意括号)
x => ({ foo: x });
```
箭头函数完全修复了this的指向，this总是指向词法作用域，也就是外层调用者obj
## generator
1. 语法:function* func(Para)和yield
2. 调用func(Para)仅仅生成generator对象
3. 之后调用next()方法或者for ... of循环迭代generator对象
```JavaScript
function* fib(max) {
    var
        t,
        a = 0,
        b = 1,
        n = 0;
    while (n < max) {
        yield a;
        [a, b] = [b, a + b];
        n ++;
    }
    return;
}
var f = fib(5);
f.next(); // {value: 0, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 2, done: false}
f.next(); // {value: 3, done: false}
f.next(); // {value: undefined, done: true}

for (var x of fib(10)) {
    console.log(x); // 依次输出0, 1, 1, 2, 3, ...
}

```