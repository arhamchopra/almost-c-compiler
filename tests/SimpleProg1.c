int main(){
    int c,d;
    int first[2][2];
    /* int second[10]; */
    /* ScanInt(&first[c][d]); */

    /* for(c=0;c<10;c++){ */
    /*     ScanInt(&second[c]); */
    /* } */
    /*  */
    /* for(c=0;c<10;c++){ */
    /*     PrintInt(second[c]); */
    /* } */

    for (c = 0; c < 2; c++){
      for (d = 0; d < 2; d++){
          ScanInt(&first[c][d]);
      }
    }
    for (c = 1; c >= 0; c--){
      for (d = 1; d >= 0; d--){
          PrintInt(first[c][d]);
      }
    }
 /*  */
    return 0;

}
