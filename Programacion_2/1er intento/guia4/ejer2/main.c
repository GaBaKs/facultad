#include <stdio.h>
#include <stdlib.h>
#include "pila.h"






int main(){
    FILE *arch;
    TPila pila;
    TElementoP aux;
    IniciaP(&pila);
    if ((arch= fopen("ejer2.txt","r")) ==  NULL)
        printf("le pifiaste flaquito, a ver si vamos amurando");
    else {
            fscanf(arch,"%c\n",&aux);
            while (feof(arch)==0){
                poneP(&pila,aux);
                printf("%c \n",consultaP(pila));
                fscanf(arch,"%c\n",&aux);
            }

    }

return 0;
}
