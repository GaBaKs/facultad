#include <stdio.h>

typedef int Tvec[30];

void lecturav(Tvec vec,int *n);
void impares(Tvec vec,int n);
void mostrarvec2(Tvec vec2,int n2);
void genvec2(Tvec vec,Tvec vec2,int n,int *n2);
void buscarvalorx(Tvec vec,int n);
int main(){
 Tvec vec;
 Tvec vec2;
 int n=0;
 int n2=0;

 lecturav(vec,&n);
 for (int i=0;i<n;i++){
    printf("%d \t",vec[i]);
 }
impares(vec,n);
genvec2(vec,vec2,n,&n2);
buscarvalorx(vec,n);
 return 0;
 }


void lecturav(Tvec vec,int *n){
    int num;

    printf("lectura del vector: \n");
    printf("ingrese un numero (0 para terminar) \n");
    scanf("%d",&num);
    *n=0;
    while (num>0) {
        vec[*n]=num;
        ((*n)++);
        printf("ingrese un numero (0 para terminar) \n");
        scanf("%d",&num);
      }
}

void impares(Tvec vec,int n){

 for (int i=1;i<n;i+=2){
    printf("posicion: %d  valor: %d\n",i,vec[i]);
 }
}
void mostrarvec2(Tvec vec2,int n2){
    for(int i=0;i<n2;i++){
        printf("vec 2: Posicion: %d valor: %d\n",i,vec2[i]);
    }
}
void genvec2(Tvec vec,Tvec vec2,int n,int *n2){
  int k;
  *n2=0;
  printf("ingrese un elemento K para dividir \n");
  scanf("%d",&k);
  for(int i=0;i<n;i++){
    if (vec[i] % k == 0){
        vec2[*n2]=vec[i];
        ((*n2)++);
    }
  }
  mostrarvec2(vec2,*n2);
}
void buscarvalorx(Tvec vec,int n){
    int x;
    int j=0;
    printf("ingrese un valor a buscar en el vector \n");
    scanf("%d",&x);
    while ((j<n) && (vec[j]!=x))
        j++;

    if (j==n)
        printf("El valor ingresado no existe en el vector");
     else
        printf("El valor %d se encuentra en la posicion %d",x,j);

}

