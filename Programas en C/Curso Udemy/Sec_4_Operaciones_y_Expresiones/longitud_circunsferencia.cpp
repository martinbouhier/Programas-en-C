#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
	float r, pem;
	printf("Introduzca el radio del c�rculo:\n");
	scanf("%f", &r);
	pem = 2 * M_PI * r;
	printf("\nEl per�metro del c�rculo es: %.2f", pem);
	return 0;
	system("pause");
}
