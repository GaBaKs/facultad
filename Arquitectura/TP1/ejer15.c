#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

    int fecha=0;
    calculafecha(&fecha);
    devuelvefecha(fecha);

}




void devuelvefecha(short int fecha){

    short int dia,mes,anio;
    //mascanio=0x007F,mascmes=0x0F00;

    dia=(fecha&0xF800) >> 11;
    printf("dia: %d\n",dia);
    mes=(fecha&0x0780) >> 7;

    anio=fecha&0x007F;
    if (anio>50)
        anio+=1900;
    else
        anio+=2000;
    printf("%d-%d-%d",anio,mes,dia);

}

void calculafecha(short int *fecha){

    int dia=10, mes=3,anio=51;

    dia=dia << 11;
    mes=mes << 7;
    *fecha=dia+mes+anio;
    printf("fecha: %d\n",*fecha);


}



