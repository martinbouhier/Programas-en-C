#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
	float c1,c2,h; // Variables
	//c1 = cateto1, c2 = cateto2, h = hipotenusa
	printf("Dados los valores de los catetos del triángulo rectangulo calcularemos la Hipotenusa:");
	printf("\nCateto1: ");
	scanf("%f", &c1);
	printf("\nCateto2: ");
	scanf("%f",&c2);
	h = sqrt(pow(c1,2)+pow(c2,2));  //sqrt es la forma de ejecutar la raiz cuadrada - y pow eleva al cualquier exponente un numero
    printf("\nLa Hipotenusa es: %f", h);
	return 0;
	system("pause");
}
