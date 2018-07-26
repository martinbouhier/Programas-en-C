/*. Visualizar la tarifa de la luz según el gasto de corriente eléctrica.
Para un gasto menor de 1.000Kwxh la tarifa es 1.2,
entre 1.000 y 1850 es de 1.0 y mayor a 1850 0.9.*/

#include <stdio.h>
#define TARIFA1 1.2
#define TARIFA2 1.0
#define TARIFA3 0.9

int main(){
	float consumo,gasto;
	printf("Ingrese el consumo de luz en Kwxh:\n"); scanf("%f",&consumo);
	if(consumo < 1000){
		gasto = consumo * TARIFA1;
		printf("Su gasto fue de: $%.2f\n",gasto);
	} else{
		if (1850 > consumo && consumo > 1000){
			gasto = consumo * TARIFA2;
			printf("Su gasto fue de: $%.2f\n",gasto);
		} else{
			gasto = consumo * TARIFA3;
			printf("Su gasto fue de: $%.2f\n",gasto);
		}
	}
	return 0;
}

