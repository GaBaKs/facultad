#include <stdio.h>
#include <string.h>

int main() {
    const char *cadena = "Hola, mundo!";
    char *posicion = strchr(cadena, 'm');

    if (posicion != NULL) {
        printf("El carácter 'm' se encontró en la posición: %1d", posicion);
    } else {
        printf("El carácter 'm' no se encontró.\n");
    }

    return 0;
}
