#include <stdio.h>
#include <stdlib.h>
#include "pilas.h"


int main(){
    TelementoP dato;
    FILE * arch;
    Tpila P;
    IniciaP(&P);
    if (arch=fopen("datospila.TXT","r")==NULL)
           printf("error en la apertura del archivo");
    else{
         fscanf(arch,"%c",&dato);
         while (feof(arch)==0){
           PoneP(&P,dato);
           fscanf(arch,"%c",&dato);
         }


    }
}
