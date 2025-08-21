#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef struct nodo{
    char[20] nombre;
    struct nodo * sig;}nodo;


 typedef nodo * TlistaSal;

 typedef struct nodito{
   char[20] jugador;
   int edad;
   char estado;
   struct nodito * sig;};

 typedef nodito * Sublista;

 typedef struct nodo{
    char[20] equipo;
    int puntaje;
    struct nodo * sig;}nodo;

typedef nodo * Tlista;
