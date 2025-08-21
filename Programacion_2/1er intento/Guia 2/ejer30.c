#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef car st6[6];
typedef car st10[10];
typedef car st8[8];
typedef struct{
    st6 patente;
    float velocidad;
    float velmax;
    st10 fecha;
    st8 hora;
} dato;





int procesoarch(dasdsa)

int main(){


}

int procesoarch(){
    FILE *arch;
    FILE *archb;
    dato aux;
     archb=fopen("ejer30b.dat","bw");
    if ((arch=fopen("ejer30.txt","r")) == NULL)
        printf("le pifiate flaco, el archivo de texto no va");
    else {
       fscanf("%s%d%d%s%s",&aux.patente,&aux.velocidad,&aux.velmax,&aux.fecha,&aux.hora);
       if (aux.velocidad>aux.velmax*1.2){
            fwrite(&archb,sizeof(dato),1,)

       }

    }

}

