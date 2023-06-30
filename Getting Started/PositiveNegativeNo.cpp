// Check if the no. is positive or negative 

#include<iostream>
using namespace std;

int positiveNegativeNo(int num){
    if(num > 0){
        cout<<"Positive Number."<<endl;
    }
    else if(num < 0){
        cout<<"Negative Number."<<endl;
    }
    else{
        cout<<"Zero.";
    }
    return 0;
}
int main()
{
    int num;
    cout<<"Enter a number: ";
    cin>>num;
    positiveNegativeNo(num);
    return 0;
}