#include <stdio.h>
int fibb(int n) {
    int fnow = 0, fnext = 1, tempf;
    while(n-1>0){
            n=n-1;
            tempf = fnow + fnext;
            fnow = fnext;
            fnext = tempf;
            }
        return fnext;   
}

int main(){
    int a=20;
    ScanInt(&a);
    PrintInt(fibb(a));
    return 0;

}
