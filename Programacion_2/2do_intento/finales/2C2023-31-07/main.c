



//ejercicio 3


 int verifica (arbol a, pos p){

    pos c;
    int flag=0;
    if (!nulo(p) && !nulo(hijomasizq(p,a))){
        c=hijomasizq(p,a);
        while (!nulo(c) && !flag){
            if (info(p,a)<info(c,a))
                c=hermanoder(c,a);
            else
                flag++;    
        }
        if (!flag)
            return 1;
        else
            return verifica(a,hijomasizq(p,a))||verifica(a,hermanoder(p,a));
    }
    else
        return 0;
 }



// ejercicio 4
    #include <ctype.h>
    int recorrebosque(arbol a){
        int cont=0;
      while (a!=NULL){  
        if (esvocal(a.dato) && hijoscumplen(a->izq))
            cont+=cumple(a->izq,1);
        else
            cont+=cumple(a->izq,0);    
        a=a->der;
      }  
      return cont;

    }

    int esvocal(char dato){
        tolower(dato);
        if (dato=='a' || dato=='e'||dato=='i'||dato=='o'||dato=='u')
            return 1;
        else
         return 0;
    }

   int cumple(arbol a,int contnodos){
    arbol hijo;
        if (a!=NULL){
            if (hijoscumplen(a->izq))
                return cumple(a->izq,contnodos+1)||cumple(a->der,contnodos+1);
            else
                return cumple(a->izq,contnodos)||cumple(a->der,contnodos);
        }
          if (contnodos>=2)
              return 1;
          else
              return 0;

   } 


   int hijoscumplen(arbol a){
   int flag=1;
    while (a!=null && flag){
        if (esvocal(a.dato))
            flag=0;
        a=a->der;    
    }
    return flag;

   }