#include "scheduler.h"
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>

struct QueueItem {
    int data;
    struct QueueItem *next;
};

struct Queue {
    struct QueueItem *head;
    struct QueueItem *tail;
};

typedef enum _ThreadState {
    STATE_UNUSED = 0, // This entry in the _threads array is unused.

    STATE_READY,      // The thread is ready and should be on a ready queue for
                      //   selection by the scheduler
    STATE_RUNNING,    // The thread is running and should not be on a ready queue
    STATE_WAITING     // The thread is blocked and should not be on a ready queue
} ThreadState;

typedef struct _Thread {
    int threadId;
    ThreadState state;
    /*
     * Range: 0 ... HIGHEST_PRIORITY (including)
     * HIGHEST_PRIORITY is highest priority
     */
    int priority;
} Thread;

typedef struct _Starvation {    //used to count nr of priorities invoked in the past
    int priority;
    int counter;
} Starvation;

Thread _threads[MAX_THREADS] = {{0}};

/* TODO: Add global variables if needed. */

struct Queue runQueue;

struct Queue*ptr[HIGHEST_PRIORITY];   //array of runQueues indexed by priority

Starvation starvation;                //struct to keep track of priorities ran to prevent starvation

/*
 * Adds a new, waiting thread.
 */
int startThread(int threadId, int priority)
{
    if (((threadId < 0) || (threadId >= MAX_THREADS) ||
        (_threads[threadId].state != STATE_UNUSED)) ||
        (priority < 0) || (priority > HIGHEST_PRIORITY)) {

        return -1;
    }

    _threads[threadId].threadId = threadId;
    _threads[threadId].state    = STATE_WAITING;
    _threads[threadId].priority = priority;
    return 0;
}

/*
 * Append to the tail of the queue.
 * Does nothing on error.
 */
void _enqueue(struct Queue *queue, int newData)
{

    struct QueueItem *newItem = (struct QueueItem *)malloc(sizeof(struct QueueItem*));

    newItem->data = newData;
    newItem->next = NULL;

    if (queue->head== NULL) {                      //emptu list
        queue->head = newItem;
        queue->tail = newItem;
    } else if ( (queue->head==queue->tail) ) {    //list with 1 item
        queue->head->next = newItem;
        queue->tail = newItem;
    } else {                                      //list with many items
        queue->tail->next = newItem;
        queue->tail = newItem;
    }
}

/*
 * Remove and get the head of the queue.
 * Return -1 if the queue is empty.
 */
int _dequeue(struct Queue *queue)
{
    (void)queue;

    // TODO: Implementurn

    struct QueueItem *tmp = queue->head;        //current head, used to free later
    int returnValue = queue->head->data;        //current value of head, used for return

    if (queue->head==NULL) {                    //empty list
        return -1;
    } else if (queue->head==queue->tail) {      //one item in list
        queue->head = NULL;
        queue->tail = NULL;
        free(tmp);                              //free memory
        return returnValue;
    } else {                                    //many items in list
        queue->head = queue->head->next;
        free(tmp);                              //free memory
        return returnValue;
    }
    return -1;                                  //-1 on error
}

void initScheduler()
{
    // TODO: Implement if you need to initialize any global variables you added

    for (int i=0; i<HIGHEST_PRIORITY+1; i++){    //malloc for queue struct in each priority
        ptr[i] = malloc(sizeof(struct Queue));
    }

    starvation.priority=-430;                    //set starting priority outside of real range as not to confuse with real priorities
    starvation.counter=0;                        //initialise counter

}

/*
change a thread from waiting state to ready state
 */
void onThreadReady(int threadId)
{
    (void)threadId;

    // TODO: Implement

    _threads[threadId].state    = STATE_READY;                //update state of thread
    _enqueue(ptr[_threads[threadId].priority], threadId);     //append thread to appropiate queue

}

/*
enqueue thread again to priority queue
 */
void onThreadPreempted(int threadId)
{
    (void)threadId;

//    // TODO: Implement

    _threads[threadId].state = STATE_READY;                  //update state of thread
    _enqueue(ptr[_threads[threadId].priority], threadId);    //append thread to appropiate queue
    
}

//change thread from running to waiting
void onThreadWaiting(int threadId)
{
    (void)threadId;

    _threads[threadId].state = STATE_WAITING;    //update thread status
    
}

/*
dequeue first thread at max priority, has in built starvation prevention if thread has been invoked more thatn 5 times
 */
int scheduleNextThread()
{

    int i = HIGHEST_PRIORITY; 
    int id=-1;                                        //return value
    while (1) {                                       //while loop that always returns

        if (i==0 && ptr[i]->head==NULL) {            //base case, if last priority is empty
            return -1;                               
        }
        
        if (ptr[i]->head != NULL) {                  //checks if priority queue is not empty

            if (starvation.counter<5) {              //if thread has been invoked less than 5 times in a row
            
                if (starvation.priority==i) {        //if same thread as ran before then increment counter
                    starvation.counter++;
                } else {                             //if diff thread than before then set counter and priority
                    starvation.counter = 1;
                    starvation.priority = i;
                }

                id = _dequeue(ptr[i]);              //if conditions have been met the thread is dequeued and state is changed, funtion is finished
                _threads[id].state = STATE_RUNNING;
                return id;
            
            } else if (i != starvation.priority) {  //if current priority was not the last priority
             
                starvation.counter = 1;             //starvation variables set
                starvation.priority = i;
                id = _dequeue(ptr[i]);              //thread dequeued, state changed and returned
                _threads[id].state = STATE_RUNNING;
                return id;
            
            } else {
                i--;
            }
            } else {
                i--;
            }
        }
}