
#include <cstdio>
#include <cstdlib>
inline char rchar(){
    return getchar();
}
inline int rint(){
    int ret=0;
    char tem=rchar();
    //while(tem>'9'||tem<'0')tem=rchar();
    while(tem<='9'&&tem>='0'){ret=ret*10+tem-'0';tem=rchar();}
    return ret;
}

int main(){
  int X;
  int N=1<<20;
  for(int i=0;i<N;i++){
      X=rint();
  }
}
