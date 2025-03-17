#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(){
    char secret[16];
    char buf[16];

    secret[0] = 'l';
    secret[1] = 'e';
    secret[2] = 'a';
    secret[3] = 'k';
    
    int archivo = open ("./input", O_RDONLY);
    read(archivo, buf, 16);
    puts(buf);
    return 0;
}
