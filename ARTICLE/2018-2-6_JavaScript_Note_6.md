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
修改CSS也是经常需要的操作。DOM节点的style属性对应所有的CSS，可以直接获取或设置。因为CSS允许font-size这样的名称，但它并非JavaScript有效的属性名，所以需要在JavaScript中改写为 **驼峰式命名** fontSize
```JavaScript
// 获取<p id="p-id">...</p>
var p = document.getElementById('p-id');
// 设置CSS:
p.style.color = '#ff0000';
p.style.fontSize = '20px';
p.style.paddingTop = '2em';
```
### 插入DOM
#### 移动
```HTML
<!-- HTML结构 -->
<p id="js">JavaScript</p>
<div id="list">
    <p id="java">Java</p>
    <p id="python">Python</p>
    <p id="scheme">Scheme</p>
</div>
```
把```<p id="js">JavaScript</p>```添加到```<div id="list">```的最后一项：
```JavaScript
var
    js = document.getElementById('js'),
    list = document.getElementById('list');
list.appendChild(js);
```
#### 新建
```JavaScript
haskell = document.createElement('p');
haskell.id = 'haskell';
haskell.innerText = 'Haskell';
list.appendChild(haskell);
```
或者
```JavaScript
var d = document.createElement('style');
d.setAttribute('type', 'text/css');
d.innerHTML = 'p { color: red }';
document.getElementsByTagName('head')[0].appendChild(d);
```
#### insertBefore
插入到指定元素之前
```JavaScript
parentElement.insertBefore(newElement, referenceElement);
```
### 删除DOM
```JavaScript
parentElement.removeChild(childElement);
```
children属性是一个只读属性，并且它在子节点变化时会实时更新
## 操作表单
HTML表单的输入控件主要有以下几种：
* 文本框，对应的```<input type="text">```，用于输入文本；
* 口令框，对应的```<input type="password">```，用于输入口令；
* 单选框，对应的```<input type="radio">```，用于选择一项；
* 复选框，对应的```<input type="checkbox">```，用于选择多项；
* 下拉框，对应的```<select>```，用于选择一项；
* 隐藏文本，对应的```<input type="hidden">```，用户不可见，但表单提交时会把隐藏文本发送到服务器。
### 获取值
如果我们获得了一个```<input>```节点的引用，就可以直接调用inputElement.value获得对应的用户输入值
### 设置值
设置值和获取值类似
* 对于text、password、hidden以及select，直接设置value就可以
* 对于单选框和复选框，设置checked为true或false即可。
### HTML5控件
HTML5新增了大量标准控件，常用的包括date、datetime、datetime-local、color等，它们都使用```<input>```标签
```HTML
<input type="date" value="2015-07-01">
<input type="datetime-local" value="2015-07-01T02:03:04">
<input type="color" value="#ff0000">
```
### 提交表单
JavaScript可以以两种方式来处理表单的提交（AJAX方式在后面章节介绍）。
* 方式一是通过<form>元素的submit()方法提交一个表单，例如，响应一个<button>的click事件，在JavaScript代码中提交表单：
```HTML
<!-- HTML -->
<form id="test-form">
    <input type="text" name="test">
    <button type="button" onclick="doSubmitForm()">Submit</button>
</form>

<script>
function doSubmitForm() {
    var form = document.getElementById('test-form');
    // 可以在此修改form的input...
    // 提交form:
    form.submit();
}
</script>
```
* 第二种方式是响应<form>本身的onsubmit事件，在提交form时作修改：
```HTML
<!-- HTML -->
<form id="test-form" onsubmit="return checkForm()">
    <input type="text" name="test">
    <button type="submit">Submit</button>
</form>

<script>
function checkForm() {
    var form = document.getElementById('test-form');
    // 可以在此修改form的input...
    // 继续下一步:
    return true;
}
</script>
```
注意要return true来告诉浏览器继续提交，如果return false，浏览器将不会继续提交form，这种情况通常对应用户输入有误，提示用户错误信息后终止提交form。
* 一般利用hidden传输口令和MD5后的密码等，而原本用户输入的没有name属性的```<input>```的数据不会被提交
```HTML
<!-- HTML -->
<form id="login-form" method="post" onsubmit="return checkForm()">
    <input type="text" id="username" name="username">
    <input type="password" id="input-password">
    <input type="hidden" id="md5-password" name="password">
    <button type="submit">Submit</button>
</form>

<script>
function checkForm() {
    var input_pwd = document.getElementById('input-password');
    var md5_pwd = document.getElementById('md5-password');
    // 把用户输入的明文变为MD5:
    md5_pwd.value = toMD5(input_pwd.value);
    // 继续下一步:
    return true;
}
</script>
```

### 操作文件
&emsp;在HTML表单中，可以上传文件的唯一控件就是```<input type="file">```。
&emsp;注意：当一个表单包含```<input type="file">```时，表单的enctype必须指定为multipart/form-data，method必须指定为post，浏览器才能正确编码并以multip00art/form-data格式发送表单的数据。
&emsp;出于安全考虑，浏览器只允许用户点击```<input type="file">```来选择本地文件，用JavaScript对```<input type="file">```的value赋值是没有任何效果的。当用户选择了上传某个文件后，JavaScript也无法获得该文件的真实路径
&emsp;通常，上传的文件都由后台服务器处理，JavaScript可以在提交表单时对文件扩展名做检查，以便防止用户上传无效格式的文件
```JavaScript
var f = document.getElementById('test-file-upload');
var filename = f.value; // 'C:\fakepath\test.png'
if (!filename || !(filename.endsWith('.jpg') || filename.endsWith('.png') || filename.endsWith('.gif'))) {
    alert('Can only upload image file.');
    return false;
}
```
#### File API

由于JavaScript对用户上传的文件操作非常有限，尤其是无法读取文件内容，使得很多需要操作文件的网页不得不用Flash这样的第三方插件来实现。

随着HTML5的普及，新增的File API允许JavaScript读取文件内容，获得更多的文件信息。

HTML5的File API提供了File和FileReader两个主要对象，可以获得文件信息并读取文件。
```JavaScript
var
    fileInput = document.getElementById('test-image-file'),//<input>
    info = document.getElementById('test-file-info'),//<p>
    preview = document.getElementById('test-image-preview');//<div>
// 监听change事件:
fileInput.addEventListener('change', function () {
    // 清除背景图片:
    preview.style.backgroundImage = '';
    // 检查文件是否选择:
    if (!fileInput.value) {
        info.innerHTML = '没有选择文件';
        return;
    }
    // 获取File引用:
    var file = fileInput.files[0];
    // 获取File信息:
    info.innerHTML = '文件: ' + file.name + '<br>' +
                     '大小: ' + file.size + '<br>' +
                     '修改: ' + file.lastModifiedDate;
    if (file.type !== 'image/jpeg' && file.type !== 'image/png' && file.type !== 'image/gif') {
        alert('不是有效的图片文件!');
        return;
    }
    // 读取文件:
    var reader = new FileReader();
    reader.onload = function(e) {
        var
            data = e.target.result; // 'data:image/jpeg;base64,/9j/4AAQSk...(base64编码)...'            
        //显示预览
        preview.style.backgroundImage = 'url(' + data + ')';
    };
    // 以DataURL的形式读取文件:
    reader.readAsDataURL(file);
});
```