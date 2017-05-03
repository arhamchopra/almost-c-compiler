#include <stdio.h>
 
int ackermann(int m, int n)
{
        if (!m) return n + 1;
        if (!n) return ackermann(m - 1, 1);
        return ackermann(m - 1, ackermann(m, n - 1));
}
 
int main()
{
        int m, n;
        ScanInt(&m);
        ScanInt(&n);
        PrintInt(ackermann(m,n));
        return 0;
}
