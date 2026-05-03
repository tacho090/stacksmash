#include <stdio.h>

#define BUFF_SIZE 1024

int add(int a, int b) {
  int result = a + b;
  return result;
}

int main() {
  char buffer[BUFF_SIZE];
  int x = 1, y = 2;

  int sum = add(2, 3);
  return 0;
}
