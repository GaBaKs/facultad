#define MAX 50

typedef int TElementoC;
typedef struct {
TElementoC datos[MAX];
 int pri, ult; } TCola;

 void IniciaC (TCola *C);

 int VaciaC(TCola C);

 void poneC (TCola *C, TElementoC X);

 void sacaC (TCola *C, TElementoC *X);

 TElementoC consultaC (TCola C);
