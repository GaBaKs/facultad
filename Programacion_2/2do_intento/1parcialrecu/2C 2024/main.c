#include <stdio.h>
#include <stdlib.h>
#define ST3 4
#define ST30 31
#define ST20 21



typedef struct nodito{

    int hora;       //ordenado
    char cod[ST3];    // se repite
    struct nodito * sig;}nodito;


typedef struct nodito * Sublista;

typedef struct nodoC{
    int nump;       //ordenado
    Sublista sub;
    struct nodoC * sig;}nodoC;

typedef struct nodoC * TlistaC;


typedef struct nodo{
    char cod[ST3];  //no se repite
    char nombre[ST30];
    char constru[ST20];   //aparece dos veces
    Tpila P;    //tiempos de vuelta de corredor el mejor tiempo esta arriba
}nodo;

typedef struct nodo * Tlista;


}

void cargaP(TlistaC LCP,int P){         //inciso a

    TlistaC antC,actC,nuevoC;
    sublista actS,nuevoS;
    FILE * arch;

    antC=LCP;
    actC=LCP->sig;
    nuevoC=(TlistaC) malloc (sizeof(nodoC));
    nuevoC->nump=P;
    while (actC!=LCP && P<actC->nump){      //encuentro donde poner a p
        antC=actC;
        actC=actC->sig;
    }
    antC->sig=nuevoC;
    nuevoC->sig=actC;
    nuevoC->sub=NULL;
    if (arch=fopen("MEDICIONES.TXT","rt")==NULL)
        printf("hubo un error en la apertura del archivo");
    else{
        nuevoS=(sublista) malloc (sizeof(nodito));
            nuevoS->sig=NULL;
        fscanf("%d %s",&nuevoS->hora,nuevoS->cod);
        while (!feof(arch)){        //cargo la sublista
            if (nuevoC->sub==NULL){          //ingreso a la cabeza
                nuevoC->sub=nuevoS;

            }
            else
                actS->sig=nuevoS;
            actS=nuevoS;
            nuevoS=(sublista) malloc (sizeof(nodito))
            nuevoS->sig=NULL;
            fscanf("%d %s",&nuevoS->hora,nuevoS->cod);

        }
    }

fclose(arch);

}



void cargatiempo(TlistaC LCP,Tlista LSC){
    sublista auxS;
    Tpila Paux;
    Tlista aux;
    int numv=0;
    int t0,t1,tvuelta;
    char C[ST3];
    TelementoP datoP;
    printf("ingrese un codigo de competidor");
    scanf("%s",C);
    datoP.numv=0;
    aux=LSC;
    while (aux!=NULL && strcmp(C,aux->cod)!=0)
        aux=aux->sig;
    if (aux!=NULL){                         //existe C
        auxS=LCP->sub;
        t1=0;
        while (auxS!=NULL){                 //recorro meta
            if (strcmp(auxS->cod,C)==0){    //encuentro fin de vuelta de C
                t0=t1;
                t1=auxS->hora;
                datoP.tvuelta=t1-t0;
                datoP.numv++;
                meteP(aux->P,datoP);
            }
        auxS=auxS->sig;
        }
        printf("el mejor tiempo del piloto %s de la escuderia %s es de %d segundos",aux->nombre,aux->constru,consultaP(aux->P));
    }
    else
        printf("no existe el corredor C");

}

void meteP(Tpila *P,TelementoP datoP){
    TelementoP aux;
     if (!vacia(*P)){
        sacaP(P,&aux);
        if (aux.tvuelta<datoP.tvuelta)
            poneP(P,datoP);
        else
            meteP(P,datoP);
        poneP(P,aux);
    }
    else
        poneP(P,datoP);
}















void descalificados(TlistaC LCP,Tlista LSC,char X[ST20]){             //inciso c

    int corredor=0;
    Tlista aux;
    TlistaC auxC;
    sublista auxS,antS,elimS;
    char cod1[ST3],cod2[ST3];

    aux=LSC;
    while (corredor<2){                     // encuentro los dos cod de corredor
        if (strcmp(X,aux->constru)==0){
            if (corredor==0)
                strcpy(cod1,aux->cod);
            else
                strcpy(cod2,aux->cod);
             corredor++;
        }
        aux=aux->sig;

    }
    auxC=LCP->sig;
    while (auxC!=LCP){              // recorro LC
        auxS=auxC->sub;
        antS=NULL;
        while (auxS!=NULL){         //recorro sublista
            if (strcmp(auxS->cod,cod1)==0 || strcmp(auxS->cod,cod2)==0){                    // es igual a alguno de los cod d piloto?
                if (auxS==auxC->sub){               //es la cabeza
                    elimS=auxC->sub;
                    auxS=auxS->sig;
                    auxC->sub=auxS;
                }
                else{                       // no es la cabeza
                    antS->sig=auxS->sig;
                    elimS=auxS;
                    auxS=auxS->sig;
                }
                free(elimS);
            }
            else{
                antS=auxS;
                auxS=auxS->sig;
            }

        }
    auxC=auxC->sig;
    }


}
























