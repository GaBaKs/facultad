#include <stdio.h>

 int main(){
  unsigned int suma=0,num;
  printf("ingrese un numero(0 para terminar) \n");
  scanf("%d", &num);

  while (num!=0) {
    suma +=num;
    printf("ingrese un numero(0 para terminar) \n");
    scanf("%d", &num);
  }

  printf("el total de la suma es de %d",suma);
 return 0;

 }
