/* Dadas las horas trabajadas de una persona y el valor por hora,
calcular su salario e Imprimirlo.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
	int horas;
	float pagoxhora,salario;
	printf("Ingrese el número de horas trabajadas: ");
	scanf("%i",&horas);
	pagoxhora = 120;
	salario = horas * pagoxhora;
	printf("El salario del empleado es: $%.2f",salario);
	return 0;
	system("pause");
}
