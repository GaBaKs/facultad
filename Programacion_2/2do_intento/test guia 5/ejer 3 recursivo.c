#include <stdio.h>
#include <stdlib.h>


int main(){
    TelementoP dato;
    Tpila P;


}

void pilarecursiva(Tpila P,TelementoP dato,int n){

    if (!VaciaP(P) && n>0){
        sacaP(&P,&dato);
        pilarecursiva(P,dato,n-1);
        poneP(&P,dato);
        consultaP(P);
    }

}
