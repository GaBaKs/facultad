#include <stdio.h>
#define MASC_TOPB  0x30 //0011 0000
#define MASC_CODOP 0x1F      //0001 1111
#define MASC_TOPA  0x30      //0011 0000
#define MASC_TOPB  0xC0      //1100 0000
#define MASC_CODMOV 0x1F //0001 1111
#define MASC_OFFMOV 0x00FFFF //0000 0000 1111 1111 1111 1111
#define CANTCELDAS 4
#define LAR 0   // Acceso de memoria
#define MAR 1   // Acceso de memoria
#define MBR 2   // Acceso de memoria
#define IP  3   // Instruccion
#define OPC 4   // Instruccion
#define OPA 5   // Instruccion
#define OPB 6   // Instruccion

#define EAX 10  //Registro de proposito general
#define EBX 11  //Registro de proposito general
#define ECX 12  //Registro de proposito general
#define EDX 13  //Registro de proposito general
#define EEX 14  //Registro de proposito general
#define EFX 15  //Registro de proposito general
#define AC  16  //Acumulador y Resto de la ALU
#define CC  17  //Codigo de condicion resultados N y Z

#define CS  26  //Segmento de codigo
#define DS  27  //Segmento de datos

typedef struct{
    int reg[32];           // Cantidad de registros
    unsigned char mem[16384];            // Cantidad de memoria
    unsigned char codigo_error;            // Codigo de error
    unsigned short tabla_seg[4];
} TipoMKV;


int logifisi(TipoMKV MKV,int dirlog){
    int dirfis,segmento,offset;
    segmento=dirlog>>16;
    offset=dirlog & 0x0000FFFF;
        if (segmento==0){ //Segmento de codigo
            dirfis=MKV.tabla_seg[0]+offset;//Direccion fisica = base CS + direccion logica
            if (dirfis>=MKV.tabla_seg[0] && dirfis<=MKV.tabla_seg[2]) //Verifica que la direccion fisica este dentro del segmento de codigo
                return dirfis;
            else
                return -1;
        }
        else{
            dirfis=MKV.tabla_seg[2]+offset; //Direccion fisica = base DS + direccion logica
            if (dirfis>=0 && dirfis<=MKV.tabla_seg[3]) //Verifica que la direccion logica este dentro del segmento de datos
                return dirfis;
            else
                return -1;
        }
}

int get_direccion_A(TipoMKV MKV,int opA,int TopA){
    int dirfis;
    //mov[reg + cte ],opb / mov [cte],opb / mov [reg],opb contemplar estos casos
    int offset=0,cod; // para tipo memoria
    if (TopA==3){
        offset= opA & MASC_OFFMOV;  //devuelve el offset
        cod = (opA >> 16) & MASC_CODMOV;
    }
    else
        cod=opA;
    if((dirfis=logifisi(MKV,MKV.reg[cod]))!=-1)
        return offset+dirfis;
    else{
        printf("error");
    }

}

int get_Valor(TipoMKV *MKV,int op,int Top){


    if (Top==1)
        return MKV->reg[op];
    else
        if (Top==2)
            return op;
        else
            if (Top==3){
                int valor=0,aux;
                int dirlog=0x00010000; //+ MKV->reg[(op & 0x001F00) >> 16]+ op & MASC_OFFMOV;
                printf("valor dirlog: %x \n",dirlog);
                int dirfis=logifisi(*MKV,dirlog);
                printf("valor dirfis: %d \n",dirfis);
                for (int i=0;i<4;i++){
                   aux=MKV->mem[dirfis+1+i];
                   valor+=aux<<(3-i)*8;
                   printf("valor valor: %x \n",valor);
                   printf("valor dirfis+1+i: %d \n",dirfis+1+i);
                   printf("valor memoria: %x \n",MKV->mem[dirfis+1+i]);
                }
                return valor;
            }
}


void MOV(TipoMKV *MKV,int opA, int TopA, int opB, int TopB){ //hacer bien
    int dirfis,i;
    int offset,cod; // para tipo memoria

    int valorB=get_Valor(MKV,opB,TopB);
    printf("el valor de B es de %x",valorB);
        if (TopA==3){
            dirfis=get_direccion_A(*MKV,opA,TopA);
            if (dirfis+CANTCELDAS<=16384 && dirfis>=MKV->tabla_seg[3])
                for (i=CANTCELDAS;i<0;i--){
                    MKV->mem[dirfis++]=(char)(valorB >> ((i-1)*8)) & 0x000000FF ;
                }
        }
        else
            MKV->reg[opA]=valorB;
}

//mov edx , DS


void test(TipoMKV *MKV){

char instruccion=0x30;  //1010 0000   1101
MKV->mem[4]=0x01;
MKV->mem[5]=0x01;
MKV->mem[6]=0x01;
MKV->mem[7]=0x01;
MKV->mem[8]=0x01;
MKV->mem[9]=0x01;
MKV->mem[10]=0x01;
MKV->reg[OPC]=0X00000010;
MKV->reg[OPA]=0X0100000D;   //edx
MKV->reg[OPB]=0x0100001B;   //ds
MKV->reg[DS]=0x00010000;
MKV->reg[EDX]=22;
int opA=0x0000000D;
int TopA=0x01;
int TopB=0x03;
int opB=0x0000;

printf("valor incial de edx: %d \n",MKV->reg[EDX]);
MOV(MKV,opA,TopA,opB,TopB);
printf("el valor final de edx es %x",MKV->reg[EDX]);

    }

int main(){




TipoMKV MKV;
MKV.tabla_seg[0]=0;
MKV.tabla_seg[1]=4;
MKV.tabla_seg[2]=4;
MKV.tabla_seg[3]=16384-4;
test(&MKV);

    return 0;

}
