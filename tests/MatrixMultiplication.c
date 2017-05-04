/* #include <stdio.h> */
 
int main()
{
  int size = 2;
  int c, d, k;
  int sum = 0;
  int first[2][2];
  int second[2][2];
  int multiply[2][2];
 
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
