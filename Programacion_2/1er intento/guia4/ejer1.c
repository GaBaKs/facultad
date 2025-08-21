#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "pilasest.h"




void ingresadatos(TPila *P1,int n);
void muestrainv(TPila *P1,TPila *P2,int n);
void muestrabn(TPila *P2,int n);



int main(){
    TPila P1,P2;
    TElementoP x;
    int n;
    IniciaP(&P1);
    IniciaP(&P2);
    printf("ingrese un valor de n\n");
    scanf("%d",&n);
    ingresadatos(&P1,n);
    muestrainv(&P1,&P2,n);
    muestrabn(&P2,n);

  return 0;
}
void ingresadatos(TPila *P1,int n){
    TElementoP x;
    for (int i=0;i<n;i++){
        printf("Ingrese un numero de dni\n");
        scanf("%d",&x);
        poneP(P1,x);
    }
}

void muestrainv(TPila *P1,TPila *P2,int n){
    TElementoP x;
    printf("Muestra de los dni invertidos:\n");
    for (int i=0;i<n;i++){
        sacaP(P1,x);
        poneP(P2,x);
        printf("%d\t",consultaP(*P2));
    }
}

void muestrabn(TPila *P2,int n){
    TElementoP x;
    printf("muestra de los DNI bien:\n");
    for (int i=0;i<n;i++){
        sacaP(P2,x);
        printf("%d\t",x);
    }

}
