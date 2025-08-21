#include <stdio.h>
#include <string.h>
#define MAX 30

    typedef char Tstring[MAX];

int main(){
  Tstring cad1,cad2,cad3;
  int i;
  gets(cad1);
  gets(cad2);
  if (strcmp(cad1,cad2)!=0){
    strcpy(cad3,cad1);
    }
    i=strlen(cad3);
  printf("tamanio i: %s",cad3);
 return 0;
}
