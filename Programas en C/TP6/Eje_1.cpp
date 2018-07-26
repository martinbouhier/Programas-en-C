#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <conio.h>

int main()
{   //Variables
    char name[40];
	int cat, ant, tot;
	//Ingreso de datos
	printf("Nombre del empleado: \n");
	scanf("%s", &name);
	printf("Seleccione una categoria: \n 1 = $1500 \n 2 = $2000 \n 3 = $2500 \n");
	scanf("%d", &cat);
	printf("Años de antiguedad: \n");
	scanf("%d", &ant);
	//Calculos
	ant = ant * 100;
	//Condiciones
	switch(cat)
	{
		case 1:
			cat = 1500;
		case 2:
			cat = 2000;
		case 3:
			cat = 2500;
	}
	//Sueldo total
    tot = cat + ant;
    printf("%s: \n" , name);
	printf("Sueldo total %d \n", tot);
	system("pause");
}
