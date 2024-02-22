#include <stdio.h>
#include <stdlib.h>

int main(void){
    FILE *file = fopen("../data/24.txt", "r");
    fseek(file, 0, SEEK_END);
    long size = ftell(file);
    fseek(file, 0, SEEK_SET);
    char *data = malloc(size+1);
    fread(data, size, 1, file);
    long counter = 0;
    long mxcount = 0;
    long prevstartpos = 0;
    for(long i=0; i<size; i++){
        if
    }
    return 0;
}
