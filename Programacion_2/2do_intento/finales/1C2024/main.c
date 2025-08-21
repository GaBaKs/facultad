#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ST20 21
#define ST4 5
#define ST15 16
#define MAX 100
//ejercicio 2

typedef struct nodito{
    char idcancion[ST15];
    char titulo[ST20];
    int duracion;
    struct nodito * sig;}nodito;
typedef struct nodito * sublista;

typedef struct nodoD{
    int idp;
    sublista sub;
    struct nodoD *ant,*sig;}nodoD;

 typedef struct nodoD * PnodoD;

 typedef struct{
  PnodoD pri,ult;}TlistaD;


void recorrecola(TlistaD LP,Tcola *C){

    int X,trep=0;
    PnodoD ,act;
    TelementoC datoC,centinela;
    sublista auxS;
    int flag=0;



    centinela.playlist=-999;
    strcpy(centinela.idcancion,"");
    printf("ingrese un id de playlist");
    scanf("%d",&X);
    if (LP!=NULL){
        act=LP.pri;
        PoneC(C,centinela);
        sacaC(C,&datoC);
       while (datoC!=centinela){
            while (act!=NULL && datoC.playlist!=act->idp)
                act=act->sig;
            if (act!=NULL){
                auxS=act->sub;
                while (auxS!=NULL && (strcmp(datoC.idcancion,auxS->idcancion)!=0){
                    auxS=auxS->sig;
                }
                if (auxS!=NULL){
                    if (datoC.playlist!=X || strncmp(datoC.idcancion,"DUKI",4)!=0){
                        PoneC(C,datoC);
                        trep+=auxS->duracion;
                    }
                }
            }
            sacaC(C,&datoC);
       }
        printf("la duracion de la playlist C es de %d horas y %d minutos",duracion/3600,duracion%3660);
    }



}

//inciso b


void eliminacanciones(TlistaD LP,int X,int Y){

    sublista auxS,antS,elimS;
    PnodoD act;
    int flag=0;
    char id[ST4];
    printf("ingrese un id de interprete");
    scanf("%s",id);
    printf("Interprete: %s \n",id);
    act=LP.pri;
   while (flag!=2){
        while (act->idp!=X || act->idp!=Y)
            act=act->sig;
        printf("PLAYLIST %d \n Id cancion \t Titulo cancion \n",act->idp);
        flag++;
        antS=NULL;
        auxS=act->sub;
        while (auxS!=NULL){
            if (strncmp(auxS->idcancion,id,4)==0){      //elimino
                elimS=auxS;
                printf("%s \t %s \n",auxS->idcancion,auxS->titulo);
                if (auxS==act->sub)        //elimino la cabeza
                    act->sub=act->sub->sig;
                else
                    antS->sig=auxS->sig;
                auxS=auxS->sig;
                free(elimS);
            }
            else{
                ants=auxS;
                auxS=auxS->sig;
            }
        }
   }
}


















// ejercicio 3 (tarde 16 min en hacer las dos formas y 2 min en corregir la 2da)

    int comprueba(Tarbol a,pos p,int K,int cont,int niv){
        pos c;
        int gr=0;
        if (!nulo(p)){
            c=hijomasizq(p,a);
            while (!nulo(c)){
                gr++;
                cont+=comprueba(a,c,K,cont,niv+1);
                c=hermanoder(c,a);
            }
            if (gr!=0 && gr==niv)
                return 1;
            else
                return 0;


        }
        else return 0;
    }

   void comprueba(Tarbol a,pos p,int K,int *cont,int niv){
        pos c;
        int gr=0;
        if (!nulo(p) && (*cont)<=K){
            gr=grado(a,hijomasizq(p,a));
            if (gr!=0 && gr==niv)
                (*cont)++;
            comprueba(a,hijomasizq(p,a),K,cont,niv+1);
            comprueba(a,hermanoder(p,a),K,cont,niv);
        }

}

 int grado(Tarbol a,pos p){
     int gr=0;
    while (!nulo(p)){
        gr++;
        p=hermanoder(p,a);
    }
    return gr;
 }



 // ejercicio 4

 int verifica(Tmat mat[][MAX],int K,int N,int i,int j,int gr,grant){

    if (i<K)
            if (j<N)
                if (mat[i][j]!=0)
                    return verifica(mat,K,N,i,j+1,gr+1,grant);
                else
                    return verifica(mat,K,N,i,j+1,gr,grant);
            else
                if (grant==-1)
                    return verifica(mat,K,N,i+1,0,0,gr);
                else
                    if (grant!=gr)
                        return 0;
                    else
                        return verifica(mat,K,N,i+1,0,0,grant);
    else
        return 1;

 }

 // tarde 1:25 hs en total
