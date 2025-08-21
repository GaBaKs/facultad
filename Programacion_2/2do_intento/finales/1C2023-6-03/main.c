#include <stdio.h>
#include <stdlib.h>
#define ST6 7
#define ST8 9
#define ST10 11
#include "fechas.h"


// ejercicio 2

typedef struct nodito{
    char empresa[ST10];
    int rol;
    short int meses;
    struct nodito * sig;}nodito;

typedef struct nodito * sublista;



typedef struct nodo{
    char id[ST6];
    int rol;
    char fecha[ST8];
    sublista sub;
    struct nodo * sig;}nodo;

typedef struct nodo * Tlista;    

typedef struct{
    char id[ST6];
    char empresa[ST10];
    int rol;
    char termino;
}Tarch;

void actualizalista(Tlista L){
    FILE *arch;
    Tarch datoarch;
    Tlista aux;
    sublista nuevoS,actS,antS;
    if ((arch==fopen("FEBRERO.TXT","rt"))==NULL)
        printf("error en la apertura del archivo");
    else{

        fscanf("%s %s %d %c",(datoarch.id),(datoarch.empresa),&(datoarch.rol),&(datoarch.termino));
        aux=L;
        while (!feof(arch)){
            if (aux!=NULL){
                while (aux!=NULL && strcmp(aux.id,datoarch.id)<0)
                    aux=aux->sig;
                if (datoarch.termino=='N'){
                    aux->rol=rol;
                }
                else{
                    nuevoS=(sublista) malloc (sizeof(nodito));
                    strcpy(nuevoS->empresa,datoarch.empresa);
                    nuevoS->rol=rol;
                    nuevoS->meses=CANTM(aux->fecha,"202302");
                    if (aux->sub!=NULL){
                     if (strcmp(aux->sub->empresa,nuevoS->empresa)==0){
                        nuevoS->sig=aux->sub;
                        aux->sub=nuevoS;
                     }
                     else{  
                        actS=aux->sub;
                        antS=NULL;
                        while (actS!=NULL && strcmp(actS->empresa,nuevoS->empresa)<0){
                            antS=actS;
                            actS=actS->sig;
                        }
                        antS->sig=nuevoS;
                        nuevoS->sig=actS;
                     }   
                    }
                }
                fscanf("%s %s %d %c",(datoarch.id),(datoarch.empresa),&(datoarch.rol),&(datoarch.termino));
            }
            

        }
        fclose(arch);


    }
}

void eliminoEP(Tlista L,char E[ST10],char P[ST6]){
    int cont=0;
    Tlista aux=L;
    sublista actS,antS,elimS;

    while (aux!=NULL && strcmp(aux->id,P)<0)
        aux=aux->sig;
    if (aux!=NULL){
        antS=NULL;
        actS=aux->sub;
        while (actS!=NULL && strcmp(actS->empresa,E)<=0){
                if (strcmp(actS->empresa,E)==0){        //elimino
                    elimS=actS;
                    cont++;
                    if (actS==aux->sub)
                        aux->sub=aux->sub->sig;
                    else
                        antS->sig=actS->sig;
                    actS=actS->sig;
                    free(elimS);
                        
                }
                else{
                    antS=actS;
                    actS=actS->sig;
                }
        }
        printf("se ha incluido la participacion de E y P en %d proyectos",cont);
    }    
    else
        printf("no existe la persona %s en la lista",P);

}


// el c te la debo

// ejercicio 3

    int recorroarbol(TarbolN an,pos p,Tarbol ab,int K){
        int cont=0;
        int cantclaves;
        while (ab!=NULL){
            cantclaves=cuentaclaves(ab->izq)+1;
            cont+=esta(an,p,K,1,cantclaves);
            ab=ab->der;
        }
        return cont;


    }

   int cuentaclaves(Tarbol ab){
        if (ab!=NULL)
            return 1+cuentaclaves(ab->izq)+cuentaclaves(ab->der);
        else
            return 0;  
    
   }
   
   
   int esta(TarbolN an,pos p,int K,int niv,int cantclaves){

        if (!nulo(p) && niv<=K){
            if (niv==K){
                if (info(p,an)==cantclaves)
                    return 1;
                else return esta(an,hermanoder(p,an),K,niv,cantclaves);

            }
            else   
                return esta(an,hermanoder(p,an),K,niv,cantclaves)||esta(an,hijomasizq(p,a),K,niv+1,cantclaves);
        }
        else
            return 0;        
   }


   int recorropila(Tpila *P,Tmat mat,int N){
    TelementoP datoP;
        if (!vacia(P)){
            SacaP(P,&datoP);
            if (datoP.G==gr(mat,N,datoP))
                return recorropila(P,mat,N);
            else
                return 0;


        }
        else
         return 1;


   }

   int gr(Tmat mat,int N,TelementoP datoP){
    int cont=0;
    int i=(datoP.vert)-1;

   for (int j=0;j<N;J++){
     if (mat[i][j]!=0)
        cont++;
   }
   return cont;



