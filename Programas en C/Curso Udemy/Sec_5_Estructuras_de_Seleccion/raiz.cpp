/*. Ingrese un numero y calcule su raiz cuadrada,
si el número es negativo imprima dicho numero y un mensaje que diga
tiene raíz imaginaria. */

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
	float a,raiz;
	printf("Ingrese un número:\n"); scanf("%f", &a);
	if (a > 0 || a == 0){
		raiz = sqrt(a); printf("la raíz de %.2f es %.2f\n", a,raiz);
	}
	else{
		printf("El número %.2f tiene raíz imaginaria");
	}
	return 0;
	system("pause");
}
