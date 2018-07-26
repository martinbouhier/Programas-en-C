/*. Problema 10.
Un Alumno desea saber cual ser� su calificaci�n final en la materia de Algoritmos. 
Dicha calificaci�n se compone de los siguientes porcentajes:
-55% del promedio de sus 3 calificaciones parciales.
-30% de la calificaci�n del examen final.
-15% de la calificaci�n de un trabajo final.*/

#include <stdio.h>
#include <stdlib.h>
#define PARCIALES 0.55
#define FINAL 0.30
#define TP 0.15

int main(){
	float c1,c2,c3,efinal,tfinal,p1,p2,p3,nota; 
	printf("Ingrese Parcial1, Parcial2, Parcial3, ExamenFinal, TPFinal:\n"); scanf("%f %f %f %f %f", &c1, &c2, &c3, &efinal, &tfinal);
	p1 = ((c1 + c2 + c3) / 3) * PARCIALES;
	p2 = efinal * FINAL;
	p3 = tfinal * TP;
	nota = p1 + p2 + p3;
	printf("Su nota final es: %.2f\n", nota);
	system("pause");
	return 0;
}
