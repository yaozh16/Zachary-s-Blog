# 2018-2-1 JavaScript Note(2)
## function
1. 语法function [functionName] ([parameter])
2. 语法var  [functionName] =function([parameter])
3. 传入参数允许多于需要的函数
4. arguments保留字可以获取参数信息
* arguments.length
* arguments[i]
5. ...rest
用于保存多余的参数
```
function foo(a, b, ...rest)
```
6. JavaScript引擎在行末自动添加分号，注意return语句
## Varialble
JavaScript的函数定义有个特点，它会先扫描整个函数体的语句，把所有申明的变量“提升”到函数顶部,但不会提升变量的赋值
1. JavaScript默认有一个全局对象window，全局作用域的变量实际上被绑定到window的一个属性
2.  命名空间
```JavaScript
// 唯一的全局变量MYAPP:
var MYAPP = {};

// 其他变量:
MYAPP.name = 'myapp';
MYAPP.version = 1.0;

// 其他函数:
MYAPP.foo = function () {
    return 'foo';
};

```
3. 用let替代var可以申明一个块级作用域的变量
```JavaScript
'use strict';

function foo() {
    var sum = 0;
    for (let i=0; i<100; i++) {
        sum += i;
    }
    // SyntaxError:
    i += 1;
}
```
4. ES6标准引入了新的关键字const来定义常量，const与let都具有块级作用域
```JavaScript
'use strict';

const PI = 3.14;
PI = 3; // 某些浏览器不报错，但是无效果！
PI; // 3.14
```
5. 解构赋值
```JavaScript
'use strict';

// 如果浏览器支持解构赋值就不会报错:
var [x, y, z] = ['hello', 'JavaScript', 'ES6'];
// 忽略前两个元素，只对z赋值第三个元素
let [, , z] = ['hello', 'JavaScript', 'ES6'];
```
对一个对象进行解构赋值时，同样可以直接对嵌套的对象属性进行赋值，只要保证对应的层次是一致的
```JavaScript
var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school',
    address: {
        city: 'Beijing',
        street: 'No.1 Road',
        zipcode: '100001'
    }
};
var {name, address: {city, zip}} = person;
name; // '小明'
city; // 'Beijing'
zip; // undefined, 因为属性名是zipcode而不是zip
// 注意: address不是变量，而是为了让city和zip获得嵌套的address对象的属性:
address; // Uncaught ReferenceError: address is not defined

```
* 有些时候，如果变量已经被声明了，再次赋值的时候，正确的写法也会报语法错误：
```JavaScript
// 声明变量:
var x, y;
// 解构赋值:
{x, y} = { name: '小明', x: 100, y: 200};
// 语法错误: Uncaught SyntaxError: Unexpected token =
```
这是因为JavaScript引擎把{开头的语句当作了块处理，于是=不再合法。解决方法是用小括号括起来：
```JavaScript
({x, y} = { name: '小明', x: 100, y: 200});
```
## Method
一个函数中的this指针除了obj.func()形式之外，无论位置在什么地方，其this指针为undefined
* 除非对函数对象使用apply(this_object,parameter_array)函数或者call()
```
function getAge() {...}
getAge.apply(xiaoming, [p1,p2]);
getAge.call(xiaoming, p1,p2);
```
#### map(function)
#### reduce(function(x,y),initX)   其中initX可以不要
注意使用标准函数的时候可能的默认参数
```
['1','2','3'].map(parseInt);// 结果实际上是[1,NaN,NaN];
```
#### filter(function)
#### sort(function)
sort函数默认的将所有数字转为string再进行ascii比较，但也可以自己定义比较函数
返回值为负数,0,正数分别标识小于、等于、大于