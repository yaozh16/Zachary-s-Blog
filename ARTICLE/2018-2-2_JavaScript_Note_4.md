# 2018-2-2 JavaScript Note 4
## 标准对象
#### Date
```JavaScript
var now = new Date();
now; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)
now.getFullYear(); // 2015, 年份
now.getMonth(); // 5, 月份，注意月份范围是0~11，5表示六月
now.getDate(); // 24, 表示24号
now.getDay(); // 3, 表示星期三
now.getHours(); // 19, 24小时制
now.getMinutes(); // 49, 分钟
now.getSeconds(); // 22, 秒
now.getMilliseconds(); // 875, 毫秒数
now.getTime(); // 1435146562875, 以number形式表示的时间戳
```
1. 创建时间对象
```JavaScript
//注意月份从0开始
var d = new Date(2015, 5, 19, 20, 15, 30, 123);
d; // Fri Jun 19 2015 20:15:30 GMT+0800 (CST)
```
2. 提取解析一个符合ISO 8601格式的字符串,再传入
```JavaScript
//字符串使用实际月份01~12，转换为Date对象后getMonth()获取的月份值为0~11
var d = Date.parse('2015-06-24T19:49:22.875+08:00');
d; // 1435146562875
```
```JavaScript
var d = new Date(1435146562875);
d.toLocaleString(); // '2015/6/24 下午7:49:22'，本地时间（北京时区+8:00），显示的字符串与操作系统设定的格式有关
d.toUTCString(); // 'Wed, 24 Jun 2015 11:49:22 GMT'，UTC时间，与本地时间相差8小时

```

#### RegExp
1. 用/.../符号之间的部分标识或者new RegExp('...')
```
var re1 = /ABC\-001/;
var re2 = new RegExp('ABC\\-001');
```
2. pattern.test(var_str)
3. var_str.split(pattern)
4. pattern.exec(var_str)分组(rank=0处仍然是匹配整体)
5. 全局搜索
```JavaScript
var s = 'JavaScript, VBScript, JScript and ECMAScript';
//下面等效于var re = new RegExp('[a-zA-Z]+Script', 'g');
var re=/[a-zA-Z]+Script/g;

// 使用全局匹配:
re.exec(s); // ['JavaScript']
re.lastIndex; // 10

re.exec(s); // ['VBScript']
re.lastIndex; // 20
```
6. 其他标识:
i:忽略大小写
m:执行多行匹配
## JSON
#### data type
number
boolean
string
null
array
object
#### 序列化
JSON.stringify(var_object,array_property=null,indentType)
第二个参数用于控制如何筛选对象的键值，如果我们只想输出指定的属性，可以传入Array
```
JSON.stringify(xiaoming, ['name', 'skills'], '  ');
```
还可以传入函数var_func(key,value)
JSON.stringify(var_object,var_func,indentType)
则相当于对object做了一个map之后再转换
#### 反序列化
JSON.parse(var_str)
JSON.parse(var_str，var_func)