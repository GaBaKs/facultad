#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "pilas.h"
#define MAX 100
#define ZONAS 9




typedef struct nodoD{

    int zona;
    char cod[ST4];
    Tpila P;
    struct nodoD *ant,*sig;}nodoD;

typedef struct nodoD * PnodoD;

typedef struct{
    PnodoD pri,ult;
}TlistaD;

typedef struct nodoC{
    int zona;
    int cantR;
    int cantC;
    struct nodoC * sig;}nodoC;
    
typedef struct nodoC * TlistaC;

typedef struct{
    int cantR;
    int cantC;
}Tvec;


    void cantradares(TlistaD LD){
            int cont=0;
            int flag;
            PnodoD auxD;
            auxD=LD.pri;
            while (auxD!=NULL){
                flag=0;
                cumpleP((auxD->P),&flag);
                if (auxD->zona % 2 ==0 && auxD.cod[0]=='R' && flag)
                    cont++;
                auxD=auxD->sig;
            }
            printf("la cantidad de radares que hicieron infracciones el 19/12 es %d",cont);
    }

    void cumpleP(Tpila *P,int *flag){
        
        TelementoP datoP;
        if (!vacia(p)){
            SacaP(P,&datoP);
            if (datoP.fecha[0]=='1' && datoP.fecha[1]=='2' && datoP.fecha[2]=='1' && datoP.fecha[3]=='9')
                (*flag)=1;
            else
                cumpleP(P,flag);
            PoneP(P,datoP);
        }
    }


    void iniciovec(Tvec vec[ZONAS]){
        for (int i=0;i<10;i++){
            vec[i].cantR=0;
            vec[i].cantC=0;
        }


    }

    void recorroLD(TlistaD LD,Tvec vec[ZONAS]){

        PnodoD auxD=LD.pri;
        iniciovec(vec);

        while (auxD!=NULL){
            if (auxD->cod[0]=='C')
                vec[(auxD->zona)-1].cantC+=cantinfra(auxD->P);
            else
                vec[(auxD->zona)-1].cantR+=cantinfra(auxD->P);

            auxD=auxD->sig;
        }


    }




    void generoLC(TlistaC *LC,Tvec vec[ZONAS]){

        *LC=NULL;
        int suma;
        TlistaC actC,nuevoC,antC;
        for (int i=0;i<ZONAS;i++){
          if (vec[i].cantC!=0 && vec[i].cantR!=0){  
            nuevo=(TlistaC) malloc (sizeof(nodoC));
            nuevo->zona=i+1;
            nuevo->cantR=vec[i].cantR;
            nuevo->cantC=vec[i].cantC;
            if (*LC==NULL){
                nuevo->sig=nuevo;
                *LC=nuevo;
            }
            else{
                if ((vec[i].cantC+vec[i].cantR)>((*LC)->cantC+(*LC)->cantR)){
                    nuevo->sig=(*LC)->sig;
                    (*LC)->sig=nuevo;
                    *LC=nuevo;
                }
                else{
                    antC=*LC;
                    actC=(*LC)->sig;
                    while (actC!=*LC && ((actC->cantR+actC->cantC)<(nuevo->cantC+nuevo->cantR)){
                        antC=actC;
                        actC=actC->sig;
                    }
                    nuevo->sig=actC;
                    antC->sig=nuevo;
                }
            } 
          }    
        }


    }




































//ejercicio 3

    int cadlongimp(arbol a,pos p,int niv){

        if (!nulo(p)){
            if ((niv % 2 ==1) && cumple(a,p))
                return 1+cadlongimp(a,hermanoder(p,a),niv)+cadlongimp(a,hijomasizq(p,a),niv+1);
            else
                return cadlongimp(a,hermanoder(p,a),niv)+cadlongimp(a,hijomasizq(p,a),niv+1);
        }
        else
            return 0;


    }

    int cumple(arbol a,pos p){
        int longitud=strlen(info(p,a));
        char palabra[MAX]=info(p,a);
        if (longitud % 2 ==1 && (esvocal(palabra[0]) && esvocal(palabra[longitud-1]))
            return 1;
        else
            return 0;

    }

    int esvocal(char a){
        a=tolower(a);
        if (a=='a' ||a=='e' ||a=='i' ||a=='o' ||a=='u')
            return 1;
        else
            return 0;
    }

    //ejercicio 4

    int recorreabb(arbol a,int gr){

        if (a!=NULL){
            if (gr==a->dato)
                return 1;
            else
                if (gr>a->dato)
                    return recorreabb(a->der,gr);
                else
                    return recorreabb(a->izq,gr);
        }
        else
            return 0;

    }


    int recorremat(arbol a,Tmat G,int N,int i,int j,int gr){

        if (j<N){
            if (i<N && G[j][j]!=0){
                if (G[i][j]!=0)
                    return recorremat(a,G,N,i+1,j,gr+1);
                else
                    return recorremat(a,G,N,i+1,j,gr);
            }
            else{
                if (G[j][j]==0)
                    return recorremat(a,G,N,0,j+1,0);
                else{
                    if (recorreabb(a,gr))
                        return recorremat(a,G,N,0,1,0);
                    else
                        return 0;
                }
            }
        }
        return 1;

    }