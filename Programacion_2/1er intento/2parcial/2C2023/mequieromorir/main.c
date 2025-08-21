#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Hello world!\n");
    return 0;
}

int cantarboles(arbol a,int k1,int k2){
    int cont=0;

    while (a!=NULL){
        if (claveneg(a->izq,k1,k2,1))
            cont++;
        a=a->der;
    }
    return cont;
}

int claveneg(arbol a,int k1, int k2,int niv){
    if (a==NULL)
        return 0;
    else{
        if (niv>k1 && niv<k2 && a->dato<0)
            return 1;
        else
            if (niv>k2)
                return 0;
            else
                return 0||claveneg(a->izq,k1,k2,niv+1)||claveneg(a->der,k1,k2,niv);

    }
}


void gradoa(arbol a,pos p,int k,int niv,int *maxg,int *ming){
    pos c;
    int grado=0;
    // la raiz la analizo en el main
    if (!nulo(p))
        if (niv==k){
            c=hijomasizq(p,a);
            while (!nulo(c)){
                grado++;
                c=hermanoder(c,a)
            }
            if (maxg<grado)
                *maxg=grado;
            if (ming>grado)
                *ming=grado;
            gradoa(a,hermanoder(p,a),k,niv,maxg,ming);
        }
        else
        if (niv<k){
                gradoa(a,hijomasizq(p,a),k,niv+1,maxg,ming);
                gradoa(a,hermanoder(p,a),k,niv,maxg,ming);
        }

}




