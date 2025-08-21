#include <stdio.h>
#include <stdlib.h>




typedef struct nodito{
    int numemp;
    char fecha[9];
    char rect;
    struct nodito * sig;}nodito;
typedef nodito * sublista;

typedef struct nodo{
    int norma;
    char nombreN[9];
    int cantemp;
    sublista sub;
    struct nodo * sig;}nodo;
typedef struct nodo * Tlista;

int main(){
    Tlista L;
    L=NULL;
    return 0;
}
void generaL(Tlista *L){
    FILE *arch;
    Tlista nuevo;
    sublista nuevito,antS,actS;
    int norma;
    char nombreN[9];
    int cantemp;
    Tlista act;
    if ((arch=fopen("CARGACTUAL.TXT","r"))==NULL)
        printf("el archivo no pudo abrirse");
    else{
        fscanf("%d %s %d",norma,nombreN,cantemp);
        while (!feof(arch)){
            nuevo=(Tlista) malloc (sizeof(nodo));
            nuevo->norma=norma;
            nuevo->nombreN=nombreN;
            nuevo->cantemp=cantemp;
            nuevo->sig=NULL;
            nuevo->sub=NULL;
            if (*L==NULL)
             *L=nuevo;
            else{
                act=*L;
                while (act->sig!=NULL)
                    act=act->sig;
                act->sig=nuevo;
            }
            for (int i=0;i<cantemp;i++){
                nuevito=(sublista) malloc (sizeof(nodito));
                fscanf("%d %s %c",nuevito->numemp,nuevito->fecha,nuevito->rect);
                nuevito->sig=NULL;
                if (nuevo->sub==NULL)
                    nuevo->sub=nuevito;
                else{
                     if nuevo->sub->numemp>nuevito->numemp{
                        nuevito->sig=nuevo->sub;
                        nuevo->sub=nuevito;
                     }
                     else{
                        antS=NULL;
                        actS=nuevo->sub;
                        while (actS!=NULL && actS->numemp<nuevito->numemp{
                            antS=actS;
                            actS=actS->sig;
                        }
                        antS->sig=nuevito;
                        nuevito->sig=actS;
                    }
                }

            }
          fscanf("%d %s %d",norma,nombreN,cantemp);
        }

    close(arch);
    }
}


void certifempresa(Tlista L){
    Tlista act;
    sublista actS;
    int cantnormas,maxnormas=-1;
    int numemp;
    int N;

    printf("cuantas empresas desea ingresar?\n");
    scanf("%d",N);
    for (int i=0;i<N;i++){
        printf("ingrese el nombre de una empresa\n");
        scanf("%d",numemp);
        cantnormas=0;
        act=L;
        while (act!=NULL){
          actS=act->sub;
          while (actS!=NULL && actS->numemp<=numemp){
            if (actS->numemp==numemp)
                cantnormas++;
            actS=actS->sig;
          }
         act=act->sig;
        }
        if (cantnomas>maxnormas)
            maxnormas=cantnormas;
        printf("la empresa %d certifico %d normas \n",numemp,cantnormas);
    }
    printf("la empresa que mas normas certifico fue %d \n",numemp);
}
void iniciarmatriz(char matriz[20][50]){

    for (int i=0;i<20;i++)
        for(int j=0;j<50;j++)
            matriz[i][j]='N';

}

void generamatriz(Tlista L){
    char matriz[20][50];
    Tlista act;
    sublista actS;
    iniciarmatriz(matriz);
    act=L;
    while (act!=NULL){
        act->sub=actS;
            while(actS!=NULL){
                if (actS->rect=='S')
                    matriz[act->norma][actS->numemp]='S';
                actS=actS->sig;
            }
        act=act->sig;
    }
}



int recorromatriz(char matriz[20][50],Tcola *cola,int X,int i,j){
 if j==0
    if matriz[i][0]=='S'
     return 1;
    else return 0;
 else{
    if i==0
        return

 }


}
