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
13. join(connnect_char)
### 对象
1. 直接用var x={key:value;...}写
2. 可以直接delete一个属性
3. var_key_property in var_object //检测是否在对象内有该属性
4. hasOwnProperty(var_key_property). //检测是否在对象内非继承地拥有该属性
### Map和Set
#### Map
1. set(var_str_key,var_value)
2. has(var_str_key)
3. get(var_str_key)
4. delete(var_str_key)
