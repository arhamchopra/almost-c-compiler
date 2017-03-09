#include <stdio.h>
typedef char TT;

char func(TT a){
    return a;
}

TT b = 'z';

void main(){
    printf("%c %c", func('a'), 'z');
}
