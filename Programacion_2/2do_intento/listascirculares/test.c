#include <stdio.h>
#include <stdlib.h>



typedef struct nodoC{
    int dato;
    struct nodoC * sig;}nodoC;

typedef struct nodoC * TlistaC;


int main(){

TlistaC LC;
LC=NULL;
crealista(&LC);
muestralista(LC);
return 0;


}


void crealista(TlistaC * LC){
    TlistaC nuevoC,actC,antC;
    FILE * arch;
    int x;
    if ((arch=fopen("TEST.TXT","rt"))==NULL)
        printf("error en la apertura del archivo");
    else{
        fscanf("%d",&x);
        while (!feof(arch)){
            nuevoC=(TlistaC) malloc (sizeof(nodoC));
            nuevoC->dato=x;
            if (*LC==NULL)             //lista vacia
                nuevoC->sig=nuevoC;
            else{
                if ((*LC)->dato<x){             // cambio la cabeza
                    nuevoC->sig=(*LC)->sig;
                    (*LC)->sig=nuevoC;
                    *LC=nuevoC;
                }
                else{                           //recorro
                    actC=(*LC)->sig;
                    antC=*LC;
                    while (actC!=*LC && actC->dato<x){
                        antC=actC;
                        actC=actC->sig;
                    }
                    nuevoC->sig=actC;
                    antC->sig=nuevoC;


                }
            }


        fscanf("%d",&x);
        }




    close(arch);
    }
}

void muestralista(TlistaC LC){
    TlistaC auxC=LC->sig;

    do
        printf("%d",auxC->dato);
    while (auxC!=LC);


}
