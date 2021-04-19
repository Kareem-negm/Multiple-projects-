/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int factorial(int n)
{
    int fact = 1;
    for (int i=2; i<=n; i++)
       fact *= i;
    return fact;
}
 
 float sum(int n)
{
    float sum = 0;
    for (int i = 1; i <= n; i++)
        (i%2==0)?sum-=1.0/factorial(i):sum+=1.0/factorial(i);
    return sum;
}
 
int main()
{
    int n=6;
    cout<<sum(n);
   
    return 0;
}
