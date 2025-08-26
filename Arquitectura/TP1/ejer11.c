#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){


    int nro=10;
    char string[(sizeof(int)*8) + 1];
    string[(sizeof(int)*8) + 1]='\0';
    ejer11(nro,string);
    printf("%X = %s", nro, string);

    return 0;



}

void ejer11(int nro,char string[]){

    int tamano= (sizeof(int) *8); //tamano maximo en bits de un int;
    int masc= 1;
    for (int i=0;i<tamano;i++){
        masc= 1 << (tamano-1-i);
        string[i]=(nro&masc)? '1' : '0';



    }

}
