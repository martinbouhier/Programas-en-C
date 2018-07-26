#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <conio.h>
#include <math.h>

int main()
{
	int a, b, c, tot;
	printf("Ingrese el primer valor    ");
	scanf("%d", &a);
	printf("Ingrese el segundo valor    ");
	scanf("%d", &b);
	printf("Ingrese el tercer valor    ");
	scanf("%d", &c);
	tot = a + b;
	tot = tot + c;
	printf("Totales %d \n", tot);
	system("pause");	
}

