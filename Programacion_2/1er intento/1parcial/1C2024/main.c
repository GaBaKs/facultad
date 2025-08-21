#include <stdio.h>
#include <stdlib.h>
#include <colas.h>
#include <string.h>

typedef struct nodo{              // lista simple LT
    char dominio[8];
    char fecha[9];
    char hora[6];
    struct nodo * sig;}nodo;
typedef nodo * TlistaS;

typedef struct noditoD{
    char dominio[8];
    int obs;
    struct noditoD * sig;}noditoD;
typedef noditoD * Sublista;


typedef struct nodoD{
    char puesto[4];
    Sublista sub;
    struct nodoD *sig,*ant;}nodoD;
typedef struct nodoD * PnodoD;

typedef struct {
    PnodoD pri,ult;}TlistaD;


int main(){
 TlistaS LT;
 TlistaD PA;
 Tcola cola;
 Iniciac(&cola);


}

void eliminadom(TlistaS *LT){
    int contelim=0;
    int contot=0;
    TlistaS act,ant,elim;
    act=*LT;
    char N;
    char faux[2];
    ant=NULL;
    while (act!=NULL){
       if (act->fecha[4]=='1' && act->fecha[5]!='0'){  //si es nov o dic el turno esta bn pase lo que pase
            ant=act;
            act=act->sig;
            contot++;
       }
       else{
            if (act->dominio[5]<='9' && act->dominio[5]>='0')  //verifico que formato de dominio usa
                N=act->dominio[5];
            else
                N=act->dominio[4];
            if (N == act->fecha[5]){
                    ant=act;
                    act=act->sig;          // el turno esta bien, paso al siguiente
                    contot++;
            }
            else{                           //elimino
                elim=act;
                if (act==*LT){         //es 1er elemento
                    *LT=(*LT)->sig;
                    act=*LT;
                }
                else{
                    ant->sig=act->sig;
                    act=act->sig;
                }
                free(elim);
                contot++;
                contelim++;
            }
       }
    }
    printf("el porcentaje de turnos depurados es de %f %",(float)(contelim/contot));

}

int cantpuestos(TlistaD *PA){
    PnodoD act;
    act=(*PA).pri;
    int i=0;
    While (act!=NULL){
        i++;
        act=act->sig;
    }

  return i;
}

void atencionabril(Tcola *cola,Tlista LT,TlistaD *PA){
    Tcola colaux;
    Inicia(&colaux);
    TelementoC aux;
    Tlista act=LT;
    Sublista nuevoS,actS;
    PnodoD auxD;
    int N,ing;
    N=cantpuestos(*PA);
    while (!vaciaC(*cola)){
        SacaC(cola,&aux);
        while (act!=NULL && strcmp(act->dominio,aux)!=0)
            act=act->sig;
        if (act!=NULL){
            if (act->fecha[5]!='4')
                PoneC(&colaux,aux);
            else{
                nuevoS=(sublista) malloc (sizeof(noditoD));
                ing=rand() % N + 1;
                strcpy(nuevoS->dominio,aux);
                nuevoS->sig=NULL;
                nuevoS->obs=0;
                auxD=(*PA).pri;
                for (int i=0;i<ing;i++)
                    auxD=auxD->sig;
                  if (auxD->sub==NULL)
                    auxD->sub=nuevoS;
                  else{
                       actS=auxD->sub;
                while (actS->sig!=NULL)
                    actS=actS->sig;
                actS->sig=nuevoS;
                  }
            }
        }
        else printf("el dominio %s no tiene turno",aux);
        act=LT;
    }
   while (!vaciaC(colaux)){
    sacaC(&colaux,&aux);
    PoneC(cola,aux);
   }
}


void recorrido



void eliminautos(TlistaD *PA){
    FILE *arch;
    char dom[8];
    char puesto[4];
    int cantobs;
    char est;
    PnodoD act;
    Sublista elim,ant,actS;

    if ((arch=fopen("TESTEOS.TXT","r"))==NULL)
        printf("hay un error con el archivo");
    else{
        fscanf(arch,"%s %s %d %c",puesto,dom,cantobs,est);
        while (!feof(arch)){
            if (strcmp(PA->ult->puesto,puesto)==0)
                    act=(*PA.ult);
                else act=(*PA.pri);
            while (act!=NULL && (strcmp(act->puesto,puesto)!=0)
                    act=act->sig;
            if (act==NULL)
                    printf("el puesto ingresado no es valido");
            else{
                ant=NULL;
                actS=act->sub;
                if (actS!=NULL && strcmp(actS->dominio,dom)==0)
                    if (est=='R'){
                        elim=actS;
                        actS=actS->sig;
                        act->sub=actS;
                        free(elim);
                    }
                    else{
                while (actS!=NULL && strcmp(actS->dominio,dom)!=0);{
                    ant=actS;
                    actS=actS->sig;
                }
                if (actS!=NULL)
                    if (est=='O')
                        act->obs=cantobs;
                    else if (est=='R'){
                        elim=actS;
                        ant->sig=actS->sig;
                        free(elim);
                    }
               else printf("el dominio colocado no esta en el puesto");
            }
        }
         fscanf(arch,"%s %s %d %c",puesto,dom,cantobs,est);
        }
    }
   close(arch);

}

