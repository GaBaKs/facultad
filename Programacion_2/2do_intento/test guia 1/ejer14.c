#include <stdio.h>
#include <stdlib.h>


int main(){
    int N;


    printf("ingrese un valor de N \n");
    scanf("%d",&N);
    creacuadrado(N);


return 0;
}


void creacuadrado(int N){

    int i=0;
    int j;
   for (i;i<N;i++){
    printf("#");
   }
   printf("\n");

   for (j=1;j<N;j++){
        for (i=0;i<N;i++){
            if (i==0 || i==N-1)
                printf("#");
            else printf(" ");
        }
        printf("\n");
   }
   for (i=0;i<N;i++){
    printf("#");
   }

}
