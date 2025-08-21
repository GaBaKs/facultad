#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pilas.h"
#define ST6 7
#define ST4 5

typedef struct{
    char cod[ST6];
    char talle;
}bin;

typedef struct nodito{
    char cod[ST6];
    char talle;
    int cant;
    struct nodito * sig;}nodito;

typedef struct nodito * sublista;

typedef struct nodo{
    int nums;
    char talles[ST4];
    int capacidad;
    sublista sub;
    struct nodo * sig}nodo;

 typedef struct nodo *  Tlista; 

int main(){
}
void cargapila(Tpila pila){
    TelementoP data;
    FILE *arch;
    iniciaP(&pila);
    if ((arch=fopen("REMERAS.DAT","rb"))==NULL)
            printf("el archivo binario no se pudo abrir correctamente");
    else{
         while (!feof(arch)){
                            fread(&data,sizeof(TelementoP),1,arch);
                            poneP(&pila,data);
         }                   
    }
    fclose(arch);
}
void inserta(Tlista *L,Tlista aux){
    if (L==NULL){
        
    }
}
void cargalista(Tlista *L){
    FILE * arch;
    Tlista aux;
    sublista actS,antS,nuevoS;
    int i,N;
    aux=(Tlista) malloc (sizeof(nodo));
    if ((arch=fopen("MAQUINAS.TXT","r")==NULL))
                printf("el archivo no pudo abrirse");
    else{
        fscanf(arch,"%d %s %d %d",&aux->nums,aux->talles,&aux->capacidad,&N);
        for (i=0;i<N;i++){
            nuevoS=(sublista) malloc (sizeof(nodito));
            fscanf(arch,"%s %c %d",nuevoS->cod,&(nuevoS->talle),&(nuevoS->cant));
            if (L->sub==NULL){
                nuevoS->sig=NULL;
                L->sub=nuevoS;
            }
            else{
                actS=L->sub;
                while (actS!=NULL && actS->talle>nuevoS->talle){
                    antS=actS;
                    actS=actS->sig;
                }
                while (actS!=NULL && strcmp(actS->cod,nuevoS->cod)<0)    
            }    
        }


    }        



}

















}
