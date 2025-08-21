#include <stdio.h>
#include <stdlib.h>

int main()
{
    return 0;
}


void mayormenor(arbol a,int *mayor,int *nivmayor,int *menor,int *nivmenor){

        if (a!=NULL){
            recorre(a->der,nivmayor);
            if (mayor!=0 && menor !=0){
                printf("la clave mayor es %d con nivel %d y la clave menor es %d con nivel %d",*mayor,*nivmayor,*menor,*nivmenor)
            }
            }
        }


        void recorre(arbol a,int ){
            if (a!=NULL){

            }

        }

int verifica(arbol a,pos p,int niv, int k){     //niv arranca en 1
    pos c;
    flagmay=0;
    flagmen=0;
    if (!nulo(p){
        if (niv==k){

        c=hijomasizq(p,a);
        if (!nulo(c) && !nulo(hermanoder(c,a))){            // p es de min grado 2
            while (!nulo(c) && !flagmay && !flagmen){
                if (strcmp(info(c,a)<info(p,a))<0)
                    flagmen=1;
                else
                    if (strcmp(info(c,a),info(p,a))>0)
                        flagmay=1;
                c=hermanoder(c,a);

            }
            if (flagmay && flagmen)
                return 1;
            else
                return 0;

        }
        else
            return 1;

    }
    else
        if (niv<k)
            return verifica(a,hermanoder(p,a),niv,k)&&verifica(a,hijomasizq(p,a),niv+1,k);
       else
            return 1;
    }
    else
        return 1;

}

int clavemenor(int mat[][N],int N{      //
 int j;
 int gr,grmin =-1;
 int vertice;
    for (int i=0;i<N;i++){
      if (mat[i][i]==1){
        j=0;
        gr=0;
        while (j<N){
             if ((i>j && mat[i][j]==1) || i<j&&mat[j][i]==1)
                gr++;
             j++;
        }
        if (gr % 2 == 0 && grmin>gr){
            grmin=gr;
            vertice=i;
        }

      }

    }
    return vertice;
}





