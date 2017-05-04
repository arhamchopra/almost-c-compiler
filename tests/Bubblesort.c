int main()
{
  int array[10], n =10;
  int c, d, swap;
 
  for (c = 0; c < n; c++)
    ScanInt(&array[c]);
 
  for (c = 0 ; c < ( n - 1 ); c++)
  {
    for (d = 0 ; d < n - c - 1; d++)
    {
      int k1 = array[d];
      int k2 = array[d+1];
      if (array[d] > array[d+1]) /* For decreasing order use < */
      {
        swap       = array[d];
        array[d]   = array[d+1];
        array[d+1] = swap;
      }
    }
  }
  
  for ( c = 0 ; c < n ; c++ ){
     PrintInt(array[c]);
     PrintSpace();
 }
  return 0;
}
