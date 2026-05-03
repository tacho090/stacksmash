#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define ANIMAL_NAME_SIZE 64

void debug() {
        printf("You win!\n");
}

struct cat {
  char name[ANIMAL_NAME_SIZE];
  void (*speak)(char*);
};

struct dog {
  void (*speak)(char*);
  char name[ANIMAL_NAME_SIZE];
};

struct cat *cat;
struct dog *dog;

void cat_speak(char *name) {
        printf("Meow, says %s\n", name);
}

void dog_speak(char *name) {
        printf("Woof, says %s\n", name);
}

void printHelp() {
        printf("options:\n\tnewdog\n\tnewcat\n\tdeletedog\n\tdeletecat\n\tprintdog\n\tprintcat\n");
}

int main() {
        char buff[32];

        while (buff[0] != 'q') {
                printf("> ");
                scanf("%32s", buff);

        if (!strcmp(buff, "newdog")) {
                dog = malloc(sizeof(struct dog));
                if (!dog) {
                        return 0;
                }

                printf("Got dog at %p\nName?\n", dog);
                scanf("%63s", dog->name);
                if (!dog->speak)
                        dog->speak = dog_speak;

        } else if (!strcmp(buff, "newcat")) {
                cat = malloc(sizeof(struct cat));
                if (!cat) {
                        return 0;
                }

                printf("Got cat at %p\nName?\n", cat);

                char *name = malloc(0x1024);
                scanf("%63s", cat->name);
                if (!cat->speak)
                        cat->speak = cat_speak;

        } else if (!strcmp(buff, "deletedog")) {
                free(dog);
        } else if (!strcmp(buff, "deletecat")) {
                free(cat);
        } else if (!strcmp(buff, "speakdog")) {
                dog->speak(dog->name);
        } else if (!strcmp(buff, "speakcat")) {
                cat->speak(cat->name);
        } else if (!strcmp(buff, "printdog")) {
                printf("%s\n", dog->name);
        } else if (!strcmp(buff, "printcat")) {
                printf("%s\n", cat->name);
        } else {
                printHelp();
        }
  }
}
