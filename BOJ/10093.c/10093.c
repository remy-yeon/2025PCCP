#include <stdio.h>  

int main() {
    
    int a,b,max,min,val;
    scanf("%d %d", &a,&b);
    
    if (a>b){
        max = a;
        min = b;
    }
    else{
        max = b;
        min = a;
    }

    val = max - min;
    val = val - 1;
    printf("%d",val);
    
    for(int i = min; i < max; i++){
        printf("%d ", min); 
        min++;
    }
    
    return 0;
}