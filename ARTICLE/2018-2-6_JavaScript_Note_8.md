# 2018-2-6 JavaScript Note 8
## JQuery
### 选择器
一个选择器写出来类似$('#dom-id')
* 按ID查找
$('#id')
```JavaScript
var div = $('#abc'); // jQuery对象
var divDom = div.get(0); // 假设存在div，获取第1个DOM元素
var another = $(divDom); // 重新把DOM包装为jQuery对象
```
* 按tag查找```$('tagName')```
按tag查找只需要写上tag名称就可以了
```JavaScript
var ps = $('p'); // 返回所有<p>节点
ps.length; // 数一数页面有多少个<p>节点
```
* 按class查找```$('.className')```
* 按属性查找```$('[propName=value]')```
&emsp;&emsp;当属性的值包含空格等特殊字符时，需要用双引号括起来。
&emsp;&emsp;按属性查找还可以使用前缀查找或者后缀查找
```JavaScript
var icons = $('[name^=icon]'); // 找出所有name属性值以icon开头的DOM
// 例如: name="icon-1", name="icon-2"
var names = $('[name$=with]'); // 找出所有name属性值以with结尾的DOM
// 例如: name="startswith", name="endswith"
```

* 组合查找/多项查找(逗号分割)
* JQuery对象方法
1. find(...)//找子对象
2. css(prop,value)//设置css
3. get(rank)//第rank个(得到的是DOM对象，需要$(var)转化为JQuery对象)

* 层级选择器```$('ancestor descendant')``` 
可以是祖先和后代
* 子选择器```$('parent>child')```
必须是直属父子节点
* 过滤器```$('prop:filt-condition')```
```JavaScript
$('ul.lang li:first-child'); // 仅选出JavaScript
$('ul.lang li:last-child'); // 仅选出Lua
$('ul.lang li:nth-child(2)'); // 选出第N个元素，N从1开始
$('ul.lang li:nth-child(even)'); // 选出序号为偶数的元素
$('ul.lang li:nth-child(odd)'); // 选出序号为奇数的元素
```
* 表单相关,jQuery还有一组特殊的选择器
1. :input：可以选择```<input>```，```<textarea>```，```<select>```和```<button>```；
1. :file：可以选择```<input type="file">```，和```input[type=file]```一样；
1. :checkbox：可以选择复选框，和```input[type=checkbox]```一样；
1. :radio：可以选择单选框，和```input[type=radio]```一样；
1. :focus：可以选择当前输入焦点的元素，例如把光标放到一个```<input>```上，用```$('input:focus')```就可以选出；
1. :checked：选择当前勾上的单选框和复选框，用这个选择器可以立刻获得用户选择的项目，如```$('input[type=radio]:checked')```；
1.  :enabled：可以选择可以正常输入的```<input>```、```<select>```
    等，也就是没有灰掉的输入；
1.  :disabled：和:enabled正好相反，选择那些不能输入的。
* 此外，jQuery还有很多有用的选择器，例如，选出可见的或隐藏的元素：
```JavaScript
$('div:visible'); // 所有可见的div
$('div:hidden'); // 所有隐藏的div
```
* **方法**
1. next()/prev()    同一层级之间的对象的移动
2. find(...)
3. filter(...)    传入的是一个条件或者函数
4. serialize()转为字符串
一个jQuery对象如果包含了不止一个DOM节点，first()、last()和slice()方法可以返回一个新的jQuery对象，把不需要的DOM节点去掉
5. html()/html(...)获取/设置html
6. text()/text(...)获取/设置text
7. css(prop)/css(prop,value)获取/设置属性
例如```css('color', 'red')```
注意一个jQuery对象可以包含0个或任意个DOM对象，它的方法实际上会作用在对应的每个DOM节点上
为了和JavaScript保持一致，CSS属性可以用'background-color'和'backgroundColor'两种格式
8. addClass(className)
9. hide()/show()
可以没有参数，也可以加入msec参数控制速度
10. 获取信息
```JavaScript
// 浏览器可视窗口大小:
$(window).width(); // 800
$(window).height(); // 600

// HTML文档大小:
$(document).width(); // 800
$(document).height(); // 3500

// 某个div的大小:
var div = $('#test-div');
div.width(); // 600
div.height(); // 300
div.width(400); // 设置CSS属性 width: 400px，是否生效要看CSS是否有效
div.height('200px'); // 设置CSS属性 height: 200px，是否生效要看CSS是否有效
```
11. attr()和removeAttr()方法用于操作DOM节点的属性
```JavaScript
// <div id="test-div" name="Test" start="1">...</div>
var div = $('#test-div');
div.attr('data'); // undefined, 属性不存在
div.attr('name'); // 'Test'
div.attr('name', 'Hello'); // div的name属性变为'Hello'
div.removeAttr('name'); // 删除name属性
div.attr('name'); // undefined
```
12. prop()方法和attr()类似，但是HTML5规定有一种属性在DOM节点中可以没有值，只有出现与不出现两种(如'checked')
attr()和prop()对于属性checked处理有所不同：
```JavaScript
var radio = $('#test-radio');
radio.attr('checked'); // 'checked'
radio.prop('checked'); // true
```
prop()返回值更合理一些。不过，用is()方法判断更好：
```JavaScript
var radio = $('#test-radio');
radio.is(':checked'); // true
```
类似的属性还有selected，处理时最好用is(':selected')。
13. 操作表单
对于表单元素，jQuery对象统一提供val()方法获取和设置对应的value属性
14. append()/prepend()修改DOM结构(调用append()/prepend()传入HTML片段、原始的DOM对象、jQuery对象和函数对象)
```JavaScript
// 创建DOM对象:
var ps = document.createElement('li');
ps.innerHTML = '<span>Pascal</span>';
// 添加DOM对象:
ul.append(ps);

// 添加jQuery对象:
ul.append($('#scheme'));

// 添加函数对象:
ul.append(function (index, html) {
    return '<li><span>Language - ' + index + '</span></li>';
});
```
&emsp;```append()```把DOM添加到最后，```prepend()```则把DOM添加到最前。
如果要添加的DOM节点已经存在于HTML文档中，它会首先从文档移除，然后再添加，也就是说，用append()，你可以移动一个DOM节点。

* 把新节点插入到指定位置after()方法
* 删除DOM节点，拿到jQuery对象后直接调用remove()方法就可以了。

## 事件
#### on(event,function)
```JavaScript
var a = $('#test-link');
a.on('click', function () {
    alert('Hello!');
});
```
#### 标准事件
* 鼠标事件
click: 鼠标单击时触发；
dblclick：鼠标双击时触发；
mouseenter：鼠标进入时触发；
mouseleave：鼠标移出时触发；
mousemove：鼠标在DOM内部移动时触发；
hover：鼠标进入和退出时触发两个函数，相当于mouseenter加上mouseleave。

* 键盘事件
键盘事件仅作用在当前焦点的DOM上，通常是```<input>```和```<textarea>```。
keydown：键盘按下时触发；
keyup：键盘松开时触发；
keypress：按一次键后触发。
* 其他事件
focus：当DOM获得焦点时触发；
blur：当DOM失去焦点时触发；
change：当```<input>```、```<select>```或```<textarea>```的内容改变时触发；
submit：当```<form>```提交时触发；
ready：当页面被载入并且DOM树完成初始化后触发。
&emsp;&emsp;其中，ready仅作用于document对象。由于ready事件在DOM完成初始化后触发，且只触发一次，所以非常适合用来写其他的初始化代码。
&emsp;&emsp;初始化的几种写法:
```JavaScript
$(document).on('ready', function () {
            $('#testForm').on('submit', function () {
                alert('submit!');
            });
        });
```
```JavaScript
$(document).ready(function () {
    // on('submit', function)也可以简化:
    $('#testForm').submit(function () {
        alert('submit!');
    });
});
```
```JavaScript
$(function () {
    // init...
});
```
完全可以反复绑定事件处理函数，它们会依次执行：
```JavaScript
$(function () {
    console.log('init A...');
});
$(function () {
    console.log('init B...');
});
$(function () {
    console.log('init C...');
});
```
### 事件参数

有些事件，如mousemove和keypress，我们需要获取鼠标位置和按键的值，否则监听这些事件就没什么意义了。所有事件都会传入Event对象作为参数，可以从Event对象上获取到更多的信息.
### 取消绑定

一个已被绑定的事件可以解除绑定，通过off('click', function)实现
省略function则取消该对象所有该事件绑定函数
省略绑定类型则取消该对象所有绑定函数
### 事件触发条件
一个需要注意的问题是，事件的触发总是由用户操作引发的
JS代码修改不会导致触发，如果需要触发，则可以使用trigger函数
```JavaScript
input.trigger('change')
```
### 浏览器安全限制

在浏览器中，有些JavaScript代码只有在用户触发下才能执行，例如，window.open()函数
```JavaScript
// 无法弹出新窗口，将被浏览器屏蔽:
$(function () {
    window.open('/');
});
```
这些“敏感代码”只能由用户操作来触发：
```JavaScript
var button1 = $('#testPopupButton1');
var button2 = $('#testPopupButton2');

function popupTestWindow() {
    window.open('/');
}

button1.click(function () {
    popupTestWindow();
});

button2.click(function () {
    // 不立刻执行popupTestWindow()，100毫秒后执行:
    setTimeout(popupTestWindow, 100);
});
```
当用户点击button1时，click事件被触发，由于popupTestWindow()在click事件处理函数内执行，这是浏览器允许的，而button2的click事件并未立刻执行popupTestWindow()，延迟执行的popupTestWindow()将被浏览器拦截。

### 动画
1. hide(msec)/show(msec)/toggle(msec)
2. slideUp/slideDown/slideToggle
3. fadeIn/fadeOut/fadeToggle
4. 自定义动画animate(state,time,function_to_run_when_finished)
```JavaScript
var div = $('#test-animate');
div.animate({
    opacity: 0.25,
    width: '256px',
    height: '256px'
}, 3000, function () {
    console.log('动画已结束');
    // 恢复至初始状态:
    $(this).css('opacity', '1.0').css('width', '128px').css('height', '128px');
});
```
5. delay(msec)
## JQuery插件
### 拓展写法
```JavaScript
//例如写加亮
$.fn.highlight1=function(){
  this.css('backgroundColor', '#fffceb').css('color', '#d85030');
  return this;//为了之后能链式调用方法
}
//之后就可以
$('#test-highlight1 span').highlight1();
```
### 默认参数
使用jQuery提供的辅助方法$.extend(target, obj1, obj2, ...)，它把多个object对象的属性合并到第一个target对象中，遇到同名属性，总是使用靠后的对象的值，也就是越往后优先级越高
```JavaScript
// 把默认值和用户传入的options合并到对象{}中并返回:
var opts = $.extend({}, {
    backgroundColor: '#00a8e6',
    color: '#ffffff'
}, options);
```
```JavaScript
$.fn.highlight = function (options) {
    // 合并默认值和用户设定值:
    var opts = $.extend({}, $.fn.highlight.defaults, options);
    this.css('backgroundColor', opts.backgroundColor).css('color', opts.color);
    return this;
}

// 设定默认值:
$.fn.highlight.defaults = {
    color: '#d85030',
    backgroundColor: '#fff8de'
}
```
最终，我们得出编写一个jQuery插件的原则：
1. 给$.fn绑定函数，实现插件的代码逻辑；
2. 插件函数最后要return this;以支持链式调用；
3. 插件函数要有默认值，绑定在$.fn.```<pluginName>```.defaults上;
4. 用户在调用时可传入设定值以便覆盖默认值。
### 针对特定元素的扩展
```JavaScript
$.fn.external = function () {
    // return返回的each()返回结果，支持链式调用:
    return this.filter('a').each(function () {
        // 注意: each()内部的回调函数的this绑定为DOM本身!
        var a = $(this);
        var url = a.attr('href');
        if (url && (url.indexOf('http://')===0||url.indexOf('https://')===0)) {
            a.attr('href', '#0')
             .removeAttr('target')
             .append(' <i class="uk-icon-external-link"></i>')
             .click(function () {
                if(confirm('你确定要前往' + url + '？')) {
                    window.open(url);
                }
            });
        }
    });
}
```