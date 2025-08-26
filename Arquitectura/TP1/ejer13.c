#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){

    char dias=22;  //00001010
    weekday_set(&dias,6);
    diasemana(dias);

    return 0;

}


void diasemana(char dias){

    char masc;
    for(int i=0;i<7;i++){
        masc=1 << i;
        if (dias&masc){
            switch(i){

            case 1:
                printf("Lunes\n");
                break;
            case 2:
                printf("Martes\n");
                break;
            case 3:
                printf("Miercoles\n");
                break;
            case 4:
                printf("Jueves\n");
                break;
            case 5:
                printf("Viernes\n");
                break;
            case 6:
                printf("Sabado\n");
                break;
            case 0:
                printf("Domingo\n");
                break;
            default:
                printf("wtf tiro error");
            }
        }



    }
}



void weekday_set (char * dias,int dia){

    switch(dia){
            case 1:
                *dias=*dias|0b00000010;
                break;
            case 2:
                *dias=*dias|0b00000100;
                break;
            case 3:
                *dias=*dias|0b00001000;
                break;
            case 4:
                *dias=*dias|0b00010000;
                break;
            case 5:
                *dias=*dias|00100000;
                break;
            case 6:
                *dias=*dias|0b01000000;
                break;
            case 0:
                *dias=*dias|0b00000001;
                break;
            default:
                printf("wtf tiro error");
        }


}
