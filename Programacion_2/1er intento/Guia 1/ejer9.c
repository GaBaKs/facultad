#include <stdio.h>
int main() {
    int x=9,y;
    switch (x){
        case 4: y=7;
                break;
        case 5: y=9;
                break;
        case 9: y=14;
                break;
        default: y=22;
    }
    printf("El valor de X es: %d\nEl valor de Y es: %d",x,y);
    return 0;
}
