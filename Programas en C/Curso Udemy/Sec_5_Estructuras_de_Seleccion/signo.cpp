/*. Ingresar el nombre y el signo de cualquier persona e imprimir el nombre
solo si la persona es de aries, caso contrario imprimir no es de signo aries. */

#include <stdio.h>
#include <string.h>

int main(){
	char name[40], signo[30];
	printf("Introduzca el nombre:\n"); 
	gets(name);
	printf("Introduzca el signo:\n");
	gets(signo);
	if(strcmp(signo, "aries")==0){
		printf("\nEs signo Aries, su nombre es %s", name);
	}
	else{
		printf("\nNo es signo Aries");
	}
	return 0;
}
