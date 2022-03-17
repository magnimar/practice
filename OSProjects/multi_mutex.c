#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <alloca.h>
#include <stdio.h>
#include <pthread.h>

#include "multi_mutex.h"

pthread_mutex_t lock;

//pthread_mutex_init(&lock, NULL);


int multi_mutex_unlock(pthread_mutex_t **mutexv, int mutexc)
{
    for (int i=mutexc; i>0; i--) {
        int try = pthread_mutex_unlock(mutexv[i-1]);
        if (try != 0) {
            return -1;
        }
    }
    return 0;
}

int multi_mutex_trylock(pthread_mutex_t **mutexv, int mutexc)
{
    for (int i=0; i<mutexc; i++) 
    {
        int try = pthread_mutex_trylock(mutexv[i]);
        if (try != 0)
        {
            for (int n=0; n<i; n++) 
            {
                pthread_mutex_unlock(mutexv[n]);
            }
            return -1;
        }
    }
    return 0;
}

// ====== TEST 2: You abort locking and unlock all locked mutexs when a mutex cannot be locked in your multi_mutex_trylock. =====
//Testing multi_mutex.c with test2.c
//Starting to test multi_mutex.c...
///home/sty22/A8p2/.tests/test2.c line 30: pthread_mutex_unlock(&m[i]) => Expected 1, but got 0
//You have errors in your solution, please fix them.
//x:error
//TEST FAILED