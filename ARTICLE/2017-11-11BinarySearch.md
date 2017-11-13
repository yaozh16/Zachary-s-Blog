# Search

## BinarySearch

###  code

```cpp
int lo=0,hi=_size;
while(lo<hi){
  int mi=(lo+hi)>>1;
  if(e<data[mi])
    hi=mi;
  else
    lo=mi+1;
}
return --lo;
```

### 规则

对于e始终有$e< data[hi]$与$data[lo-1]\le e$，最终结束时有$data[lo-1]\le e< data[hi]=data[lo]$

