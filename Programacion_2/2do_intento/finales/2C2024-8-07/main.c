





    int verifica(arbol a, pos p,int cont){
        pos c;
        int gr=0;
        int cumple=0;
        if (!nulo(p) && cont<3){
            c=hijomasizq(p,a);
            while (!nulo(c)){
                gr++;
                cumple=verifica(a,c,cont);
                c=hermanoder(c,a);
            }
            if (gr==3){
                cont+1
            }



        }



    }


     int verifica(arbol a, pos p,int cont){
        int gr;
        int cumple=0;
        if (!nulo(p) && cont<3){
            gr=grado(hijomasizq(p,a));
            if (gr==3)
                return 1+verifica(a,hijomasizq(p,a),cont+1)+verifica(a,hermanoder(p,a),cont+1);
            else
                return verifica(a,hijomasizq(p,a),cont)+verifica(a,hermanoder(p,a),cont);
        }
        else
            return 0;
