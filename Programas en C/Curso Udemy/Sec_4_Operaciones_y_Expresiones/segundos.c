/*. Calcular la cantidad de segundos que están incluidos en el número de horas,
minutos y segundos ingresados por el usuario.*/

#include <stdio.h>

int main(){
	int horas, minutos, segundos, t1, t2, t3, total;
	printf("Digite la cantidad de horas: ");
	scanf("%i", &horas);
	printf("Digite la cantidad de minutos: ");
	scanf("%i", &minutos);
	printf("Digite la cantidad de segundos: ");
	scanf("%i", &segundos);
	t1 = horas * 3600;
	t2 = minutos * 60;
	t3 = segundos;
	total = t1 + t2 + t3;
        printf("\nCantidad de segundos: %i\n",total);
    	return 0;
}
