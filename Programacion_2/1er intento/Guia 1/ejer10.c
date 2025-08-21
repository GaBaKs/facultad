#include <stdio.h>

int main(){
 int test=3,*p2;
 int* *p;
 p2=&test;
 *p=p2;
 printf("asdasd %d",*p2);
return 0;
}
