# 2018-1-29 JavaScript Note
## basics
### debug
alert(variable);
console.log(variable)
### common
1. JavaScript把null、undefined、0、NaN和空字符串''视为false，其他值一概视为true
2. 'use strict';控制严格
### string
1. `...`会是多行直接输出
2. 模板变量填充
```JavaScript
`你好, ${name}, 你今年${age}岁了!`;
```
3. toUpperCase()
4. toLowerCase()
5. indexOf(var_subString)
6. substring(int_startpoint,int_trailer)
### array
1. 直接可以修改内容和length属性，没初始化为undefined
2. indexOf(var_item)
3. slice(start_rank,trailer)
4. slice(start_rank)
5. slice()
6. pop() //尾部删除
7. unshift() //头部添加
8. shift()  //头部删除
9. sort()
10.  reverse()
11. splice(start_rank, num_to_delete,...[added item])
```JavaScript
splice(2, 0 ,1,'12','asd') //example : insert 3 item
splice(2, 2 )              //example : delete 2 item
```
12. concat(another_array_to_connect)//返回新的array
13. join(connect_char)
14. map(function)
```JavaScript
var sq=function(x){
  return x*x;
}
var arr=[1,2,3,4,5,6];
var result= arr.map(sq);  //result=[1,4,9,16,25,36]
```
15. reduce(function)
```
[x1, x2, x3, x4].reduce(f) = f(f(f(x1, x2), x3), x4)
```
### 对象
1. 直接用var x={key:value;...}写
2. 可以直接delete一个属性
3. var_key_property in var_object //检测是否在对象内有该属性
4. hasOwnProperty(var_key_property). //检测是否在对象内非继承地拥有该属性
### Map和Set
#### Map
```JavaScript
var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
```
1. set(var_str_key,var_value)
2. has(var_str_key)
3. get(var_str_key)
4. delete(var_str_key)
#### Set
```JavaScript
var s2 = new Set([1, 2, 3]);
```
1. add(var)
2. delete(var)
### iterable
#### for ... of
for ... of循环只循环集合本身的元素
```
var a = [1, 2, 3];
for (var x of a)
```
#### for ... in
for ... in循环由于历史遗留问题，它遍历的实际上是对象的属性名称。
```
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x of a) {
    console.log(x); // 'A', 'B', 'C'
}
```
#### forEach
1. Array
```JavaScript
'use strict';
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    console.log(element + ', index = ' + index);
});
```
2. Map
```JavaScript
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
    console.log(value);
});
```
3. Set
```JavaScript
var a = ['A', 'B', 'C'];
a.forEach(function (element) {
    console.log(element);
});
```