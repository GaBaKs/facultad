#include <stdio.h>
#include <stdlib.h>


typedef struct nodo{



}



int main(){


}


int privocal(arbol a){          //MAL, tiene que calcular con intervalos y no mandar variable ocmpleta

if (a->dato[0]=='a' || a->dato[0]=='e' || a->dato[0]=='i' || a->dato[0]=='o' || a->dato[0]=='u' || a->dato[0]=='A' || a->dato[0]=='E' || a->dato[0]=='I'|| a->dato[0]=='O'|| a->dato[0]=='U')
    return 1;
 else return 0;

}

int privocal(char letra){
    if ((letra>'a' && letra<='z') || (letra>'A' && letra<='Z') && (a->dato[0]!='a' || a->dato[0]!='e' || a->dato[0]!='i' || a->dato[0]!='o' || a->dato[0]!='u' || a->dato[0]!='A' || a->dato[0]!='E' || a->dato[0]!='I'|| a->dato[0]!='O'|| a->dato[0]!='U'))
        return 0;
     else return 1;

}


int grado(arbol a){
int cont=0;
    while (a!=NULL){
        cont++;
        a=a->der;
    }
   return cont;

}

int verifica(arbol a){
  if (a!=NULL){
    if (a->izq==NULL)   //verifico que el nodo no sea hoja
        return verifica(a->der);
    else{
         if (!privocal(a) && (grado(a->izq) % 2)==0)
            return 0;
         else return verifica(a->izq)&&verifica(a->der);
    }
  }
  else return 1;
}

void recorrobosque(arbol a){
   int flag=1;
    if (a==NULL)
        printf("el bosque esta vacio");
    else{
        while (a!=NULL && flag){
            if (!privocal(a) && (grado(a->izq)% 2)==0)
                    flag=1;
            else
                flag=verifica(a->izq);
            a=a->der;
        }
        if (!flag)
            printf("no todos los arboles cumplen");
        else
            printf("todos los arboles cumplen");
    }
}

int contnodos(arbol a,pos p,int niv,int k){         // niv<k 1er hijo hoja multiplos dps sumo
    pos c;
    int flag=0;
        if (!nulo(p) && niv<k){
            c=hijomasizq(p,a);
            if (!nulo(c) && nulo(hijomasizq(c,a))){       // 1er hijo hoja
                    c=hermanoder(c,a);
                    if (!nulo(c)){                        //compruebo si tiene hermanos
                        while (!nulo(c)&& !flag){
                            if(info(c,a) % info(hijomasizq(p,a))==0)            // es multiplo
                                c=hermanoder(c,a);
                            else
                                flag=1;
                        }
                        if (flag)
                            return contnodos(a,hijomasizq(p,a),niv+1,k)+contnodos(a,hermanoder(p,a),niv,k);
                        else
                            return 1+contnodos(a,hijomasizq(p,a),niv+1,k)+contnodos(a,hermanoder(p,a),niv,k);

                    }
                    else
                        return contnodos(a,hijomasizq(p,a),niv+1,k)+contnodos(a,hermanoder(p,a),niv,k);
            }
            else
               if (nulo(c))
                return contnodos(a,hermanoder(p,a),niv,k);
                else
                    return contnodos(a,hijomasizq(p,a),niv+1,k)+contnodos(a,hermanoder(p,a),niv,k);
        }
        else
            return 0;

}



int cumple(int M[][N],TvecL L,int N,int i,int j){
    int i,j;
    int z=N-1;
    int flag=0;
    while (z>=0 && !flag){
        if (M[z][z]==0 && gradoM(M,N-1,z)% 2 ==0){
            if (cumplelista(L,z))
                z=z-1;
            else
                    flag=1;
        }
        else
            flag=1;
    }
    if (flag)
        return 0;
    else
        return 1;
}

int gradoM(int M[][N],int i,int j){

            if (i>=0 && M[i][j]!=0)
                    return M[i][j]+cumpleM(M,i-1,j);
            else
                if(i>=0)
                    return cumpleM(M,i-1,j);
                else
                    return 0;

    }

int cumplelista(TvecL L,int z){
    int gradoS=0;
    int bucle=0;
    Tlista aux;
    aux=L[z].lista;
    while (aux!=NULL){
       gradoS+=aux->pond;
       if (!bucle && aux->vertice==z)
            bucle=1;
       aux=aux->sig;
    }
    if (gradoS % 2 ==1 && bucle)
        return 1;
    else
        return 0;

}


