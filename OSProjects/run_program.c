#include "run_program.h"
#define ERROR_CODE 127
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int run_program(char *file_path, char *argv[])
{
    (void) file_path;
    (void) argv;
	pid_t pid;
    int wstatus;
	int return_val;

	if (file_path == NULL) {
		return ERROR_CODE;
	}

	switch( pid = fork() ) {
		case -1:
			return ERROR_CODE;
		case 0:
            execvp(file_path, argv);
			break;
		default:
			wait(NULL);
			return_val = WEXITSTATUS(wstatus);
	}
			if (return_val == ERROR_CODE) {
				return ERROR_CODE;
			} else {
				return return_val;
			}
}