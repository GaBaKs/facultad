#include <stdio.h>
#include <stdlib.h>

//ejer 1
//a) esto es incorrecto, ya que Floyd busca el costo de camino minimo, y no tiene sentido que en la diagonal haya un valor diferente de 0 ya que el
//menor valor para ir a si mismo es 0. No tiene nada que ver si es conexo o no.
//b) Falso. se debe hacer a la vuelta, desde la clave insertada a la raiz.






//ejer 3


    int menorclave(arbol a, pos p,int k,int niv){
        pos c;
        int min=9999;
        int trae;
        if (k==1==niv){
            if (!nulo(hijomasizq(p,a)))
                return info(p,a);
        }
        else

        if (!nulo(p)){
            c=hijomasizq(p,a);
            if (niv==k-1){
                while (!nulo(c)){
                    if (!nulo(hijomasizq(c,a)) && min>info(c,a))
                        min=info(c,a);
                    c=hermanoder(c,a);    
                }
                return min!=9999? min : -1;
            }
            else
             if (niv<k){
                while (!nulo(c)){
                    trae=menorclave(a,c,k,niv+1);
                    if (trae!=-1 && trae<min)
                        min=trae;
                    c=hermanoder(c,a);    
                }
                return min!=9999? min:-1;
             }
             else
                return -1;
        }
        else return -1;

    }

    //ejercicio 4


        void actualizacola(Tmat G,int N,Tcola *C){
            TelementoC cent,datoC;
            cent.id1=9999;
            PoneC(C,cent);
            SacaC(C,&datoC);
            while (datoC.id1!=cent.id1){
                if (cumple(mat,N,datoC)){
                    PoneC(C,datoC);
                }
                SacaC(C,&datoC);
            }



        }


        int cumple(Tmat G,int N,TelementoC datoC){
            int valor;
            if (datoC.id1>datoC.id2)
                valor=G[datoC.id1-1][datoC.id2-1];
            else
                valor=G[datoC.id2-1][datoC.id1-1];
            if (valor!=0 && valor<=datoC.cos)
                return 1;
            else
                return 0;


        }



        /hallar la cant de nodos de grado par

        int gradopar(arbol a){
            int gr=0;
            arbol hijo;
            if (a!=NULL){
                hijo=a->izq;
                while(hijo!=NULL){
                    gr++;
                    gradopar+=gradopar(hijo);
                    hijo=hijo->der;
                }
                if (gr!=0 && gr%2==0)
                    return 1;
                else
                    return 0;
            }
            else
                return 0;



        }
        