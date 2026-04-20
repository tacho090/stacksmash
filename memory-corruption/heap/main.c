#include <stdio.h>
#include <stdlib.h>

#define BUFF_SIZE 1024
#define SAFEFREE(x) free(x); x = NULL;

struct Square {
  char *name;
  int (*add)(int, int);
}

int main() {
  struct Square *buff = malloc(sizeof(struct Square));
  if (buff == NULL) {
    return 0;
  }
  SAFEFREE(buff);
}
