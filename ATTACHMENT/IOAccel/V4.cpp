#include <cstdio>
#include <cstdlib>
int main() {
	setvbuf(stdin,new char[1<<30],_IOFBF,1<<30);
	int X;
  scanf("%d\n", &X);
	int N=1<<20;
	for(int i=0;i<N;i++){
	   scanf("%d",&X);
	}
}
