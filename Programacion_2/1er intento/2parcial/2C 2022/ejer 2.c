#include <stdio.h>
#include <stdlib.h>



int mayor(arbol a,pos p,int g){

    if (nulo(p))
        return -1;
    else{
        int mayorizq=mayor(a,hijomasizq(p,a,),g);
        int mayorder=mayor(a,hermanoder(p,a),g);
        int max;
        int grado=0;
        c=hijomasizq(p,a);
        while (!nulo(c)){
            grado++;
            c=hermanoder(p,a);
        }
        max = (mayorizq<mayorder)? mayorder:mayorizq;
        if (grado == g || grado == 2*g)
            return (info(p,a)>max)? info(p,a):max;
        else return -1;

    }
}


int verifica(arbol a,int k,int niv){
    if (a!=NULL){
        if (k-1==niv)
            if (a->izq!=NULL && a->der!=NULL)
                if (a->izq->dato>a->dato && a->der->dato<a->izq->dato && a->der->dato>a->dato)
                    return 1;
                else return 0;
            else{
                if (a->izq!=NULL)
                    if (a->izq->dato>a->dato)
                        return 1;
                    else
                        return 0;
            }
            return verifica(a->izq,k,niv+1)&&verifica(a->der,k,niv+1);

}


}

int verifica(arbol a,int k,int niv){
    int flag=0;
    if (a!=NULL){
        if (k-1==niv){
            if (a->izq!=NULL && a->der!=NULL)
                if (a->izq->dato>a->dato && a->der->dato<a->izq->dato)
                    flag=1;
                else flag=0;
            else{
                if (a->izq!=NULL)
                    if (a->izq->dato>a->dato)
                        flag=1;
                    else
                        flag=0;
            }
            if (a->der!=NULL)
                if (a->der->dato<a->dato)
                    flag=1;
            return flag;

        }
         else
             return verifica(a->izq,k,niv+1)&&verifica(a->der,k,niv+1);

}


}

