#include "persistence.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void make_persistent(struct tm **time)
{
	
    struct tm *structPtr;

	structPtr = malloc(sizeof(struct tm));

	if(structPtr == NULL) { printf("malloc failed\n"); exit(1); }

	memcpy(structPtr, *time, sizeof(struct tm));

	(*time) = structPtr;

}

void free_persistent(struct tm **time)
	{
	free(*time);
	*time = NULL;
}