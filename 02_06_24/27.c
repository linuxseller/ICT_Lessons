#include <stdio.h>
#include <stdlib.h>
int main(){
    FILE *file = fopen("27B.txt", "r");
    long long int n, kmx=0, mx=-11111111111;
    fscanf(file, "%lld", &n);
    printf("%lld\n", n);
    long long int *data = malloc(sizeof(long long int)*n);
    long long int *datathatfits = malloc(sizeof(long long int)*n);
    long long int datafits_n = 0;
    for(long long int i=0; i<n; i++){
        fscanf(file, "%lld", (data+i));
    }
    for(long long int k=n; k>0; k--){
        long long sm=0, pos=0, flag=1;
        while(flag){
            sm += data[pos];
            pos = (pos + k) % n;
            flag = (pos==0)?0:1;
        }
        if(sm>=mx){
            kmx = k;
            mx = sm;
        }
    }
    printf("%lld %lld\n", mx, kmx);
}
