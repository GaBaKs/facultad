#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct nodo{
    char dom[6];
    char fechaT[7];
    char hora[4];
    struct nodo * sig;}nodo;
typedef struct nodo * Tlista;

typedef struct nodito{

    char dom[6];
    int cantobs;
    struct nodito * sig;}nodito;

 typedef struct nodito * Tsublista;

 typedef struct nodoD{
    char puesto[2];
    Tsublista sub;
    struct nodoD * ant, * sig;}nodoD;
 typedef struct nodoD * PnodoD;


typedef struct{
    PnodoD pri,ult;}TlistaD;


int main(){


}


void Eliminaincorrectos(Tlista *LT){
    int totalT=0,depurados=0,elimina;
    Tlista aux,elim,ant;
    aux=*LT;
    ant=NULL;
    while (aux!=NULL){
        elimina=0;
        totalT++;
        if (aux->fecha[4]!='1' || aux->fecha[5]=='0'){
            if (aux->dom[5]>='0' && aux->dom[5]<='9'){                 //es patente vieja
                if (aux->fechaT[5]!=aux->dom[5])                      //si el num de pat no coincide
                    elimina=1;
            }
            else
                if (aux->dom[4]!=aux->fechaT[5])                       //patente nueva
                    elimina=1;
        }
        if (elimina){
            (if aux==*LT)
                *LT=*LT->sig;
            else
                ant->sig=aux->sig;

            elim=aux;
            aux=aux->sig;
            free(elim);
            depurados++;
        }
        else{
            ant=aux;
            aux=aux->sig;
        }

    }
    printf("el porcentaje de turnos depurados es %5.2f %%",((float)depurados/totalT)*100);
}

int cantpuestos(TlistaD PA){
    PnodoD aux;
    int n=0;
    aux=PA.pri;
    while (aux!=NULL){
        aux=aux->sig;
        n++;
    }

return n;

}

void metoauto(TlistaD PA,TelementoC datoC,int Pasig){

    PnodoD auxD;
    Tsublista actS,nuevoS;
    auxD=PA.pri;
    for(int i=1;i<Pasig;i++){
        auxD=auxD->sig;
    }
    actS=auxD->sub;
    nuevoS=(Tsublista) malloc sizeof(nodito);
    while (actS->sig!=NULL)
        actS=actS->sig;
    strcpy(nuevoS->dom,datoC);
    nuevoS->sig=NULL;
    nuevoS->cantobs=0;
    actS->sig;nuevoS;


}


void atencionautos(Tlista LT,TlistaD PA,Tcola *C){

TelementoC datoC;
Tcola colaux;
Tlista aux;
IniciaC(&colaux);
int N=cantpuestos(PA),Pasig;
SacaC(C,&datoC);
    while (!vacia(&C)){
        aux=LT;
                while (aux!=NULL && strcmp(aux->dom,datoC)>0){                       //busco si ese dom tiene turno
                    aux=aux->sig;
                }
                  if (aux!=NULL && strcmp(aux->dom,datoC)==0){                      // tiene turno
                    if (aux->fechaT[4]=='0' && aux->fechaT[5]=='4'){     //analizo si el dom es igual y si la fecha es en abril
                        Pasig=rand() % N + 1;
                        metoauto(PA,datoC,Pasig);
                    }
                    else
                       PoneC(&colaux,datoC);                      
                  }
                  else
                      printf("%s no tiene turno\t",datoC);
                SacaC(C,&datoC);

   }
    while(!vacia(colaux)){
        SacaC(&colaux,datoC);
        PoneC(C,datoC);
    }
}






PnodoD buscapuesto(TlistaD PA,char puesto[2]){
PnodoD auxD;
    if (strcmp((PA.pri)->puesto,puesto)==0)
        return PA.pri;
    else if (strcmp((PA.ult)->puesto,puesto)==0)
        return PA.ult;
    else{
         auxD=PA.pri;
        while (strcmp(puesto,auxD->puesto)!=0)
            auxD=auxD->sig;
        return auxD;
    }
}


void obsrec(TlistaD * PA){

    char puesto[2];
    char dom[6];
    int cantobs;
    char estado;
    PnodoD auxD,elimD;
    Tsublista elimS,antS,auxS;

    FILE * arch;
    if ((arch=fopen("TESTEOS.TXT","r"))==NULL)
        printf("error en la apertura del archivo");
    else
    {
     fscanf(arch,"%s %s %d %c",puesto,dom,&cantobs,&estado);
     while (!feof(arch)){
       auxD=buscapuesto(&PA,puesto);
       auxS=auxD->sub;
       antS=NULL;
       while (strcmp(auxS->dom,dom)!=0){
        antS=auxS;
        auxS=auxS->sig;
       }
       if (estado=='O')
        auxS->cantobs=cantobs;
       else                                             //elimino
       {
        if (auxD->sub==auxS)            //elimino la cabeza de la sublista
            auxD->sub=auxS->sig;
        else
            antS->sig=auxS->sig;
        free(auxS);
        if (auxD->sub==NULL){      //si no hay mas autos en el nodo lo elimino
            if(auxD==(*PA).pri)    //elimino la cabeza
                (*PA).pri=(*PA).pri->sig;
            else
                if (auxD==(*PA).ult)            //eliminar el ultimo
                    (*PA).ult=((*PA).ult)->ant;
                else{                               //elimino algo del medio
                    auxD->ant->sig=auxD->sig;
                    auxD->sig->ant=auxD->ant;
                }


             free(auxD);
        }
       }
       fscanf(arch,"%s %s %d %c",puesto,dom,cantobs,estado);
     }
    }

close(arch);
}




