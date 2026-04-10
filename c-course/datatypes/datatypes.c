#include <stdio.h>

int main() {
	int a = -42;
	unsigned int b = 42;
	float x = 3.14f;
	double y = 2.7123971235;
	char c = 'Z';

	printf("Signed int: %d\n", a);
	printf("UNsigned int: %u\n", b);
	printf("Float: %.2f\n", x);
	printf("Double: %.9f\n", y);
	printf("Char: %c\n", c);

	return 0;
}
