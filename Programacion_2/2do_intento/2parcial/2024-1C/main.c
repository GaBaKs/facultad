#include <stdio.h>
#include <stdlib.h>
typedef int TElememtoA;
typedef struct nodo{
        TElememtoA dato;
        struct nodo *izq;
        struct nodo *der;
} NODO;
typedef NODO * arbol;

void addnodo(arbol* a, TElememtoA e);

int main(){
 arbol a;
 int x;

 addnodo(&a, 40);
 addnodo(&a->izq, 20);
 addnodo(&a->der, 50);
 addnodo(&a->der->der, 37);
addnodo(&a->izq->izq,3);
addnodo(&a->izq->izq->der,3);
addnodo(&a->izq->izq->der->der,2);
addnodo(&a->izq->izq->der->der->der,1);
addnodo(&a->izq->izq->der->der->der->izq,4);
addnodo(&a->izq->izq->der->der->der->izq->der,3);



 addnodo(&a->der->der->izq, 10);
 addnodo(&a->der->der->izq->der, 12);
 addnodo(&a->der->der->izq->der->der, 14);
 addnodo(&a->der->der->izq->der->der->der, 23);
 addnodo(&a->der->der->izq->der->der->der->izq, 70);
 addnodo(&a->der->der->izq->der->izq, 33);
 addnodo(&a->der->der->izq->der->izq->der, 53);

 verificabosque(a);

 return 0;

}

void addnodo(arbol* a, TElememtoA e) {
    *a = (arbol)malloc(sizeof(NODO));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}


// ejercicio 1  (55 min en total xq intento 1 male sal, intento dos fueron 14 minutos

/*

void verificabosque(arbol a){
    if (a!=NULL){
        while (a!=NULL && verifica(a)){
            a=a->der;
        }
      if (a!=NULL)
            printf("no todos los arboles verifican");
      else
        printf("todos los arboles verifican");
    }
    else
        printf("el bosque es nulo");
}


int grado(arbol a){
    int grado=0;
    while (a!=NULL){
        grado++;
        a=a->der;
    }
    return grado;
}

void gradomaximo(arbol a,int * gradomax){
    int gradoact;
    if (a!=NULL){
        gradoact=grado(a->izq);
        if (gradoact>*gradomax)
            *gradomax=gradoact;
        gradomaximo(a->izq,gradomax);
        gradomaximo(a->der,gradomax);
    }
}

int verifica(arbol a){
    int gradoraiz=grado(a->izq);
    int gradomax=gradoraiz;
    gradomaximo(a->izq,&gradomax);
    if (gradoraiz==gradomax)
            return 1;
    else return 0;

}

*/

void verificabosque(arbol a){
    if (a!=NULL){
        while (a!=NULL && verifica(a)){
            a=a->der;
        }
      if (a!=NULL)
            printf("no todos los arboles verifican");
      else
        printf("todos los arboles verifican");
    }
    else
        printf("el bosque es nulo");
}


int grado(arbol a){
    int grado=0;
    while (a!=NULL){
        grado++;
        a=a->der;
    }
    return grado;
}

void gradomaximo(arbol a,int * gradomax,int gradoraiz){
    int gradoact;
    if (a!=NULL && ((*gradomax)<=gradoraiz)){
        gradoact=grado(a->izq);
        if (gradoact>*gradomax)
            *gradomax=gradoact;
        gradomaximo(a->izq,gradomax,gradoraiz);
        gradomaximo(a->der,gradomax,gradoraiz);
    }
}

int verifica(arbol a){
    int gradoraiz=grado(a->izq);
    int gradomax=gradoraiz;
    gradomaximo(a->izq,&gradomax,gradoraiz);
    if (gradoraiz==gradomax)
            return 1;
    else return 0;

}

// ejercicio 2

/*
int verifica(arbol a,pos p){

 pos c,aux;
 int grado,gradoant;
    if (!nulo(p)){
        c=hijomasizq(p,a);
        grado=0;
        gradoant=-1;
      if (nulo(c)) // es hoja el padre
            return verifica(a,hermanoder(p,a));
        else{
         while (!nulo(c)){  //recorro todos los hijos
            aux=hijomasizq(c,a);
            while (!nulo(aux)){
                grado++;
                aux=hermanoder(aux,a);
            }
            if (gradoant<grado){
                c=hermanoder(p,a);
                grado=0;
                gradoant=grado;
            }
            else
                return verifica(a,hermanoder(p,a)) || verifica(a,hijomasizq(p,a));
          }
          return 1;
        }
    }
    else return 0;

}


*/

/*   ejer 2 bien hecho(11 min)
int verifica(arbol a,pos p){
    pos c;
    pos nieto;
    int flag=0;
    int gradoant=-1,gradoact;
    if (!nulo(p)){
        c=hijomasizq(p,a);
       if (!nulo(c)){           // p es hoja
        while (!nulo(c) && !flag){
            gradoact=0;
            nieto=hijomasizq(c,a);
            while (!nulo(nieto)){
                gradoact++;
                nieto=hermanoder(nieto,a);
            }
            if (gradoact<gradoant)
                flag=1;
            else{
                c=hermanoder(c,a);
                gradoant=gradoact;
            }
        }
        if (!flag)
            return 1;
        else
            return verifica(a,hermanoder(p,a)) || verifica(a,hijomasizq(p,a));
      }
      return verifica(a,hermanoder(p,a));
    }
   else
        return 0;
}


*/
typedef struct{
    int alcanza,alcanzado;}Tvec
}

void generovec(int mat[][MAX],int i,int j,int N,Tvec vec[MAX]){

    if (j>=0 && mat[j][j]!=1){
        if (i>=0){
            if (mat[i][j]==1 && (i!=j)){
                vec[i].alcanza++;
                vec[j].alcanzado++;
            }
                generovec(mat,i-1,j,N,vec);
        }
       else
        generovec(mat,N-1,j-1,N,vec)
    }
    else if (j>=0)
        generovec(mat,N-1,j-1,N,vec);
}


int cuentanodos(Tvec vec[MAX],int N){
    int cont;
    for (int i=0;i<N;i++){
        if (vec[i].alcanza==vec[i].alcanzado)
            cont++;

    }
    return cont;


}









