#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ST10 11
#define ST25 26



typedef struct nodito{
    char idcan[ST10];
    char titulo[ST25];
    int duracion;
    struct nodito * sig;}nodito;
typedef struct nodito * sublista;

typedef struct nodo{
    char idint[ST10];
    sublista sub;
    struct nodo * sig;}nodo;

typedef struct nodo * Tlista;

typedef struct nodoC{
    char idcan[ST10];
    char idint[ST10];
    struct nodoC * sig;}nodoC;

typedef struct nodoC * TlistaC;

typedef struct{
    char idint[ST10];
    char idcan[ST10];
    int pos;}reg;

void elimina(TlistaC * LR,TlistaC ant,TlistaC act);
void verifica(TlistaC * LR,char * NS,char idact[ST10],char idcan[ST10]);
void listacanciones(Tlista L,TlistaC * LR);
void leearch(Tlista L,TlistaC * LR,Tpila *P);
int dentroLR(TlistaC LR,reg aux);
int valida(Tlista L,reg aux);
void insertaLR(TlistaC *LR,reg aux);
void recorropila(Tpila *P,char k[ST10]);

int main(){
    TlistaC LR;
    Tlista L;
    Tpila P;
    char k[ST10];
    iniciaP(&P);
    IniciaL(&L);
    IniciaLR(&LR);
    listacanciones(L,&LR);
    leearch(L,&LR);
    printf("ingrese un interprete K");
    scanf("s",&k);
    recorropila(&P,k);
}

void elimina(TlistaC * LR,TlistaC ant,TlistaC act){
    TlistaC aux;
    if (*(LR->sig)==(*LR)){
        *LR=NULL;
    }
    else
        if (act==*LR){
            ant->sig=*(LR->sig);
            *LR=ant;

        }
        else{
            ant->sig=act->sig;
        }
     free(act);   
}


void verifica(TlistaC * LR,char * NS,char idact[ST10],char idcan[ST10]){
    TlistaC act,ant;
    if (*LR!=NULL){
        ant=*LR;
       if (strcmp(ant->idcan,idcan)==0 && strcmp(ant->idint,idact)==0){ 
            *NS=S;
            elimina(LR,ant,&LR);
        }
       else{      
        act=*(LR->sig);
        while (act->sig!=*LR && strcmp(act->idcan,idcan)!=0 && strcmp(act->idint,idact)!=0){
            ant=act;
            act=act->sig;
        }
        if (strcmp(act->idcan,idcan)==0 && strcmp(act->idint,idact)==0){
            *NS=S;
            elimina(&LR,ant,act);
        }    
        else *NS=N;
    }



}
void listacanciones(Tlista L,TlistaC * LR){
    char idact[ST10];
    Tlista auxL;
    sublista auxS;
    char NS;
    int contelim=0;
    float min=0;
    printf("ingrese un id de interprete");
    scanf("%s",idact);

    if (L!=NULL){
         auxL=L;
        while (auxL!=NULL && strcmp(idact,auxL->idint)<0)
            auxL=auxL->sig;
        if (auxL==NULL)
            printf("el interprete colocado no se encuentra en la lista.");
        else{
            printf("Interprete: %s \n",idact);
            printf("Id cancion                Titulo cancion             Eliminada \n");
            auxS=auxL->sub;
            while (auxS!=NULL){
                verifica(&LR,&NS,idact,auxS->idcan);
                printf("%s           %s               %c \n",auxS->idcan,auxS->titulo,NS);
                if (NS=='S'){
                    contelim++;
                    min+=(float)auxS->duracion/60.0;
                }
                auxS=auxS->sig;
            }
            if (contelim==0)
              printf("No se eliminaron canciones");
            else
                printf("%d canciones eliminadas (%.2f minutos)",contelim,min);    
        }

    }


}

//inciso b

void leearch(Tlista L,TlistaC * LR,Tpila *P){

    FILE * arch;
    reg aux;
    TelementoP auxP;
    if ((arch=fopen("NUEVAS.DAT","rb"))==NULL)
        printf("el archivo no pudo ser abierto");
    else{
        fread(&aux,sizeof(reg),1,arch);
        if (dentroLR(&LR,aux)){
            auxP.idintcan='';
            auxP.duracion=valida(L,aux);
           if (auxP.duracion !=0){
            strcat(auxP.idintcan,aux.idint);
            strcat(auxP.idintcan,aux.idcan);
            poneP(P,auxP);
           }  
        }
        else{
            insertaLR(LR,aux.pos);
        }    
            
    }

}

int dentroLR(TlistaC LR,reg aux){
    
    if (LR!=NULL){
        TlistaC auxC=LR->sig;
        while (auxC!=LR && (strcmp(aux.idint,auxC->idint)!=0 || srtcmp(aux.idcan,auxC->idcan)!=0))
            auxC=auxC->sig;
        if (auxC!=LR)
            return 1;
        else return 0;
    }
    else return 0;
    }

int valida(Tlista L,reg aux){
    Tlista auxL;
    if (L!=NULL){
        while (L!=NULL && (strcmp(aux.idint,L->idint)!=0 || strcmp(aux.idcan,L->sub->idcan)!=0))
            L=L->sig;
        if (L!=NULL);
            return L->duracion;
        else return 0;
    }
    else return 0;
}

void insertaLR(TlistaC *LR,reg aux){
    TlistaC nuevo;
    TlistaC ant,act;
    int postact=0;
    nuevo=(TlistaC) malloc (sizeof(nodoC));
    nuevo->idcan=aux.idcan;
    nuevo->idint=aux.idint;
    if (*LR==NULL){
        nuevo->sig=nuevo;
        *LR=nuevo;
    }
    else{
        act=*(LR->sig);
        ant=*LR;
        while (act!=*LR && posact<aux.pos){
            ant=act;
            act=act->sig;
            posact++;
        }
        if (posact<aux.pos && act==*LR){
            nuevo->sig=*(LR->sig);
            *(LR->sig)=nuevo;
            *LR=nuevo;
        }
        else{
            if (posact=aux.pos){
                nuevo->sig=act;
                ant->sig=nuevo;
            }
        }

            
    }    
}


void recorropila(Tpila *P,char k[ST10]){
 TelementoP aux;
    if (!vacia(P)){
        sacaP(P,&aux);
        recorropila(P,k);
        if (strcmp(k,aux.idint)==0)
          poneP(P,aux);
    }
}



