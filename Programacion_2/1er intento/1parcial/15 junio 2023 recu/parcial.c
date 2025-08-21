#include <stdio.h>
#include <stdlib.h>
#include "colas.h"
#define MAX8 8
#define MAX4 4


typedef struct nodoC{
    char pat[MAX8];
    char vip;
    char radio[MAX4];
    int maxpas;
    char libre;
    struct nodoC * sig;}nodoC;

 typedef struct nodoC * TlistaC;

 typedef struct{
    int cantv;
    int totpas;
 }Tvec;

 typedef struct{
    int cantpas;
    char vip;
    char radio;}bin;

 typedef struct nodo{
    char pat[MAX8];
    Tcola cola;
    struct nodo * sig;}nodo;

 typedef struct nodo * Tlista;
int cumple(TlistaC aux,bin data){

    if (aux->libre=='S' && data.cantpas<aux->maxpas && data.ip==aux->vip && (aux->radio[0]==data.radio || aux->radio[1]==bin->radio || aux->radio[2]==bin->radio))
            return 1;
    else
            return 0;
}

void recorre(TlistaC LC,Tlista L){
    FILE *arch;
    bin data;
    TlistaC auxC;
    int flag;
    if ((arch=fopen("VIAJES.DAT","rb"))==NULL)
        printf("fallo al abrir el archivo");
    else{
         fread(&data,sizeof(bin),1,arch);
         while(!feof(arch)){
             flag=0;
            if (LC!=NULL){
                auxC=LC->sig;
                while (auxC!=LC && !flag){
                    if (cumple(auxC,data)){
                        auxC->libre='N';
                        flag=1;

                    }
                    else
                        auxC=auxC->sig;
                }
                if (flag)
                    actualizaS(L,auxC->pat,data);
                else
                    printf("no se pudo asignar el viaje a ningun vehiculo");

            }
            fread(&data,sizeof(bin),1,arch);


         }
        fclose(arch);
    }
}
void actualizaS(Tlista L,char pat[MAX8],bin data){
    Tlista aux;
    aux=L;
    TelementoC auxCola;
    while (aux!=NULL && strcmp(pat,aux->pat)<0)
        aux=aux->sig;
    if (aux!=NULL && strcmp(pat,aux->pat)==0){
            auxcola.cantpas=data.cantpas;
            auxcola.vip=data.vip;
            auxcola.radio=data.radio;
            poneC(&(aux->cola),auxcola);
    }
    else
        printf("no se encontro el coche en la lista");
}


void cambiacola(Tlista L){
    int max,act;
    char pat[MAX8];
    if (L!=NULL){
        while (L!=NULL){
            act=elimina(&(L->cola));
            strcpy(L->pat,pat);
            if (act>=max)
                max=act;
            L=L->sig;
        }
        printf("la patente del auto con mas eliminaciones es %s con %d eliminaciones",pat,max);
}
}
int elimina(Tcola * aux){
    Tcola aux2;
    int cont=0;
    TelementoC dato;
    IniciaC(&aux2);
    while (!vacia(*aux)){
        SacaC(aux,&dato);
        if (dato.cantpas==0)
            cont++;
        else
            PoneC(&aux2,dato);
    }
    while (!vacia(aux2)){
        SacaC(&aux2,&dato);
        PoneC(aux,dato);
    }
    return cont;
}


void borraremis(Tlista *L,TlistaC *LC,Tvec vec[2]){
    char p[MAX8];
    Tlista act,ant;
    act=*L;
    ant=NULL;
    printf("ingrese una patente P a eliminar");
    scanf("%d",p);
    while (act!=NULL && strcmp(p,act->pat)!=0){
        ant=act;
        act=act->sig;
    }
    generaV(act->cola,vec);
    EliminaL(&L,ant,act);
    eliminaLC(&LC,p);
}


void generaV(Tcola C,Tvec vec[2]){
    TelementoC auxC;
    while (!vacia(C)){
       sacaC(&C,&auxC);
       if (auxC.radio=='U'){
            vec[0].cantv++;
            vec[0].totpas+=auxC.cantpas;
       }
       else
       if (auxC.radio=='R'){
            vec[1].cantv++;
            vec[1].totpas+=auxC.cantpas;
       }
       else{
            vec[2].cantv++;
            vec[2].totpas+=auxC.cantpas;
       }
    }
}


void eliminaL(Tlista *L,Tlista act,Tlista ant){
    if (act==*L){
        *L=(*L)->sig;
        free(act);
    }
    else{
        ant->sig=act->sig;
        free(act);
    }
}

void eliminaLC(TlistaC*LC,char p[MAX8]){
    TlistaC ant,act,aux;
    act=*LC->sig;
    if (strcmp((*LC)->pat,p)==0 && (*LC)->sig==*LC){
        *LC=NULL;
        free(act);
    }
    else
         if (strcmp((*LC)->pat,p)==0){
            while(act->sig!=*LC){
                act=act->sig;
            }
            aux=*LC;
            act->sig=*LC->sig;
            *LC=act;
            free(aux);
         }
         else{
            ant=*LC;
            while (strcmp(act->pat,p)!=0){
                ant=act;
                act=act->sig;
            }
            ant->sig=act->sig;
            free(act);
         }
}



