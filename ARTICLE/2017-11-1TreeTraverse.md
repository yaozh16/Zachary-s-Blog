# TreeTraverse Note

## 1. traversePre

```cpp
while(!stack.empty()){
	x=stack.pop();
	visit(x);
	stack.push(x->rc);
	stack.push(x->lc);
}
```

## 2. traverseMid

```cpp
stack.push(root);
traverseVine(stack);
while(!stack.empty()){
	x=stack.pop();
    if(x->rc){
    	stack.push(x->rc);
    	traverseVine();
    }
    visit(x);
}
```
```cpp
traverseVine(stack){
	while(stack.top())
    	stack.push(stack.top()->lc);
    stack.pop();
}
```
## 3. traversePost

```cpp
stack.push(root);
gotoHLVFL(stack);
while(!stack.empty()){
	x=stack.pop();
    if(!x)
    	continue;
    if(stack.top()!=x->parent)
    	gotoHLVFL(stack);
   	visit(x);
}
```
```cpp
goHLVFL(stack){
	while(stack.top()){
    	stack.push(stack.top()->rc);
        stack.push(stack.top()->lc);
    }
    stack.pop();
}
```
## 4. traverseLayer

```cpp
while(!queue.empty()){
	x=queue.pop();
    if(x){
    	queue.push(x->lc);
        queue.push(x->rc);
    }
}
```