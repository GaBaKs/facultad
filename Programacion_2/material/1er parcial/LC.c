#include <stdio.h>
#include <stdlib.h>

typedef struct nodo{
    char Letra;
    struct nodo *sig;}nodo;
typedef nodo* TListaC;

int CargaLC(TListaC*);
void InsertOrdLC(TListaC*, char);
void InsertLC(TListaC*, char);
void ImprLC(TListaC);
void CantVoc(TListaC);
void EstaOrdLC(TListaC);
void ElimPos(TListaC*, int);

int main()
{
    TListaC LC;
    int Pos;

    if (CargaLC(&LC)==1)
        printf("Error: Archivo inexistente \n");
    else
    {
        ImprLC(LC);
        CantVoc(LC);
        EstaOrdLC(LC);
        printf("Inserte la Pos del nodo a eliminar \n");
        scanf("%d",&Pos);
        ElimPos(&LC,Pos);
        ImprLC(LC);
    }
    return 0;
}
int CargaLC(TListaC *LC)
{
    FILE* ArchT;
    char C;

    ArchT=fopen("Datos LC.txt","rt");
    if (ArchT==NULL)
        return 1;
    else
    {
        *LC=NULL;
        fscanf(ArchT," %c",&C);
        while(!feof(ArchT))
        {
            //InsertOrdLC(LC,C);
            InsertLC(LC,C);
            fscanf(ArchT," %c",&C);
        }
        fclose(ArchT);
        return 0;
    }
}
void InsertOrdLC(TListaC *LC, char C)
{
    TListaC Aux, Ant, Act;

    Aux=(TListaC)malloc(sizeof(nodo));
    Aux->Letra=C;
    if (*LC==NULL)
    {//recordar que LC apunta al "Ult"
        Aux->sig=Aux;
        *LC=Aux;
    }
    else
    {
        if (Aux->Letra > (*LC)->Letra)
        {//reviso insertar al final
            Aux->sig=(*LC)->sig;
            (*LC)->sig=Aux;
            *LC=Aux;
        }
        else
        {
            Ant=*LC;
            Act=(*LC)->sig;
            while(Aux->Letra > Act->Letra)
            {
                Ant=Act;
                Act=Act->sig;
            }
            Ant->sig=Aux;
            Aux->sig=Act;
        }
    }
}
void InsertLC(TListaC *LC, char C)
{
    TListaC Aux;
    //inserto por llegada, no ordenadamente
    Aux=(TListaC)malloc(sizeof(nodo));
    Aux->Letra=C;
    if (*LC==NULL)
    {//cabeza
        Aux->sig=Aux;
        *LC=Aux;
    }
    else
    {//final
        Aux->sig=(*LC)->sig;
        (*LC)->sig=Aux;
        *LC=Aux;
    }
}
void ImprLC(TListaC LC)
{
    TListaC Aux;

    Aux=LC->sig;
    if (Aux!=NULL)
    {
        if (Aux==LC)//un solo nodo
            printf("%c ",Aux->Letra);
        else
        {
            while (Aux!=LC)
            {
                printf("%c ",Aux->Letra);
                Aux=Aux->sig;
            }
            printf("%c ",Aux->Letra);
        }
        printf("\n");
    }
}
void CantVoc(TListaC LC)
{
    TListaC Aux;
    int Cont=0;

    Aux=LC->sig;
    if (Aux!=NULL)
    {
        if (Aux==LC)
        {//Caso un solo nodo
            if(Aux->Letra== 'a' || Aux->Letra== 'e' || Aux->Letra== 'i' || Aux->Letra== 'o' || Aux->Letra== 'u')
                Cont++;
        }
        else
        {
            while (Aux!=LC)
            {//Nodos intermedios
                if(Aux->Letra== 'a' || Aux->Letra== 'e' || Aux->Letra== 'i' || Aux->Letra== 'o' || Aux->Letra== 'u')
                    Cont++;
                Aux=Aux->sig;
            }
            //Ultimo nodo, LC
            if(Aux->Letra== 'a' || Aux->Letra== 'e' || Aux->Letra== 'i' || Aux->Letra== 'o' || Aux->Letra== 'u')
                Cont++;
        }
        if (Cont==0)
            printf("No hay ninguna vocal en la LC \n");
        else
            printf("En total se encontraron %d vocales \n", Cont);
    }
}
void EstaOrdLC(TListaC LC)
{
    TListaC Aux;

    Aux=LC->sig;
    if (LC!=NULL)
    {
        while(Aux!=LC && Aux->Letra <= Aux->sig->Letra)
        {
            Aux=Aux->sig;
        }
        if (Aux==LC)
            printf("La lista esta ordenada \n");
        else
            printf("La lista NO esta ordenada \n");
    }
}
void ElimPos(TListaC *LC, int Pos)
{
    TListaC Aux, Act, Ant;
    int i;

    Aux=(*LC)->sig;
    if (Pos==0)
    {
        if (Aux == *LC)
            *LC=NULL;//un solo nodo
        else
            (*LC)->sig=Aux->sig;
        free(Aux);
    }
    else
    {
        Act=(*LC)->sig;
        for(i=0;i<Pos;i++)
        {
            Ant=Act;
            Act=Act->sig;
        }
        if (Act==*LC)
            *LC=Ant;//Si es el ultimo
        Ant->sig=Act->sig;
        free(Act);
    }
}
