#include <stdio.h>
#include <stdlib.h>

typedef struct nodoC{

    int dato;
    struct nodoC * sig;}nodoC;

typedef struct nodoC * TlistaC;


int main(){

    TlistaC LC;
    Tpila P;
    IniciaP(&P);

    return 0;

}


void eliminalista (TlistaC *LC, Tpila *P){

    TlistaC ant,act,elim;
    TelementoP datoP;
    int pos=2;
   if (*LC!=NULL)
        if ((*LC)->sig==*LC)
            printf("la lista tiene un solo elemento, por lo tanto no hay que eliminar nada");
        else{
            ant=*LC->sig;
            act=ant->sig;
            do{
                if (act->dato<ant->dato){           // no es ascendente
                    elim=act;
                    if (act==*LC){                  //elimino la cabeza
                        ant->sig=(*LC)->sig;
                        datoP.numero=act->numero;
                        *LC=ant;
                        act=*LC;
                    }
                    else{               //no es la cabeza
                        ant->sig=act->sig;
                        datoP.numero=act->numero;
                        act=act->sig;
                    }

                    datoP.pos=pos;
                    poneP(&P,datoP);
                    pos++;
                    free(elim);

                }
               else{
                   ant=act;
                   act=act->sig;
                   pos++;
               }
            }
            while (act!=*LC);
        }
    else
        printf("la LC esta vacia");

}



// ejercicio 2

//a (.h de pilas)


void IniciaP(Tpila *P);
TelementoP ConsultaP(Tpila P);
int VaciaP(Tpila P);
void PoneP(Tpila *P,TelementoP x);
void SacaP(Tpila *P,TelementoP *x);


// b (.c de pilas)

void PoneP (TpilaP *P,TelementoP x){

    if ((*P).tope!=MAX-1){
        (*P).datos[++((*P).tope)]=X;
    }
}
TelementoP ConsultaP(Tpila P){
   if (P.tope!=-1)
    return P.dato[P.tope];

}
