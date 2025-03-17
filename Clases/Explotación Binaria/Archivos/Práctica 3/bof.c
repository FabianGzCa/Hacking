#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

void vuln() {
    char buf[16];
    int archivo = open("./input", O_RDONLY);

    read(archivo, buf, 666);
}

int main(){
    char buf[16] = "Esto no es.";
    char secret[16] = "flag{congrats}";
    
    vuln();
    puts(buf);

    
    return 0;
}
