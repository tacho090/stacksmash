#include <stdio.h>
#include <stdio.h>

#define SQUARE_NAME_SIZE 32

#define SAFEFREE(x) free(x); x = NULL;

struct Square {
  char name[SQUARE_NAME_SIZE];
  int size;
  int (*get_perimeter)(void*);
};

int perimeter(struct Square *sq) {
  return sq->size*4;
}

void debug() {
  puts("You win!\n");
}

int main() {
  struct Square *sq = malloc(sizeof(struct Square));
  if(sq == NULL) {
    return 0;
  }

  sq->get_perimeter = perimeter;

  printf("What is the name of your square?\n");
  int n = read(0, sq->name, 0x32);
  if(sq->name[n-1] == 0xa) {
    sq->name[n-1] == 0x0;
  }

  printf("What is the square size?\n");
  scanf("%d", &sq->size);

  printf("Sup, %s\n", sq->name);
  printf("Your perimeter is %d.\n", sq->get_perimeter(sq));

  SAFEFREE(sq);
}
