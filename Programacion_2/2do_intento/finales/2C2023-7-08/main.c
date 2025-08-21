#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100

typedef struct nodoD{
        char cad[MAX];
        struct nodoD * sig;}nodoD;

typedef struct nodoD * PnodoD;

typedef struct{
    PnodoD pri,ult;
}TlistaD;

// la pila tiene int E y char C
typedef struct{
    char cad[MAX];
    int vocales,consonantes;
}Tarch;

int Cinicial(TlistaD LD,char C){        //tarde 12 min en el a

    PnodoD aux;
    int cont=0;
   if (LD!=NULL){
    if ((LD.ult)->cad[0]<=C)
       if ((LD.ult)->cad[0]<C)
        return 0;
       else{
            aux=LD.ult;
           while (aux!=NULL && aux->cad[0]==C)
                cont++;
           aux=aux->sig;
       }
    else{
        aux=LD.pri;

        while (aux!=NULL && aux->cad[0]<=C){
                cont++;
            aux=aux->sig;
        }
    }
     return cont;
   }
   else return 0;
}

void actualizopila(Tpila *P,TlistaD LD){
    TelementoP datoP;
    if (!vacia(P)){
        SacaP(P,&datoP);
        datoP.E=Cinicial(LD,datoP.C);
        actualizopila(P,LD);
        PoneP(P,datoP);
    }
}


void eliminaL(TlistaD *LD,Tpila P){         //tarde 27 min en el b
    FILE * arch;
    PnodoD aux,elim;
    Tarch datoarch;
    int vocales;
    int consonantes;
   if ((arch=fopen("RESUMEN.DAT","wb"))==NULL)
        printf("error en la apertura del archivo");
   else{
          aux=LD->pri;
          while (aux!=NULL){
            if (!estainicial(aux->cad[0],P)){      //elimino
                cuentaletras(aux->cad,0,0);      //mando vocales y consonantes
                strcpy(datoarch.cad,aux->cad);
                datoarch.vocales=vocales;
                datoarch.consonantes=consonantes;
                fwrite(&datoarch,sizeof(Tarch),1,arch);
                //eliminacion
                elim=aux;
                if (LD->pri==LD->ult){       //si es unico
                    LD->pri=NULL;
                    LD->ult=NULL;
                }
                else
                     if (LD->pri==aux){                       //si es el 1ro
                        LD->pri=LD->pri->sig;
                        LD->pri->ant=NULL;
                     }
                     else
                         if (LD->ult==aux){                       //si es el ult
                            LD->ult=LD->ult->ant;
                            LD->ult->sig=NULL;
                         }
                        else{                           //esta en el medio
                            aux->sig->ant=aux->ant;
                            aux->ant->sig=aux->sig;
                        }

                aux=aux->sig;
                free(elim);
            }
            else
                aux=aux->sig;

        }
    fclose(arch);
   }
}

int estainicial(char C,Tpila P){
    TelementoP datoP;
    Tpila Paux;
    int flag;
   if (!vacia(P)){
    SacaP(&P,&datoP);
    while (!vacia(P) && datoP.C!=C){
        PoneP(&Paux,datoP);
        SacaP(&P,&datoP);
    }
    if (datoP.C==C)
        flag=1;
    else
        flag=0;
    while (!vacia(Paux)){
        SacaP(&Paux,&datoP);
        PoneP(&P,&datoP);
    }
    return flag;
   }
   else return 0;
}


void recorredigrafo(Tvec v,int N,Arbol a,int *cont){            //tarde 12 min en hacerlo y 3 min en revisar
    Tlista aux;
    int flag,minimo;
    for(int i=0;i<N;i++){
        flag=0;
        minimo=9999;
        aux=v[i];
        while (aux!=NULL && !flag){
            if (aux->vert==i)      //tiene bucle
                flag=1;
            if (aux->dato<minimo)
                    minimo=aux->dato;

          aux=aux->sig;
        }
        if (!flag && !enABB(a,minimo))
            (*cont)++;

    }

}

int enABB(Arbol a,int minimo){

    if (a!=NULL){
        if ((float)minimo==a->dato)
            return 1;
        else
            if ((float)minimo>a->dato)
                return enABB(a->der,minimo);
            else
                return enABB(a->izq,minimo);
    }
    else return 0;

}



int gradoK(arbol a,pos p,int K,int cont){           //tarde 6 min

    if (!nulo(p)){
        if (cont<=1){
            if (grado(a,hijomasizq(p,a)==K)
                cont++;
            return gradoK(a,hijomasizq(p,a),K,cont)&&gradoK(a,hermanoder(p,a),K,cont);
        }
        else
            return 0;

    }
        else return 1;
}


int grado(arbol a,pos c){
    int gr=0;
    while (!nulo(c)){
        gr++;
        c=hermanoder(c,a);
    }
    return grado;

}


/* teorico
V O F
a)Un arbol AVL es un arbol binario en el cual se verifica que la longitud de todas sus ramas es la
misma o difieren en, a la sumo, 1.

















