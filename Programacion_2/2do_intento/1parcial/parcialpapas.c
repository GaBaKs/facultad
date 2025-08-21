#include <stdio.h>
#include <stdlib.h>
#include "colas.h"
#include "pilas.h"

typedef struct nodito{
    float pesokg;
    int cantp[3];
    struct nodito * sig}nodito;

typedef struct nodito * Tsublista;

typedef struct nodoD{
    char dest;
    Tsublista sub;
    struct nodoD * ant,*sig}nodoD;
typedef nodoD * PnodoD;

typedef struct TlistaD{
    PnodoD pri,
    PnodoD ult}TlistaD;

void embolsado(Tcola *Cpapa,TlistaD LD,Tpila *Pdesc);
void atiendepedido(TlistaD LD,int cantb,char dest);
void reingresopapa(Tcola *C,Tpila *Pdesc,int *quedanp);



int main(){
    Tcola Cpapa;
    TlistaD LD;
    LD.pri=NULL;
    LD.ult=NULL;
    Tpila Pdesc;
    IniciaP(&Pdesc);
    IniciaC(&Cpapa);
    cargaLD(&LD);
    cargacola(&Cpapa);
    int cantb,quedanp;
    char dest;
    embolsado(&Cpapa,LD,&Pdesc);
    printf("ingrese un destino\n");
    scanf("%c",&dest);
    printf("ingrese una cantidad de bolsas\n");
    scanf("%d",&cantb);
    atiendepedido(LD,cantb,dest);
    reingresopapa(&Cpapa,&Pdesc,&quedanp);
    if (quedanp)
        printf("quedan papas de calidad 4 en la pila de descarte");
    else
        printf("no quedan papas de calidad 4 en la pila de descarte");


 return 0;
}



void embolsado(Tcola *Cpapa,TlistaD LD,Tpila *Pdesc){
    Tsublista auxS,BolsaS;
    PnodoD auxD;
    TelementoC auxC;
    int totpapas;
    float porc1,pesoprom;


    IniciaP(Pdesc);
    BolsaS=(Tsublista) malloc (sizeof(nodito));
    BolsaS->cantp[0]=0;
    BolsaS->cantp[1]=0;
    BolsaS->cantp[2]=0;
    BolsaS->pesokg=0;
    BolsaS->sig=NULL;
    int i;
    while (!vacia(Cpapa)){
        SacaC(Cpapa,&auxC);
        if ((auxC.peso<30) || (auxC.cal==4) || (auxC.cal==5))                          // la papa es valida?
            PoneP(Pdesc,auxC);
        else
        {
            if (BolsaS->pesokg<= 50)                             // si hay espacio en la bolsa
            {
                BolsaS->pesokg+=(float)auxC.peso/1000;
                BolsaS->cantp[(auxC.cal) - 1]++;
            }
            if (BolsaS->pesokg>50)
            {                                                                        // no hay espacio en la bolsa
                totpapas=BolsaS->cantp[1]+BolsaS->cantp[0]+BolsaS->cantp[2];
                porc=(float)BolsaS->cantp[0]/totpapas;
                pesoprom=(BolsaS->pesokg*1000)/totpapas;
                if (porc>=50 && pesoprom>=100)                                // analizo si guardar a EXTERIOR
                    i=3;
                else{                                                        //analizo si guardar en Nacional
                    porc=(float)(BolsaS->cantp[1]+BolsaS->cantp[0])/totpapas;
                    if (porc>=0.4 && pesoprom>=50)
                        i=2;
                    else
                        i=1;
                }
                                                                                    //donde guardo en la LD
                if (i==3)
                    auxD=LD.ult;
                else
                    if (i==1)
                        auxD=LD.pri;
                    else
                        auxD=LD.pri->sig;
                auxS=auxD->sub;                                             // entro a la sublista
                if (auxS==NULL)                                             //existe?
                    auxD->sub=BolsaS;
                else
                    while (auxS->sig!=NULL)                                     //si no existe recorro
                        auxS=auxS->sig;
                    auxS->sig=BolsaS;


            BolsaS=(Tsublista) malloc (sizeof(nodito));                         //creo otra bolsa mas
            BolsaS->cantp[0]=0;
            BolsaS->cantp[1]=0;
            BolsaS->cantp[2]=0;
            BolsaS->pesokg=0;
            BolsaS->sig=NULL;


            }
        }



    }
    if (BolsaS->pesokg!=0)
        printf("se perdieron %f5.2 kg de papas",BolsaS->pesokg);
    free(BolsaS);



}


void atiendepedido(TlistaD *LD,int cantb,char dest){
    char archivo[3];
    PnodoD auxD;
    Tsublista auxS,elimS,antS;
    FILE * arch;
    int cont=0,cantpapas;
    float pesototal=0;
    sprintf(archivo,"%c%d",dest,cantb);
    if ((arch=fopen(archivo,"w"))==NULL)
        printf("ocurrio un error en la apertura del archivo");
    else{
        if (strcmp(dest,LD->pri->dest)==0)
            auxD=LD->pri;
        else
            if ((strcmp(dest,LD.ult->dest)==0))
                auxD=LD->ult;
        else
            auxD=LD->pri->sig;
            auxS=auxD->sub;
            while (auxS!=NULL && cont<cant){
                cantpapas=auxS->cantp[0]+auxS->cantp[1]+auxS->cantp[2];
                fprintf(arch,"%5.2f %d\n",auxS->pesokg,cantpapas);
                auxD->sub=auxD->sub->sig;
                elimS=auxS;
                auxS=auxS->sig;
                free(elimS);
                cont++;
                pesototal+=cantpapas;

            }
            fprintf(arch,"%5.2f",pesototal);
            if (auxD->sub==NULL){                   //elimino nodo de LD
                if (auxD==LD->pri)
                    LD->pri=LD->pri->sig;
                else
                    if (auxD==LD->ult)
                        LD->ult=LD->ult->ant;
                else{
                    auxD->ant->sig=auxD->sig
                    auxD->sig->ant=auxD->ant;
                }
                free(auxD);

            }

    }
    Close(arch);
}


void reingresopapa(Tcola *Cpapa,Tpila *Pdesc,int *quedanp){
    TelementoP datoP;

    if (!vacia(P)){
        SacaP(Pdesc,&datoP);
        reingresopapa(&C,&Pdesc,&quedanp);
        if (datoP.cal==4 && datoP.peso>30)
            PoneC(C,datoP);
        else{
           if (datoP.cal==4)
             quedanp=1;
            PoneP(Pdesc,datoP);
        }


    }



}


