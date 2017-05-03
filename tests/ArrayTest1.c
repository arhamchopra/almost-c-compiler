int main(){
    int a[5];
    a[3] = 5;
    a[1] = 4;
    a[4] = 100;
    int i = 5;
    i = i - 2;
    PrintInt(a[i-2]);
    
    a[4] = -100;
    PrintInt(a[4]);

    return 0;
}
