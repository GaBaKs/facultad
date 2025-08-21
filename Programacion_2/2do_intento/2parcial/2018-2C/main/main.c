#include <stdio.h>
#include <stdlib.h>

int main()
{


}
/*

int contclaves(arbol a){                    //tarde 9:05 en resolver y 2:10 revisando
arbol aux;
int acumact=0;
 if (a!=NULL){
    aux=a->izq;
    while (aux!=NULL){
        acumact+=aux->dato;
        aux=aux->der;
    }
    if (a->dato>acumact && a->izq!=NULL)
        return contclaves(a->izq)+contclaves(a->der);
    else
        if (a->izq!=NULL)
            return 1+contclaves(a->izq)+contclaves(a->der);

 }
 else return 0;

}



// minimain


main(){
 pos p;
 arbol a;
 iniciarbol(&a,&p);


if ( !vacio(a) && !verifica(a,p,k,1))
    printf("existe un nodo que cumple con estas condiciones");
else printf("el arbol esta vacio o no cumple con estas condiciones");
}

int verifica(arbol a,pos p,int k,int niv){                           // tarde 10:10 en hacerlo y no lo revise (total 21:29)
 pos c;

    if (!nulo(p)){
        c=hijomasizq(p,a);
        if (!nulo(c) && niv==k){
            return 0;
        }
        else
            return verifica(a,hijomasizq(p,a),k,niv+1) && verifica(a,hermanoder(p,a),k,niv);

        }
        else return 1;
    }

//minimain

typedef struct{
    int llegada,suma,bucle;
}Tvec
typedef struct nodo{
    int pond;
    int vertice;
    struct nodo * sig;}nodo;
}
typedef struct nodo * Tlista;
typedef struct{
 int vertice;
 Tlista lista;
}TvecL;


void mayorcost(TvecL V,int n){      // tarde 19:44 en hacerlo y 7:46 en corregirlo(tenia un error) total de tiempo 49:00
    Tvec Vaux[n];
    Tlista auxL;
    float costprom=0;
    float costact;
    int posmax=-1;
    for (int i=0;i<n;i++){
        auxL=V.lista;
        while (auxL!=NULL){
           Vaux[auxL->vertice].suma+=auxL->pond;
           if (i==auxL->vertice)        // tiene bucle
                Vaux[i].bucle=1;
           Vaux[i].llegada++;
          auxL=auxL->sig;
        }
    }
    // recorro vector
    for (i=0;i<N;i++){
        if (Vaux[i].bucle){
            costact=(float) Vaux[i].suma/Vaux[i].llegada;
            if (costact>costprom){
                costprom=costact;
                posmax=i;
            }
        }
    }
    if (posmax>=0)
        prinf("el vertice que mayor costo promedio tiene es %5.2f",costprom);
    else
        printf("ningun nodo tiene bucle");

}
*/
