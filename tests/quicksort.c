#include <stdio.h>
int array[10] ; 

int quicksort(int left , int right) ; 

int partition(int left , int right){
	int idx ; 
	idx = left ; 

	int  i  ; 
	for( i = left + 1 ; i <= right ; i= i+1){
		if(array[idx]  >  array[i]){
			int t ; 
			t = array[i] ; 
			array[i] = array[idx] ; 
			array[idx] = t ;
			t = array[i] ; 
			array[i] = array[idx+1] ; 
			array[idx+1] = t ; 

		}
	}
	return idx ; 
}


int quicksort(int left , int right){
	
	if(left > right)
		return 1 ; 

	int x ; 
	x = partition(left , right) ; 

	quicksort(left , x-1) ; 
	quicksort(x+1 , right) ; 

    return 1;
}

int main(){
	int i, tmp ; 
	for(i=0; i<10 ; i = i+1){
		ScanInt(&tmp) ; 
		array[i] = tmp;
	}
	quicksort(0 , 9) ; 
	for(i=0; i<10 ; i= i+1){
		PrintInt(array[i]) ; 
		PrintSpace();
	}
i=0;
return 1;
}
