/* #include <stdio.h> */
 
int main()
{
  int size = 5;
  int c, d, k;
  int sum = 0;
  int first[5][5];
  int second[5][5];
  int multiply[5][5];
 
  for (c = 0; c < size; c++){
    for (d = 0; d < size; d++){
        ScanInt(&first[c][d]);
    }
  }
 
 
    for (c = 0; c < size; c++){
    for (d = 0; d < size; d++){
        ScanInt(&second[c][d]);
    }
    }

  for (c = 0; c < size; c++) {
      for (d = 0; d < size; d++) {
        for (k = 0; k < size; k++) {
          sum = sum + first[c][k]*second[k][d];
        }
 
        multiply[c][d] = sum;
        sum = 0;
      }
    }
    PrintNewline();
 
    for (c = 0; c < size; c++) {
      for (d = 0; d < size; d++){
        PrintInt(multiply[c][d]);
        PrintSpace();
      }
      PrintNewline();
    }
  return 0;
}
