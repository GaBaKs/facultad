#include <stdio.h>
#include <stdlib.h>


int main(){
    int N,M;

    printf("ingrese valor 1 \n");
    scanf("%d",&N);
    printf("ingrese valor 2 \n");
    scanf("%d",&M);
    printf ("el resultado de la multiplicacion es %d",llamarecursivo(N,M));

 return 0;
 }


 int llamarecursivo(int N,int M){

    if (N<=0)
        return 0;
    else{
        return M+llamarecursivo(N-1,M);


    }

}
