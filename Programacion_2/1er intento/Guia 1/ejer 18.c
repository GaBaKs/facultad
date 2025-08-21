#include <stdio.h>
#define MAX 30

void crearvec();
void duplica();
int main(){
    int vector[MAX],n;
    crearvec(vector,&n);
    duplica(vector,n);
 return 0;
}


void crearvec(int vector[],int *n){
 int num;
  *n=0;
  printf("ingrese un numero(0 para terminar \n)");
  scanf("%d",&num);
  while (num!=0){
    vector[*n]=num;
     (*n)++;
    printf("ingrese un numero(0 para terminar)\n");
    scanf("%d",&num);
  }
}

void duplica(int vector[],int n){
 int i;
 for(i=;i<n;i+=2){
    vector[i]*=2;
    printf("%d \t",vector[i]);
 }
}
