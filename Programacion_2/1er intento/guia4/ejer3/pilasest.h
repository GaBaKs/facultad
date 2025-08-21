#define MAX 50

typedef struct {
    char st[MAX];
} TElementoP;


typedef struct {
TElementoP datos[MAX];
int tope; } TPila;

    void poneP(TPila *P, TElementoP x);
    void sacaP(TPila *P, TElementoP* x);
    TElementoP consultaP(TPila P);
    int VaciaP(TPila P);
    void IniciaP (TPila *P);
