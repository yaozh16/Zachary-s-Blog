# Android学习笔记(7)Fragment
October 26, 2017 11:11 PM
## 目录
|编号|内容|
|-|-|
|1|[构造](#构造)|

## 构造
|Activity State| Fragment Callback|
|-|-|
|**Created**|onAttach(Activity)|
||onCreate()|
||onCreateView(LayoutInflater, ViewGroup,Bundle)|
||onActivityCreated(Bundle)|
|**Started**|onStart()|
|**Resumed**|onResume()|
|**Paused**|onPause()|
|**Destroyed**|onDestroyView()|
||onDestroy()|
||onDetach()|

### public View onCreateView(LayoutInflater inflater, ViewGroup container,Bundle savedInstanceState)
返回一个view作为控件给Activity

构造中可以把一个layout导入
```java
return inflater.inflate(R.layout.fragment_layout,container,false);
```

## 动态的添加、更新、以及删除Fragment
### 动态加载
```java
//这里将一个FrameLayout替换为一个Fragment
FragmentManager fm = getFragmentManager();
FragmentTransaction transaction = fm.beginTransaction();
ContentFragment frag = new ContentFragment();
transaction.replace(R.id.id_content, frag);
transaction.commit();
//相应的，可以将别的Fragment替换到这个layout上
```
### 事务操作
|操作|说明|
|-|-|
|transaction.add() |往Activity中添加一个Fragment|
|transaction.remove() |从Activity中移除一个Fragment，如果被移除的Fragment没有添加到回退栈（回退栈后面会详细说），这个Fragment实例将会被销毁|
|transaction.replace()|使用另一个Fragment替换当前的，实际上就是remove()然后add()的合体~|
|transaction.hide()|隐藏当前的Fragment，仅仅是设为不可见，并不会销毁|
|transaction.show()|显示之前隐藏的Fragment|
|transatcion.commit()|提交一个事务|









