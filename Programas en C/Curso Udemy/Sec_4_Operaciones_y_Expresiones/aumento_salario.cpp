/*. Calcular el nuevo salario de un obrero si obtuvo un incremento del 25%
sobre su salario anterior. */

#include <stdio.h>
#include <stdlib.h>

int main(){
	float sal_ant, perc=1.25, sal_act;
	printf("Introduzca su salario: \n$");
	scanf("%f", &sal_ant);
	sal_act = sal_ant * perc;
	printf("Su nuevo salario es:\n$%.2f\n", sal_act);
		
	system("pause");
	return 0;
}
