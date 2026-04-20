#include <stdio.h>

int initialized = 42;    // .data
int uninitialized;       // .bss

int main() {
    static int local_static = 7;  // .data
    static int temp;              // .bss
    printf("initialized: %d\n", initialized);
    printf("uninitialized: %d\n", uninitialized);
    return 0;
}
