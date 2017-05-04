/* #include <stdio.h> */
 
int ackermann(int m, int n)
{
        if (!m) return n + 1;
        if (!n) return ackermann(m - 1, 1);
        return ackermann(m - 1, ackermann(m, n - 1));
}
 
int main()
{
        int am, an;
        ScanInt(&am);
        ScanInt(&an);
        PrintInt(ackermann(am,an));
        return 0;
}
