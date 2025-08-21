#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#DEFINE ST5 4
#define ST30 29
#define ST7 6

typedef struct nodito{
    ST7 pat;
    int fechaJ;
    ST5 hora;
    int TabonadoH,TabonadoM;
    int TocupacionH,TocupacionM;
    struct nodito * sig;}nodito;
typedef struct nodito * Tsublista;

typedef struct nodoD{
    ST5 cod;
    ST30 nomap;
    char estudiante;
    Tsublista sub;
    struct nodoD * sig, * ant;}nodoD;

typedef struct nodoD * PnodoD;
typedef struct{
    PnodoD pri,ult;
}TlistaD;



int mes_juliano(int fechaJ);
PnodoD nodoagente(TlistaD LD,char cod[4]);
void actualizoLD(TlistaD LD,Tcola * C);
void generoarchbin(TlistaD LD,int K,char AG[4]);
void eliminaX(TlistaD * LD,char X[4]);

int main(){
    TlistaD LD;
    Tcola C;

    int K;
    char AG[4];
    char X[4];
    IniciaC(&C);
    cargalistaLD(&LD);
    cargacola(&C);
    actualizoLD(LD,&C);
    printf("ingrese un valor de k\t");
    scanf("%d",&k);
    printf("ingrese un codigo de agente\t");
    scanf("%s",AG);
    generoarchivobin(LD,K,AG);
    printf("ingrese un agente X\t");
    scanf("%s",X);
    eliminaX(&LD,X);

return 0;
}

int mes_juliano(int fechaJ){
    if fechaJ



}


PnodoD nodoagente(TlistaD LD,char cod[4]){
    PnodoD auxD;


    if (LD.pri!=NULL && strcmp((LD.pri)->cod,cod)==0)
        return LD.pri;
    else
        if (LD.ult!=NULL && strcmp((LD.ult)->cod,cod)==0)
            return LD.ult;
        else{
            auxD=LD.pri;
            while (auxD!=LD.ult && strcmp(auxD->cod,cod)<0)
                auxD=auxD->sig;
           if (auxD==LD.ult)
                return NULL;
           else
                return auxD;
    }
}


void actualizoLD(TlistaD LD,Tcola * C){

    PnodoD auxD;
    Tsublista auxS,antS,nuevoS;
    Tcola Caux;
    TelementoC Cdato;

    While(!vacia(C)){
        SacoC(C,&Cdato);
        if (mes_juliano(Cdato.fechaJ)==9 && (C.Tabonado<C.Tocupacion)){        //analizo si es en septiembre y si uso mas de lo que pago
                auxD=nodoagente(LD,C.cod);
                if (auxD!=NULL){
                    nuevoS=(Tsublista) malloc sizeof(nodito);
                    strcpy(nuevoS->pat,Cdato.pat);
                    nuevoS->fechaJ=Cdato.fechaJ;
                    strcpy(nuevoS->hora,Cdato.hora);
                    nuevoS->TabonadoM=Cdato.Tabonado % 60;
                    nuevoS->TabonadoH=Cdato.Tabonado /60;
                    nuevoS->TocupacionM=Cdato.Tocupacion % 60;
                    nuevoS->TocupacionH=Cdato.Tocupacion / 60;
                                                                    //analizo donde meter de la sublista
                    if (auxD->sub==NULL || strcmp((auxD->sub)->pat,Cdato.pat)>0{                           //si esta vacia ingreso a la cabeza
                        nuevoS->sig=NULL;
                        auxD->sub=nuevoS;
                    }
                    else{
                        auxS=auxD->sub;
                        antS=NULL;
                        while (auxS!=NULL && strcmp(auxS->pat,Cdato.pat)<0){     //recorro hasta que la patente sea mayor al dato
                            antS=auxS;
                            auxS=auxS->sig;
                        }
                        antS->sig=nuevoS;
                        nuevoS->sig=auxS;
                    }

                }
        }
    else
        PoneC(&Caux,Cdato);

    }
    while (!vacia(Caux)){
        SacaC(&Caux,&Cdato);
        PoneC(C,Cdato);
    }
}




// inciso b

void generoarchbin(TlistaD LD,int K,char AG[4]){

    FILE * arch;
    PnodoD auxD;
    int mes;
    Tsublista auxS;
    TregB regB;
    int contmultas=0;
    if ((arch=fopen("MULTAS.DAT","bw"))==NULL)
        printf("error en la apertura del archivo");
    else{
        auxD=nodoagente(LD,AG);
        auxS=auxD->sub;
        while (auxS!=NULL){
            contmultas++;
            mes=mes_juliano(auxS->fechaJ);
            if ((mes % 2)==0 && (stcmp(auxS->hora,"12:00")<0 || strcmp(auxS->hora,"18:00")>0)){         // analizo si es mes par y paso antes de las 12 y dps de las 18
                 strcpy(regB.pat,auxS->pat);
                 regB.fechaJ=auxS->fechaJ;
                 strcpy(regB.hora,auxS->hora);
                 regB.TabonadoH=auxS->TabonadoH;
                 regB.TabonadoM=auxS->TabonadoM;
                 regB.TocupacionH=auxS->TocupacionH;
                 regB.TocupacionM=auxS->TocupacionM;
                 fwrite(&regB,sizeof(TregB),1,arch);
            }
           auxS=auxS->sig;
        }
        if (auxD->estudiante=="S" && contmultas>K)
            printf("Al agente le corresponde la bonificacion del 15%%");


    }
    close(arch);
}

// inciso c
void eliminaX(TlistaD * LD,char X[4]){
    PnodoD auxD,elimD;
    Tsublista auxS,antS,elimS;
    int borroLD=0;
    auxD=nodoagente(&LD,X);
    if (auxD==NULL)
        printf("el agente X no existe");
    else{
        auxS=auxD->sub;
        while (!borroLD && auxS!=NULL){
            if (strncmp(auxS->pat,"AF",2)==0){          //la patente arranca por AF
                if (auxS==auxD->sub)                  //elimino la cabeza
                    auxD->sub=auxD->sub->sig;
                else
                    antS->sig=auxS->sig;
                elimS=auxS;
                auxS=auxS->sig;
                free(elimS);
                if (auxD->sub==NULL){                     //elimino nodo de la LD
                        if (LD->pri==auxD)                 //elimino la cabeza de la LD
                            LD->pri=LD->pri->sig;
                        else
                            if (LD->ult==auxD)
                                LD->ult=LD->ult->ant;
                        else{
                            auxD->ant->sig=auxD->sig;
                            auxD->sig->ant=auxD->ant;
                        }
                     free(auxD);
                     borroLD=1;
                }
            }
            else{
                antS=auxS;
                auxS=auxS->sig;
            }
        }
    }
}

