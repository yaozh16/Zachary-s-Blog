# 2018-2-6 JavaScript Note 6
## 浏览器
#### 浏览器对象
##### 1. window
&emsp;window对象有innerWidth和innerHeight属性，可以获取浏览器窗口的内部宽度和高度。内部宽高是指除去菜单栏、工具栏、边框等占位元素后，用于显示网页的净宽高。
&emsp;对应的，还有一个outerWidth和outerHeight属性，可以获取浏览器窗口的整个宽高
##### 2. navigator
navigator对象表示浏览器的信息，最常用的属性包括：
* navigator.appName：浏览器名称；
* navigator.appVersion：浏览器版本；
* navigator.language：浏览器设置的语言；
* navigator.platform：操作系统类型；
* navigator.userAgent：浏览器设定的User-Agent字符串

**使用短路运算符||计算，少用if**
```JavaScript
var width = window.innerWidth || document.body.clientWidth;
```
##### 3. screen
screen对象表示屏幕的信息，常用的属性有：
* screen.width：屏幕宽度，以像素为单位；
* screen.height：屏幕高度，以像素为单位；
* screen.colorDepth：返回颜色位数，如8、16、24。
##### 4. location
location对象表示当前页面的URL信息。例如，一个完整的URL
```URL
http://www.example.com:8080/path/index.html?a=1&b=2#TOP
```
可以用location.href获取。要获得URL各个部分的值，可以这么写：
```JavaScript
location.protocol; // 'http'
location.host; // 'www.example.com'
location.port; // '8080'
location.pathname; // '/path/index.html'
location.search; // '?a=1&b=2'
location.hash; // 'TOP'
```
要加载一个新页面，可以调用 location.assign()。
如果要重新加载当前页面，调用 location.reload() 方法非常方便。
##### 5. document
document对象表示当前页面。由于HTML在浏览器中以DOM形式表示为树形结构，document对象就是整个DOM树的根节点。

* document的title属性是从HTML文档中的<title>xxx</title>读取的，但是可以动态改变：
```JavaScript
document.title = '努力学习JavaScript!';
```
* 用document对象提供的getElementById()和getElementsByTagName().、document.getElementsByClassName()可以按ID获得一个DOM节点和按Tag名称、按CSS的Class名称获得一组DOM节点：
```JavaScript
var menu = document.getElementById('drink-menu');
menu.tagName; // 'DL'

var drinks = document.getElementsByTagName('dt');
s = '提供的饮料有:';
for (i=0; i<drinks.length; i++) {
    s = s + drinks[i].innerHTML + ',';
}
console.log(s);
```
* document对象还有一个cookie属性，可以获取当前页面的Cookie。

&emsp;如果引入的第三方的JavaScript中存在恶意代码，则www.foo.com网站将直接获取到www.example.com网站的用户登录信息。
&emsp;为了解决这个问题，服务器在设置Cookie时可以使用httpOnly，设定了httpOnly的Cookie将不能被JavaScript读取。这个行为由浏览器实现，主流浏览器均支持httpOnly选项，IE从IE6 SP1开始支持。
&emsp;为了确保安全，服务器端在设置Cookie时，应该始终坚持使用httpOnly。
##### 6. history
history对象保存了浏览器的历史记录，JavaScript可以调用history对象的 __back()__ 或 __forward ()__ ，相当于用户点击了浏览器的“后退”或“前进”按钮。

### 操作DOM
##### 获取节点
1. getElementByXXX函数
```JavaScript
var node = document.getElementById('test-div').getElementsByClassName('red');
node.firstElementChild;//获取节点node下第一个子节点
node.lastElementChild;//获取节点node下最后一个子节点
node.children;// 获取节点node下的所有直属子节点:
```
2. querySelector()与querySelectorAll()
```JavaScript
// 通过querySelector获取ID为q1的节点：
var q1 = document.querySelector('#q1');

// 通过querySelectorAll获取q1节点内的符合条件的所有节点：
var ps = q1.querySelectorAll('div.highlighted > p');

```
### 修改DOM
1. innerText
1. innerHTML
1. style
修改CSS也是经常需要的操作。DOM节点的style属性对应所有的CSS，可以直接获取或设置。因为CSS允许font-size这样的名称，但它并非JavaScript有效的属性名，所以需要在JavaScript中改写为驼峰式命名fontSize
```JavaScript
// 获取<p id="p-id">...</p>
var p = document.getElementById('p-id');
// 设置CSS:
p.style.color = '#ff0000';
p.style.fontSize = '20px';
p.style.paddingTop = '2em';

```