/*. Número positivo o negativo .*/

#include <stdio.h>

int main(){
	int entrada;
	printf("Digite un entero:\n"); scanf("%i", &entrada);
	if(entrada >= 0){
		printf("Su número es positivo\n");
	}
	else{
		printf("Su número es negativo\n");
	}
	return 0;
}