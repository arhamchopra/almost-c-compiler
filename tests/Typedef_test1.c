#include <stdio.h>
typedef char TT;
int a = 5;
char func(int a, int a){
    return a;
}

TT b = 'z';

void main(){
    printf("%c %c", func('a'), 'z');
}
