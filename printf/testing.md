# Testing Your Printf

> **Important**

To ensure that your printf functions in the same manner as the system's printf, here are some methods to test it. This test examines how printf handles characters and strings.

> **Note**

Create a file and copy the following code for testing your printf with:

```
#include <limits.h>
#include <stdio.h>
#include "main.h"
#define ZERO 0

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
    int len;
    int len2;

    len = _printf("Let's try to printf a simple sentence.\n");
    len2 = printf("Let's try to printf a simple sentence.\n");

    _printf("empty Character:[%c]\n", ' ');
    printf("empty Character:[%c]\n", ' ');
    _printf("Character:[%c]\n", 'H');
    printf("Character:[%c]\n", 'H');
    _printf("Character:[%c%c]\n", 'H', 'I');
    printf("Character:[%c%c]\n", 'H', 'I');
    _printf("Character:[%c%c%c]\n", 'H', 'I', '!');
    printf("Character:[%c%c%c]\n", 'H', 'I', '!');

    _printf("Character:[%c %c %c]\n", 'H', 'I', '!');
    printf("Character:[%c %c %c]\n", 'H', 'I', '!');
    _printf("Two c with Space:[%c %c]\n", 'H', 'I');
    printf("Two c with Space:[%c %c]\n", 'H', 'I');
    _printf("empty String:[%s]\n", "");
    printf("empty String:[%s]\n", "");
    _printf("Space String:[%s]\n", " ");
    printf("Space String:[%s]\n", " ");
    _printf("String:[%s]\n", "I am a string !");
    printf("String:[%s]\n", "I am a string !");
    _printf("String:[%s%s]\n", "I am a string !", "second string !");

   _printf("String:[%s%s]\n", "I am a string !", "second string !");
    printf("String:[%s %s]\n", "I am a string !", "second string !");

    return (0)
}
```

## Testing Your Printf Numbers

```
#include <limits.h>
#include <stdio.h>
#include "main.h"

int main(void)
{
	int len = 0;
	int len2 = 0;

    len = printf("String:[%s%s]\n", "I am a string !", "second string !");
    len2 = _printf("String:[%s%s]\n", "I am a string !", "second string !");
    printf("Length:[%d, %i]\n", len, len2);

	len = _printf("Number: %d, %i\n", 4034, 4034);
	len2 = printf("Number: %d, %i\n", 4034, 4034);
	printf("Len:[%d]\n", len);
	printf("Lelen:[%d]\n\n", len2);

	len = _printf("Negative: %i, %d\n", -4034, -4034);
	len2 = printf("Negative: %i, %d\n", -4034, -4034);
	printf("Len:[%d]\n", len);
	printf("Lelen:[%d]\n\n", len2);

	len = _printf("NULL: %i\n", NULL);
	len2 = printf("NULL: %i\nlenlen", NULL);
	printf("Len:[%d]\n", len);
	printf("Lelen:[%d]\n\n", len2);

	len = _printf("%d\n", INT_MAX);
	len2 = printf("%d\n", INT_MAX);
	printf("Len:[%d]\n", len);
	printf("Lelen:[%d]\n\n", len2);

	len = _printf("%d\n", INT_MIN);
	len2 = printf("%d\n", INT_MIN);
	printf("Len:[%d]\n", len);
	printf("Lelen:[%d]\n\n", len2);

    len = _printf("\nNumber: [%d], [%i]\n", 4034, 4034);
    len2 = printf("Number: [%d], [%i]\n", 4034, 4034);
    printf("Len:[%d]\n", len);
    printf("Lelen:[%d]\n\n", len2);

    len = _printf("Negative: [%i], [%d]\n", -4034, -4034);
    len2 = printf("Negative: [%i], [%d]\n", -4034, -4034);
    printf("Len:[%d]\n", len);
    printf("Lelen:[%d]\n\n", len2);

    len = _printf("long: [%i], [%d]\n", 4545439394949595, 4545439394949595);
    len2 = printf("long: [%i], [%d]\n", 4545439394949595, 4545439394949595);
    printf("Len:[%d]\n", len);
    printf("Lelen:[%d]\n\n", len2);

    len = _printf("Greater than int: [%i], [%d]\n", 454543939494, 454543939494);
    len2 = printf("Greater than int: [%i], [%d]\n", 454543939494, 454543939494);
    printf("Len:[%d]\n", len);
    printf("Lelen:[%d]\n\n", len2);

    len = _printf("N-Greater than int: [%i], [%d]\n", -454543939494, -454543939494);
    len2 = printf("N-Greater than int: [%i], [%d]\n", -454543939494, -454543939494);
    printf("Len:[%d]\n", len);
    printf("Lelen:[%d]\n\n", len2);

    len = _printf("long: [%i], [%d]\n", -4545439394949595, -4545439394949595);
    len2 = printf("long: [%i], [%d]\n", -4545439394949595, -4545439394949595);
    printf("Len:[%d]\n", len);

    printf("Lelen:[%d]\n\n", len2);

    len = _printf("NULL: [%i]\n", NULL);
    len2 = printf("NULL: [%i]\n", NULL);
    printf("Len:[%d]\n", len);
    printf("Lelen:[%d]\n\n", len2);

    len = _printf("Zero: [%i]\n", ZERO);
    len2 = printf("Zero: [%i]\n", ZERO);
    printf("Len:[%d]\n", len);
    printf("Lelen:[%d]\n\n", len2);

    len = _printf("[%d]\n", INT_MAX);
    len2 = printf("[%d]\n", INT_MAX);
    printf("Len:[%d]\n", len);
    printf("Lelen:[%d]\n\n", len2);

    len = _printf("[%d]\n", INT_MIN);
    len2 = printf("[%d]\n", INT_MIN);
    printf("Len:[%d]\n", len);
    printf("Lelen:[%d]\n\n", len2);

    _printf(NULL);
    printf(NULL);

	return (0);
}
```
