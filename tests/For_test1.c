int add( int a){
    return a;
}
int main(){
    int a;
    for(a=0;a<10;a++){
        int b = 12;
        if (a<7){
            b = 3;
            break;
        }
        else{
            b = 99;
            continue;
        }
        int g = 4;
        continue;
    }
    add(a);
}
