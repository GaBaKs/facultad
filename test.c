#include <stdio.h>

// Función de ejemplo
void saludar(char *nombre) {
    printf("Hola, %s!\n", nombre);
}

int main() {
    // Declara un puntero a función que toma un puntero a char y no devuelve nada
    void (*ptr_saludo)(char *);

    // Asigna la dirección de la función saludar al puntero
    ptr_saludo = saludar;

    // Llama a la función a través del puntero
    ptr_saludo("Mundo"); // Salida: Hola, Mundo!

    return 0;