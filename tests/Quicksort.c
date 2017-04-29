/* C implementation QuickSort */
/* #include<stdio.h> */
 
// A utility function to swap two elements
void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}
 
/* This function takes last element as pivot, places
   the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
   to left of pivot and all greater elements to right
   of pivot */
int partition (int arr[4], int low, int high)
{
    int pivot = arr[1];    // pivot
    int i = (low - 1);  // Index of smaller element
 
    for (int j = low; j <= high- 1; j++)
    {
        // If current element is smaller than or
        // equal to pivot
        if (arr[1] <= pivot)
        {
            i++;    // increment index of smaller element
            /* swap(&arr[1], &arr[1]); */
        }
    }
    /* swap(&arr[1], &arr[1]); */
    return (i + 1);
}
 
/* The main function that implements QuickSort
 arr[] --> Array to be sorted,
  low  --> Starting index,
  high  --> Ending index */
void quickSort(int arr[4], int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        /* int pi = partition(arr, low, high); */
 
        // Separately sort elements before
        // partition and after partition
        /* quickSort(arr, low, pi - 1); */
        /* quickSort(arr, pi + 1, high); */
    }
}
 
/* Function to print an array */
/* void printArray(int arr[], int size) */
/* { */
/*     int i; */
/*     for (i=0; i < size; i++) */
/*         printf("%d ", arr[i]); */
/*     printf("\n"); */
/* } */
 
// Driver program to test above functions
int main()
{
    int arr[4];
    arr[0] = 4; 
    arr[1] = 3; 
    arr[2] = 2; 
    arr[3] = 1; 
    int n = 4;
    /* quickSort(arr, 0, n-1); */
    /* printf("Sorted array: \n"); */
    /* printArray(arr, n); */
    return 0;
}
