#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
int main(){
    size_t start = 1100000000, end = 1987653210;
    size_t *arr = malloc(0xffffffff);
    size_t count = 0;

    for(size_t i=start; i<end; i++){
        size_t last_num = i<<((((i&2)>>1)+1))|(i&3);
        i++;
        size_t num = i<<((((i&2)>>1)+1))|(i&3);
        i--;
        printf("%zd\n", num-last_num);
        /* arr[num]++; */
    }
}
