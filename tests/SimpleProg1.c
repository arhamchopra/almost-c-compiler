int fg(int n){
    PrintInt(n);
    return 0;
}

int fn(int n){
    if (n==0){
        return 1;
    }
    PrintInt(n);
    fg(n);
    fn(n-1);
    fn(n-1);

    return 0;
}



int main(){
    fn(3);
    return 0;

}
