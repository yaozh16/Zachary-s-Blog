#include <cstdio>
#include <cstdlib>
inline int rchar(){
	static const int buffSize=1<<12;
	static int L=0;
	static int p=0;
	static char ioBuff[buffSize];
	if(L==p){
        L=(int)fread(ioBuff,1,buffSize,stdin);
        p=0;
  }
  return ioBuff[p++];
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
