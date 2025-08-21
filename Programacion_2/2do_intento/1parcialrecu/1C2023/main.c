#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ST7 8
#define ST3 4


typedef struct nodoC{

    char pat[ST7];
    char vip;
    char radiocubre[ST3];
    int cantmax;
    char libre;
    struct nodoC * sig;}nodoC;

typedef struct nodoC * TlistaC;
typedef struct{
    int cantpas;
    char vip;
    char radio;
}Tviajes;

typedef struct nodo{

    char pat[ST7];
    Tcola C;        // cantpas vip y radio
    struct nodo * sig;}nodo;
typedef struct nodo * Tlista;

typedef struct{
    int cantv;
    int totpas;}vec;

typedef vec Tvec[3];


void procesoarchivo(TlistaC LC,Tlista *L){
    FILE * arch;
    Tlista aux,ant;
    TlistaC auxC;
    Tviajes datoarch;
    int flag;
    if (arch=fopen("VIAJES.dat","rb")==NULL)
        printf("ocurrio un error en la apertura del archivo");
    else{
          fread(&datoarch,sizeof(Tviajes),1,arch);
           while (!feof(arch)){
                auxC=LC->sig;
                flag=0;
                while (auxC!=LC && !flag){          //busco un auto que cumple
                    if (auxC->libre=='S' && auxC->cantmax>=datoarch.cantpas && (auxC->vip=='S' || auxC->vip=='N' && datoarch.vip=='N') && cumpleradio(auxC->radiocubre,datoarch.radio)){ //cumple
                        auxC->libre='N';
                        metocola(L,datoarch,auxC->pat);
                        flag=1;
                    }
                    else
                        auxC=auxC->sig;
                }
                if (!flag)
                    if (auxC->libre=='S' && auxC->cantmax>=datoarch.cantpas && (auxC->vip=='S' || auxC->vip=='N' && datoarch.vip=='N') && cumpleradio(auxC->radiocubre,datoarch.radio)){ //cumple
                        auxC->libre='N';
                        metocola(L,datoarch);
                        printf("la patente del viaje asignado es %s",auxC->pat);
                    }
                    else
                        printf("no hay ningun auto disponible para el viaje solicitado");
                else
                        printf("la patente del viaje asignado es %s",auxC->pat);
            fread(&datoarch,sizeof(Tviajes),1,arch);
           }


    fclose(arch);
    }
}

void metocola(Tlista *L,Tviajes datoarch,char pat[ST7]){

    TelementoC datoC;
    Tlista aux,ant,nuevo;
    Tcola Cn;


    datoC.cantpas=datoarch.cantpas;
    datoC.vip=datoarch.vip;
    datoC.radio=datoarch.radio;

    if (strcmp((*L)->pat,pat)==0)       //meto en el primer nodo
        poneC(&((*L)->C),datoC);
    else{
        if (strcmp((*L)->pat,pat)>0){     //creo lista en primer nodo
            nuevo=(Tlista) malloc (sizeof(nodo));
            iniciaC(&(nuevo->C));
            poneC(&(nuevo->C),datoC);
            nuevo->sig=*L;
            *L=nuevo;
        }
        else{               //recorro
            aux=*L;
            ant=NULL;
            while (aux!=NULL && strcmp(aux->pat,pat)<0){
                ant=aux;
                aux=aux->sig;
            }
            if (aux==NULL){         //ingreso a lo ultimo
                nuevo=(Tlista) malloc (sizeof(nodo));
                iniciaC(&(nuevo->C));
                poneC(&(nuevo->C),datoC);
                ant->sig=nuevo;
                nuevo->sig=NULL;
            }
            else{                       //al medio
                if (strcmp(aux->pat,pat)==0)
                    poneC(&(aux->C),datoC);
                else{
                    nuevo=(Tlista) malloc (sizeof(nodo));
                    iniciaC(&(nuevo->C));
                    poneC(&(nuevo->C),datoC);
                    ant->sig=nuevo;
                    nuevo->sig=aux;
                }
            }
        }
    }


}

int cumpleradio (char radiocubre[ST3],Tviajes datoarch){

    if (strchr(radiocubre,datoarch.radio)==NULL)
        return 0;
    else return 1;
}


void sacoviajes(Tlista L){

    TelementoC datoC;
    Tcola colaux;
    Tlista aux;
    char pat[ST7]="ninguno";
    int contelim,contelimax=0;
    aux=L;
    iniciaC(&colaux);
    while (aux!=NULL){
         contelim=0;
        while (!vacia(aux->C)){                 //saco todo de la cola
            sacaC(&(aux->C),&datoC);
            if (datoC.cantpas==0)
                contelim++;
            else
                poneC(&colaux,datoC);
        }
       if (contelim>=contelimax){
            contelimax=contelim;
            strcpy(pat,aux->pat);
       }
        while (!vacia(colaux)){
        sacaC(&colaux,&datoC);
        poneC(&(aux->C),datoC);
        }
       aux=aux->sig;
    }
  printf("el coche con mas eliminaciones fue el de patente %s con %d eliminaciones",pat,contelimax);

}


void eliminoP(Tlista *L,TlistaC *LC,Tvec vec){

    Tlista act,ant,elim;
    TlistaC actC,antC,elimC;
    char p[ST7];

    printf("ingrese una patente a eliminar");
    scanf("%s",p);

    //elimino de LC

    actC=(*LC)->sig;
    antC=*LC;
    while (strcmp(actC->pat,p)!=0){
        antC=actC;
        actC=actC->sig;
    }
    if (actC==*LC){         // borro la cabeza
        elimC=*LC;
        if (*LC==*LC->sig)           // es unico
            *LC=NULL;
        else{
         antC->sig=(*LC)->sig;
         *LC=antC;
        }
    }
    else{
        elimC=actC;
        antC->sig=actC->sig;
    }
    free(elimC);

    //borro en L
    if (strcmp((*L)->pat,p)==0){        //borro la cabeza
        elim=*L;
        generovector((*L)->C,vec);
        *L=*L->sig;
    }
    else{
        act=*L;
        ant=NULL;
        while (strcmp(act->pat,p)<0){
            ant=act;
            act=act->sig;
        }
        generovector(act->C,vec);
        elim=act;
        ant->sig=act->sig;

    }
     free(elim);
}

void iniciovec(Tvec vec){
        vec[0].cantv=0;
        vec[0].totpas=0;
        vec[1].cantv=0;
        vec[1].totpas=0;
        vec[2].cantv=0;
        vec[2].totpas=0;

}


void generovector(Tcola C,Tvec vec){

    TelementoC datoC;
    iniciovec(vec);
    while (!vacia(C)){
        sacaC(&C,&datoC);
        if (datoC.radio=='U'){
            vec[0].cantv++;
            vec[0].totpas+=datoC.cantpas;
        }
        else
        if (datoC.radio=='R'){
            vec[1].cantv++;
            vec[1].totpas+=datoC.cantpas;
        }
        else
        if (datoC.radio=='I'){
            vec[2].cantv++;
            vec[2].totpas+=datoC.cantpas;
        }

    }

}
























int main()
{
    printf("Hello world!\n");
    return 0;
}
