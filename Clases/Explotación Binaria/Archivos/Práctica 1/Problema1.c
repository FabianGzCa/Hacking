#include <stdio.h>

void win() {
    puts("Ganaste, toma 5 pesos");
}

void func1() {
    char buf[30];
    scanf("%s", buf);
}

int main() {
    func1();
    puts("Ya acabe");
    return 0;
}
