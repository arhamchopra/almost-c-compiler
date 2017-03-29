int f1(int a, int b){
	return a+b;
}

int f2(int a){
	f1(1,a);
	return a;
}
