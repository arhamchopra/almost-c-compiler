int main(){
    int a = 5;
    a = a++;
    int * b = &a;
    int c = *b;
    return 0;
}
