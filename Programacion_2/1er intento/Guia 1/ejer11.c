#include <stdio.h>

#define max(x,y) ((x>y)? x : y)
#define carac(x) (((x)>='a' && (x)<='z') || ((x)<='Z' && (x)>='A'))
 /* int main(){
   int a=3,b=4;
   printf("el numero mas parecido a boquita pasion es: %d",max(a,b));
    return 0;
 }
*/

   int main(){
     char car='6';
     if (carac(car))
        printf("el caracter ingresado es alfabetico");
     else
        printf("el caracter ingresado no es alfabetico");
    return 0;
   }
