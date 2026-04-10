#include <stdio.h>
#include <string.h>

int main() {
    FILE *fp;

    // Create and write to a file
    fp = fopen("test.txt", "w");
    if (!fp) {
        perror("Failed to open file");
        return 1;
    }
    fprintf(fp, "Hello, Stack Smash!\n");
    fclose(fp);

    // Read the file
    char buffer[64];
    fp = fopen("test.txt", "r");
    if (!fp) {
        perror("Failed to read file");
        return 1;
    }
    fgets(buffer, sizeof(buffer), fp);
    fclose(fp);

    printf("File contents: %s", buffer);

    // Append to the file
    fp = fopen("test.txt", "a");
    if (fp) {
        fprintf(fp, "Appending some data.\n");
        fclose(fp);
    }

    // Read again
    fp = fopen("test.txt", "r");
    if (fp) {
        printf("\nFull contents:\n");
        while (fgets(buffer, sizeof(buffer), fp)) {
            printf("%s", buffer);
        }
        fclose(fp);
    }

    // Delete the file
    if (remove("test.txt") == 0) {
        printf("\nFile deleted.\n");
    } else {
        perror("Failed to delete file");
    }

    return 0;
}
