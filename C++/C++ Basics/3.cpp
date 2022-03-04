#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function
    int ab = *a + *b;
    int ba = *a - *b? *a > *b: *b-*a;
    a = &ab;
    b = &ba;    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}