#include <stdio.h>
#include <conio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>

int main()
{
	int l1, l2;
	float sup, per, hip;
	system("cls");
	// Entrada de datos
	printf("Ingrese el primer lado    ");
	scanf("%d", &l1);
	printf("Ingrese el segundo lado    ");
	scanf("%d", &l2);
	// Calculos
	sup = (l1 * l2) / 2;
	hip = sqrt(pow(l1, 2) + pow(l2, 2));
	per = (l1 + l2 + hip);
	printf("\n La Hipotenusa es %0.2f \n", hip);
	printf("\n La Superficie es %0.2f \n", sup);
	printf("\n El Perimetro es %0.2f \n", per);
	system("pause");
}
