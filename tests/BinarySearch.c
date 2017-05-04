#include <stdio.h>

int a[10];
 
/* int bsearch (int n, int x) { */
/*     int i = 0, j = n - 1; */
/*     while (i <= j) { */
/*         int k = (i + j) / 2; */
/*         if (a[k] == x) { */
/*             return k; */
/*         } */
/*         else if (a[k] < x) { */
/*             i = k + 1; */
/*         } */
/*         else { */
/*             j = k - 1; */
/*         } */
/*     } */
/*     return -1; */
/* } */
/*   */
int bsearch_r (int x,int i, int j) {
    if (j < i) {
        return -1;
    }
    int k = (i + j) / 2;
    if (a[k] == x) {
        return k;
    }
    else if (a[k] < x) {
        return bsearch_r(x, k + 1, j);
    }
    else {
        return bsearch_r(x, i, k - 1);
    }
}
 
int main () {
    int i;
    int b[10];
    for(i=0;i<10;i++){
        ScanInt(&b[i]);
    }
    for(i=0;i<10;i++){
        a[i] = b[i];
    }
    int c = bsearch_r(5, 0, 10);
    PrintInt(c);

    return 0;
}
