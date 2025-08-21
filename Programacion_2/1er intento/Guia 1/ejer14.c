#include <stdio.h>

void cuadrado(int *p){
   for (int i=1;i<=*p;i++){
      printf("#");
   }
   printf("\n");
   for(int j=2;j<*p;j++){

        for(int i=1;i<=*p;i++){
            if((i==1) || (i==*p))
             printf("#");
            else printf(" ");
        } printf("\n");
    }
    for (int i=1;i<=*p;i++){
      printf("#");
    }

}
 int main(){
    int N=100;
    int *p;
    p = &N;
    printf("%d %d",*p,p);
    cuadrado(*p);
   return 0;
}
