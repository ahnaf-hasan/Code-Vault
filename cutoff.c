#include <stdio.h>

int main() {
    int num;
    float decimal, cutoff;

    while (scanf("%d.%f", &num, &decimal) == 2) {
        scanf("%f", &cutoff);

        if (decimal > cutoff)
            printf("%d\n", num + 1);
        else
            printf("%d\n", num);
    }

    return 0;
}