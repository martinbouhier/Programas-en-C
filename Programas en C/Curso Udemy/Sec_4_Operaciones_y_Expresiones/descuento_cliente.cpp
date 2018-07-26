/*7 Una tienda ofrece un descuento del 15% sobre el total de la compra
y un cliente desea saber cuanto deberá pagar finalmente por su compra.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
	float precio, final=0;
	printf("Ingrese el precio del producto: $");
	scanf("%f",&precio);
	final = precio * 0.85;
	printf("Usted deberá pagar: $%.2f",final);
	return 0;
	system("pause");

}
