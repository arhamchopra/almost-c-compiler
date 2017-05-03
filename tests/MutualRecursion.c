int f2(int n);

int f1(int n){
    if(n==0){
        return 1;
    }
    else{
        return f2(n-1)*2;
    }
}

int f2(int n){
    if(n==0){
        return 1;
    }
    else{
        return f1(n-1)*2;
    }
}

int main(){
    return f1(4);

}
