#include <stdio.h>
#include <stdlib.h>


int suma(int i, int* valores);
int producto(int i,int* valores);

int main(){
   int i=3;
   int aux;
   int* valores = (int*) malloc(i * sizeof(int));

  if (valores==NULL){
    printf("algo malio sal \n");
    free(valores);
    return 1;
  }
  else {
   for(int n=0;n<i;n++){
        printf("ingrese un numero %d\n",n);
        scanf("%d",&aux);
        valores[n]=aux;
        }
    printf("la suma de los 3 valores ingresados es %d \n",suma(i,valores));
    printf("el producto de los 3 valores ingresados es %d \n",producto(i,valores));
    free(valores);
    return 0;
    }
}

int suma(int i, int* valores){
 int auxsuma=0;
  for (int n=0;n<i;n++){
    printf("%d \t",auxsuma);
    auxsuma+=valores[n];
  }
  return auxsuma;
}


int producto(int i,int* valores){
    int acum=1;
    for(int n=0;n<i;n++){
       acum*=valores[n];


    }
    return acum;
}
