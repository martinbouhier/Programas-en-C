/*. Prueba de Divisibilidad */

#include <stdio.h>

int main(){
	int n1,n2;
	printf("Digite dos números: \n"); scanf("%i %i",&n1,&n2);
	if (n1 % n2 == 0){
		printf("El número %i es divisible por %i\n", n1,n2);
	}
    return 0;
}


