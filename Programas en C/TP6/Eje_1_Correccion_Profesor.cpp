#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <conio.h>
# include<string.h>

int main()
{   //Variables
    char name[40],aux[40];
	int cat, ant, tot=0, val, aux2,max,i,plus;
	//Ingreso de datos
	// qu ciclo, invente yo un for, fijate que te dice
	for(i=1;i<=3;i++)
	                 {
                     	printf("Nombre del empleado: \n");
                     	fflush(stdin);
                      	gets(name);
	                    //scanf("%s", &name); es mejor gets que scanf
                        printf("Seleccione una categoria: \n 1 = $1500 \n 2 = $2000 \n 3 = $2500 \n");
                       	scanf("%d", &cat);
                       	printf("Años de antiguedad: \n");
                       	scanf("%d", &ant);
                          	//Calculos
                           	plus = ant * 100;
                            	//Condiciones
                             	switch(cat)
                                	{
                                  		case 1:
                                    			val = 1500;
	                                   	case 2:
	                                    		val = 2000;
                                       	case 3:
                                        		val = 2500;
                                     }
                         //Sueldo total
                          tot = val + plus;
                          printf("%s: \n" , name);
                          printf("Sueldo total %d \n", tot);
	                      // maximo sueldo, solo hay uno
	                      if(i==1)
	                              {
                                   max= tot;
                                   strcpy(aux,name);
                                   aux2= cat;
                                   }
                          if (tot>max)
                                    {
                                      max= tot;
                                      strcpy(aux,name);
                                      aux2= cat;
                                      }
                     } // cierro el for
                     
                      printf("el Sueldo maximo es %d del empleado %s , categoria %d\n", max,aux,aux2);                 
	system("pause");
}
