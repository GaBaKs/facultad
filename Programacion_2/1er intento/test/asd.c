#include <stdio.h>
#include <string.h>

int main() {
    const char *cadena = "Hola, mundo!";
    char *posicion = strchr(cadena, 'm');

    if (posicion != NULL) {
        printf("El car�cter 'm' se encontr� en la posici�n: %1d", posicion);
    } else {
        printf("El car�cter 'm' no se encontr�.\n");
    }

    return 0;
}
