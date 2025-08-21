#include <stdio.h>
#include <stdlib.h>



// ejer 1: FALSO. el calculo del FE permite saber si un arbol esta balanceado o no, lo que quiere decir que solo hay una diferencia de 1 de altura entre cada rama del arbol.
// no tiene nada que ver con la eficiencia.



//ejercicio 2

typedef struct nodito{

    int num;
    struct nodito * sig;}nodito;
typedef struct nodito * sublista;

typedef struct nodo{
    int decena;
    sublista sub;
    struct nodo * sig;}nodo;
typedef struct nodo * Tlista;



void analizocorrecto(Tlista *L){

    Tlista aux,ant,elim;
    sublista auxS,antS,muevoS;
    aux=*L;
    ant=NULL;
    while (aux!=NULL){
        auxS=aux->sub;
        antS=NULL;
        while (auxS!=NULL){
            if ((auxS->num /10) != aux->decena){            // es incorrecto
                    muevoS=auxS;
                    if (aux->sub==auxS)                    //muevo el primero
                        aux->sub=aux->sub->sig;
                    else                                //es el resto
                        antS->sig=auxS->sig;     
                    auxS=auxS->sig;    
                    metoL(L,muevoS);         
            }
            else{
                antS=auxS;
                auxS=auxS->sig;
            }
            
        }
        if (aux->sub==NULL){            //elimino el nodo de L
            elim=aux;
             if (*L==aux)               //cambio la cabeza
                *L=(*L)->sig;
            else
                ant->sig=aux->sig;    
            aux=aux->sig;
            free(elim); 
        }
        ant=aux;
        aux=aux->sig;
    }
}

void metoL(Tlista *L,sublista muevoS){
    int decena=muevos->numero/10;
    sublista auxS,antS;
    Tlista aux=*L,ant=NULL,nuevo;
    while (aux!=NULL && decena<aux->decena){
        ant=aux;
        aux=aux->sig;
    }
    if (aux!=NULL && decena==aux->decena){
        
        if (muevoS->num<aux->sub->num){            //muevo la cabeza
            muevoS->sig=aux->sub;
            aux->sub=muevoS;
        }
        else{                                       //inserto en otro lado
             auxS=aux->sub;
             antS=NULL;
             while (auxS!=NULL && auxS->num<muevoS->num){
                 antS=auxS;
                 auxS=auxS->sig;
             }
             antS->sig=muevoS;
             muevoS->sig=auxS;
        }
    }    
    else{           //creo el nodo
        nuevo=(Tlista) malloc (sizeof(nodo));
        nuevo->decena=decena;
        nuevo->sub=muevoS;
        ant->sig=nuevo;
        nuevo->sig=aux;
    }

}

void informe(Tlista L){
    Tlista aux=L;
    int numero=0,contdec=0;
    sublista auxS;
    int i;
    printf("\t numeros que no han aparecido\n Decena \t Numeros de esta decena que no han aparecido\n");
   for(int decena=0;decena<10;decena++){
    printf(" %d \t",decena);
   
      if (aux!=NULL && decena==aux->decena){ 
            auxS=aux->sub;
            for (int i=0;i<10;i++){
                if (auxS!=NULL && numero==auxS->num)
                    auxS=auxS->sig;
                else
                    printf("%d , ",numero);
                numero++;   
            }   
        aux=aux->sig;     
      }
      else{             //no existe esa decena o no cumple con q es igual
            if (aux!=NULL){     //no cumple la decena
                for (i=0;i<10;i++){
                    printf("%d , ",numero);
                    numero++;
                }
              contdec++;      
            }
      }
      printf("\n");
    }
    printf("cantidad de decenas en las que no aparecio ningun numero: %d",contdec);
}



int recorroarbol(arbol a,pos p,Tcola *C,int niv,int k){

    if (!nulo(p) && niv<=k){  
        if (estaenC(info(p,a),C))
            return 1+recorroarbol(a,hijomasizq(p,a),C,niv+1,k)+recorroarbol(a,hermanoder(p,a),niv,k);
        else
            return recorroarbol(a,hijomasizq(p,a),C,niv+1,k)+recorroarbol(a,hermanoder(p,a),niv,k);
    }
    else return 0;
}

int estaenC(int dato,Tcola *C){
    TelementoC datoC;
    Tcola Caux;
    int flag=0;
    while (!vaciaC(C)){
       SacaC(C,&datoC);
       if (datoC==dato)
        flag=1;
      poneC(&Caux,datoC);
    }
    while (!vaciaC(Caux)){
        SacaC(&Caux,&datoC);
        poneC(C,datoC);
    }
    return flag;

}


void verificagrafo(Tmat mat[][MAX],int N,int i,int j,int K,int *cont,int bucle,int costoprom,int aristas){              //tarde 25 min  y 6:46 en revisar(cambie cosas)
    
    if (i<N && cont<2){
        if (j<N && mat[i][i]!=0){
    
            if (i>j){
              if(mat[i][j]!=0){
                costoprom+=mat[i][j];
                aristas++;
              }  
            }    
             else
               if(mat[j][i]!=0){
                costoprom+=mat[j][i];
                aristas++;
               }
            verificagrafo(mat,N,i,j+1,K,cont,bucle,costoprom);
        }
        else{
             if (mat[i][i]!=0 && aristas!=0 && costoprom/aristas>k)
                 (*cont)++;
              verificagrafo(mat,N,i+1,0,K,cont,0,0,0);
        }
    }

}







