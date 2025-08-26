#include <stdio.h>
#include <stdlib.h>


int main(){

    int n=0x02A3;

    printf("n es %d \n",n);
    printf("El byte de la izquierda: %d\n",incisoa(n));
    printf("El byte de la derecha: %d\n",incisob(n));
    printf("Devolver 1 si el numero es impar, y 0 si es par: %d\n",incisoc(n));
    printf("Devolver -1 si el numero es negativo, y 0 si es positivo: %d\n",incisod(n));
    printf("Devolver el número que representan los primeros 12 bits: %d\n",incisoe(n));
    printf("Devolver el número que representan los ultimos 4 bits: %d\n",incisof(n));


    return 0;
}


int incisoa(int n){


    int masc=0xFF00;
    return ((n&masc) >> 8);

}

int incisob(int n){
    int masc=0x00FF;

    return n&masc;

}

int incisoc(int n){

    int masc=0x0001;

    return (masc&n);


}

int incisod(int n){

    int masc=0x8000;
    return (masc&n);


}

int incisoe(int n){

    return  n >> 4;

}

int incisof(int n){

    int masc=0x000F;
    return n&masc;

}







