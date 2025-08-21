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
    if ((arch=fopen("TEST.txt","rt"))==NULL)
        printf("error en la apertura del archivo");
    else{
        fscanf(arch,"%d ",&x);
        while (!feof(arch)){
            nuevoC=(TlistaC) malloc (sizeof(nodoC));
            nuevoC->dato=x;
            if (*LC==NULL){             //lista vacia
                nuevoC->sig=nuevoC;
                *LC=nuevoC;
                printf("meti dato a la cabeza vacia \n");
            }
            else{
                if ((*LC)->dato<x){             // cambio la cabeza
                    nuevoC->sig=(*LC)->sig;
                    (*LC)->sig=nuevoC;
                    *LC=nuevoC;
                    printf("meti dato %d a la cabeza \n",x);
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
                    printf("meti dato %d en recorrido \n",x);


                }
            }


    fscanf(arch,"%d ",&x);
        }




    fclose(arch);
    }
}

void muestralista(TlistaC LC){
    TlistaC auxC=LC;

    do{
        auxC=auxC->sig;
        printf("%d ",auxC->dato);
    }
    while (auxC!=LC);


}
