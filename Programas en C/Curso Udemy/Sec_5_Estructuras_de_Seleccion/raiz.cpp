/*. Ingrese un numero y calcule su raiz cuadrada,
si el n�mero es negativo imprima dicho numero y un mensaje que diga
tiene ra�z imaginaria. */

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
	float a,raiz;
	printf("Ingrese un n�mero:\n"); scanf("%f", &a);
	if (a > 0 || a == 0){
		raiz = sqrt(a); printf("la ra�z de %.2f es %.2f\n", a,raiz);
	}
	else{
		printf("El n�mero %.2f tiene ra�z imaginaria");
	}
	return 0;
	system("pause");
}
