#include <stdio.h>
#include <stdlib.h>


float calculoprom(int vec[],int N,int cont,int i);

int main(){
    int vec[4];
    int N=4;
    int cont;
    int i;
    vec[0]=3;
    vec[1]=2;
    vec[2]=2;
    vec[3]=2;
    printf("el promedio de los elementos es de %5.2f",calculoprom(vec,N,0,N-1));
return 0;}


float calculoprom(int vec[],int N,int cont,int i){
    if (i<0)
        return (float)cont /N;
    else
        return calculoprom(vec,N,cont+vec[i],i-1);

}
