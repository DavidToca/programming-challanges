/*************************************************************************
 * Copyright (C) 2008 by liukaipeng                                      *
 * liukaipeng at gmail dot com                                           *
 *************************************************************************/
/* @JUDGE_ID 00000 100 C "The 3n+1 problem" */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#define MAX 1000000
/*************************************************************************
 * Queue (FIFO)                                                          *
 * Note: No error check is performed.                                    *
 *************************************************************************/
#define QUEUESIZE MAX
typedef size_t valuetype;
typedef struct queue {
  valuetype data[QUEUESIZE];
  int head;
  int tail;
  int size;
} queue;
void initqueue(queue *q) {
  q->head = 0;
  q->tail = 0;
  q->size = 0;
}
int emptyqueue(queue *q) {
  return q->size == 0;
}
void enqueue(queue *q, valuetype v) {
  q->data[q->tail++] = v;
  q->tail %= QUEUESIZE;
  q->size += 1;
}
valuetype dequeue(queue *q) {
  valuetype v = q->data[q->head++];
  q->head %= QUEUESIZE;
  q->size -= 1;
  return v;
}
/*************************************************************************/
int len[MAX] = {0};
queue q;
void fill()
{
  initqueue(&q);
  len[1] = 1;
  enqueue(&q, 1);
  for (; !emptyqueue(&q); ) {
    int cur = dequeue(&q);
    int pre;
    /* find the previous elements in the cycle */
    if (cur*2 < MAX) {
      pre = cur*2;
      len[pre] = len[cur] + 1;
      enqueue(&q, pre);
    }
    if (cur % 3 == 1 && (cur-1)/3 % 2 == 1 && (cur-1)/3 != 1) {
      pre = (cur-1)/3;
      len[pre] = len[cur] + 1;
      enqueue(&q, pre);
    }
  }
  {
    int i;
    for (i = 3; i < MAX; ++i) {
      if (len[i] == 0) {
        unsigned int j;
        int d;
        for (j = i, d = 0; j >= MAX || len[j] == 0; ++d) {
          if (j % 2 == 0)
            j = j/2;
          else
            j = 3*j+1;
        }
        len[i] = len[j] + d;
      }
    }
  }  
}
int main(int argc, char *argv[])
{
#ifndef ONLINE_JUDGE
  char in[256];
  char out[256];
  strcpy(in, argv[0]);
  strcat(in, ".in");
  freopen(in, "r", stdin);
  strcpy(out, argv[0]);
  strcat(out, ".out");
  freopen(out, "w", stdout);
#endif
  int i, j;
  fill();
  while (scanf("%d %d", &i, &j) != EOF) {
    int max = 0;
    printf("%d %d ", i, j);
    if (i > j) {
      i ^= j;
      j ^= i;
      i ^= j;
    }
    for (; i <= j; ++i)
      if (len[i] > max) 
        max = len[i];
    printf("%d\n", max);
  }
  return 0;
}
