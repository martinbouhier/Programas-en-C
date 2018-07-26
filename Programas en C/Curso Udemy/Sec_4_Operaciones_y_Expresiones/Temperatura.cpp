#include <stdio.h>
#include <stdlib.h>

int main(){
	int c,m=32,f=0;
	printf("Conversor de grados Celsius a Fahrenheit");
	printf("\nIntroduzca la temperatura en Celsius:");
	scanf("\n%i",&c);
	printf("\nUn Grado Celsius corresponde a %i grados Fahrenheit",m);
	f = c * m;
	printf("\n%i Celsius a Fahrenheit: %i\n",c,f);
	system("pause");
}
