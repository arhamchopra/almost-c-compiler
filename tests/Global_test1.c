int a_arr = 5;
int b_arr;
int c_arr[20];
int main(){
    int v=5;
    /* c_arr[2] = 22; */
    /* c_arr[v] = c_arr[v-3]; */
    /* PrintInt(c_arr[v]); */
    /* int c = c_arr[v]; */
    /* PrintInt(c_arr[5]); */
    /* PrintInt(c); */
    for(v=0;v<10;v++){
        c_arr[v]=c_arr[v-1]+v*2;
    }

    for(v=0;v<10;v++){
        PrintInt(c_arr[v]);
        PrintSpace();
    }
    return 0;
}
