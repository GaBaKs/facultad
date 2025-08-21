#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ST10 11
#define MAX 100


typedef struct nodito{
    int idc;
    char titulo[MAX];
    int duracion;
    struct nodito * sig;}nodito;
 typedef struct * nodito sublista;


typedef struct nodo{
    char idint[ST10];
    sublista sub;
    struct nodo * sig;}nodo
typedef struct nodo * Tlista;

typedef struct nodoC{
    char idint[ST10];
    int idc;
    struct nodoC * sig;}nodoC;
typedef struct nodoC * TlistaC;

//ejercicio 1       (tarde 23:41 y 5 min en revisar)

void recorreL(Tlista L,TlistaC *LC){
    int duracion=0,cont=0;
    char id[ST10];
    Tlista aux;
    sublista auxS;
    char elim;
    printf("ingrese un interprete");
    scanf("%s",id);
    buscainterprete(L,&aux,id);
    if (aux==NULL)
            printf("el interprete ingresado no existe");
    else{
        auxS=aux->sub;
        printf("interprete: %s\n ID cancion \t Titulo cancion \t Eliminada \n",id);
        while (auxS!=NULL){
            revisaLC(LC,&elim,id,auxS->idc);
            printf("%d \t %s \t %c",auxS->idc,auxS->titulo,elim);
            if (elim=='S'){
                duracion+=auxS->duracion;
                cont++;
            }
            auxS=auxS->sig;

        }
      printf("%d canciones eliminadas (%d minutos)",cont,duracion/60);
   }
}


void buscainterprete(Tlista L,Tlista * aux,char id[ST10]){
    while (L!=NULL && strcmp(L->idint,id)<0){
        L=L->sig;
    }
   if (strcmp(L->idint,id)==0)
    *aux=L;
   else
        *aux=NULL;
}

void revisaLC(TlistaC *LC,char *elim,char id[ST10],int idc){
    TlistaC act,ant;
    *elim='N';
   if ((*LC)!=NULL)
    act=(*LC)->sig;
    ant=*LC;
    do{
        if (strcmp(id,act->idint)==0 && act->idc==idc){         //elimino
            *elim='S';
            if (act==*LC){               //es la cabeza
                if (*LC==(*LC)->sig)   //es unico
                    *LC=NULL;
                else{
                    ant->sig=(*LC)->sig;
                    *LC=ant;
                }
            }
            else
                ant->sig=act->sig;
            free(act);
        }
        else{
            ant=act;
            act=act->sig;
        }

    }
    while (*LC!=NULL && act!=*LC && elim!='S');
}

//ejercicio 3           (tarde 12:40 sin contar el TDA)

void recorroP(Tpila *P,Tarbol A,pos d){
    TelementoP datoP;
    if (!vacia(*P)){
        sacaP(P,&datoP);
        recorroP(P,A,d);
        if ((strlen(datoP)%2)==1 && cumple(A,d,datoP))
            PoneP(P,datoP);

    }
}

int cumple(Tarbol A,pos p,TelementoP datoP){
    int inicial=0,ultima=0,longitud=strlen(datoP)-1;
    pos c;
    if (!nulo(p)){
        c=hijomasizq(p,A);
        while (!nulo(c) && !(inicial&&ultima)){
            if (info(c,A)==datoP[longitud])
                ultima=1;
            if (info(c,A)==datoP[0])
                inicial=1;
            c=hermanoder(c,A);
        }
      if (inicial && ultima)
            return 1;
      else
          return cumple(A,hermanoder(p,A),datoP)||cumple(A,hijomasizq(p,A),datoP);
    }
    else
        return 0;
}
// desarrollo sacaP en pilas.h

void SacaP(Tpila *P,TelementoP *x){         //tarde 2 min con 15
    Tpila elim=*P;
    if (*P!=NULL){
        *x=(*P)->dato;
        *P=(*P)->sig;
        free(elim);
    }
}



// ejercicio 4


int gradoparbosque(Tarbol A){
    int gr=0;
    Tarbol hijo;
    while (A!=NULL){
        gr+=gradoarbol(A);
        A=A->der;
    }

}
int gradoarbol(Tarbol A){
    Tarbol hijo;
    int gr=0;
    contnodos=0;
  if (A!=NULL){
    hijo=A->izq;
    while (hijo!=NULL){
        gr++;
        contnodos+=gradoarbol(hijo);
        hijo=hijo->der;
    }
    if (gr!=0 && gr%2==0)
        return contnodos+1;
    else
        return contnodos;
  }
  else return contnodos;
}


















