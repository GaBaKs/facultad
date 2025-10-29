#include <stdio.h>
#include <stdlib.h>
#include <string.h>




#pragma once

#define MAX 10
#define REGISTROS 32
#define MEMORIA 16384
#define CANTCELDAS 4
#define SEGMENTOS 6
#define ENTRADAS
typedef struct TipoMKV{
    int reg[REGISTROS];           // Cantidad de registros
    unsigned char *mem;            // Cantidad de memoria
    unsigned short tabla_seg[4]; // tabla_seg[SEGMENTOS][ENTRADAS] 6 filas para los segmentos y 2 columnas para donde empieza y cuanto mide habria que cambiar bastante
    int flag;
    int tamanoRAM;
}TipoMKV;

int main(){
    TipoMKV MKV;
    int aux;
    int argc=3;
    char * argv[argc];
    argv[0]="-p";
    argv[1]="test";
    argv[2]="mario";
    argv[3]="gaby";

    int argc2;
    int argv2[200];
    int flag;

 int i=1;
    argc2=0;
    while (i<argc && strcmp(argv[i],"-p")==0)
        i++;
    if (i<argc){        // hay -p
        flag=1;
        aux=0;
        i++;
        while (i<argc){
            strcpy(MKV.mem[aux],argv[i]);
            argv2[argc2]=aux;       //aux va a ir contando el inicio de cada palabra, osea que calcula el offset
            aux+=strlen(argv[i])+2;
            argc2++;
            i++;
        }
        // guardo las direcciones despues de todos los datos
        i=0;
        while (i<argc2){
            strcpy(MKV.mem[aux],argv2[i]);
            aux+=strlen(argv2[i])+2;
            i++;
        }
    }
    for (i=0;i<aux;i++){
        printf("%c /n",MKV.mem[i]);
    }


}

