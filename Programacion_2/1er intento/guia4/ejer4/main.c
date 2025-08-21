#include <stdio.h>
#include <stdlib.h>
#include "colas.h"


void ingresadatos(TCola cola);
void muestracola(TCola cola);

int main(){
    TCola cola;
    IniciaC(&cola);
    ingresadatos(cola);
    muestracola(cola);
return 0;

}


void ingresadatos(TCola cola){
 FILE* arch;
 TElementoC x;
  if ((arch=(fopen("ejer4.txt","r")))== NULL)
    printf("la lectura fallo breo");
  else {
        while (feof(arch) == 0){
            fscanf(arch,"%d",&x);
            poneC(&cola,x);
            sacaC(&cola,&x);
            printf("a%d",x);
        }
  }
}

void muestracola(TCola cola){
    TElementoC x;
   while (!VaciaC(cola)){
    sacaC(&cola,&x);
    }
}
