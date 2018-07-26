#include <stdio.h>
#include <stdlib.h>

int main(void){   
    //Variables
	int n1,n2,suma=0,resta=0,mult=0,div=0;
	printf("Introduzca el primer número: \n");
	scanf("%i", &n1);
	printf("Introduzca el segundo número: \n");
	scanf("%i", &n2);
	suma = n1 + n2;
	resta = n1 - n2;
	mult = n1 * n2;
	div = n1 / n2;
	printf("Resultados: \n");
	printf("n1: %i \n", n1);
	printf("n2: %i \n", n2);
	printf("Suma: %i\nResta: %i\nMultiplicación: %i\nDivision: %i\n", suma, resta, mult, div);
	system("pause");
}
