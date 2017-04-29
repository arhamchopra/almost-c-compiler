struct point{
    int Name;
    int Age;
    char Gender;
};

int main(){
    struct point a;
    a.Name = 5;
    a.Age = a.Name + 10;

    return 0;
}
