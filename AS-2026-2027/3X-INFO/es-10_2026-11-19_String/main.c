#include <stdio.h>
#include <string.h>

#define MAX_LEN 20

int strlength(const char*);

int main(int argc, char* argv[]) {
	char firstname[MAX_LEN];
	printf("Hello, please enter the first name: ");
	scanf("%19[^\n]", firstname);
	printf("You entered '%s' [%d characters]\n", firstname, strlength(firstname));

	char name0[MAX_LEN];
	char name1[MAX_LEN];

	strcpy(name0, firstname);
	strcpy(name1, name0);
	strcat(name0, "lisa");
	strcat(name1, "rita");
	char* substring = "it";
	printf(
		"\n* name0: '%s' (len: %d)\n* name1: '%s' (len: %d)\n* String comparison result: %d\n* The substring '%s' is%s present in '%s'..",
		name0, strlen(name0),
		name1, strlen(name1),
		strcmp(name0, name1),
		substring, strstr(name1, "it") == NULL ? " not" : "", name1
	);
	return 0;
}

int strlength(const char* str) {
	int len;
	for(len = 0; str[len] != '\0'; len++);
	return len;
}
