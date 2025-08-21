#include <stdio.h>




void vertice(int mat[][MAX],int N){
    int adyacente;
    int contadyacente=0;
    int cont;
    for (int i=0;i<N;i++){
        cont=0;
        for (int j=0;j<N;j++){
            if (i!=j && mat[i][j]==1)              // vertice adyacente
                if (gradosalida(mat,j,N))
                    cont++;
        }
        if (contadyacente<cont){
            contadyacente=cont;
            adyacente=i;
        }

    }

 printf("el vertice con la mayor cantidad de vertices adyacentes es %d con %d vertices de grado 0",adyacente,contadyacente);
}

int gradosalida(int mat[][MAX],int j,int N){
    int flag=1;
    int i=0;
    while (i<N && flag)
        if (mat[j][i]==1)
            flag=0;
        else
            i++;
     return flag;
}



int nodos(arbol a, pos p,int k1,int k1, int niv){
    pos c;
    int gr;
    int flag=0;
    if (!nulo(p)){
       if  (niv<k2  && niv > k1){
            c=hijomasizq(p,a);
            gr=0;
            while (!nulo(c) && !flag){
                gr++;
                if ((hijomasizq(p,a)==c || hermanoder(c,a)==NULL)  && info(c,a)<niv)
                    flag=1;
                c=hermanoder(c,a);
            }
            if (!flag && gr>1)
                return 1+nodos(a,hijomasizq(p,a),k1,k2,niv+1)+nodos(a,hermanoder(p,a),k1,k2,niv);
            else
                return nodos(a,hijomasizq(p,a),k1,k2,niv+1)+nodos(a,hermanoder(p,a),k1,k2,niv);

       }
       else
           if (niv<k2)
                    return nodos(a,hijomasizq(p,a),k1,k2,niv+1)+nodos(a,hermanoder(p,a),k1,k2,niv+1);
           else return 0;
    }
    else return 0;

}*


int esconexo(mat[][MAX],int u){

int vv[MAX];
int cc=0;
Tcola C;
TelementoC x;
int i,j;
IniciaC(&C);
    if (notodosvis(vv,u)){
        i=0;
        while (vv[i]!=0)
            i++;
        cc++;
        poneC(&C,i);
        vv[i]=cc;
        while (!vacia(c) && notodosvis(vv,u)){
            j=0;
            sacaC(&C,&x);
            while (j<u){
                if (mat[x][j]!=0 && vv[j]==0){
                    poneC(&C,j);
                    vv[j]=cc;
                }
                j++;

            }
        }
        return vacia(C)? 1 : 0;         //1 si no es conexo 0 si es conexo

    }


}







