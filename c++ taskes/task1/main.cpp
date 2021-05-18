/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
   float sum_row;
   float sum_colum;
   float sum;
   float sum_dia=0;
    int row=2,colums=3;
    float arr[row][colums];

    //for row
    for(int i=0;i<row;i++){
        //for colums
        for(int c=0;c<colums;c++){
            cin >> arr[i][c];
        }
        
    }
   // finding the row&columans sum
    for (int r = 0; r <row ; ++r) {
        for (int j = 0; j < colums; ++j) {
 
            // Add the element
            sum_row = sum_row + arr[r][j];
            sum_colum = sum_colum + arr[j][r];
            if(j=r){
                sum_dia=+ arr[r][j];
            }
        }    }

   sum=sum_row+sum_colum;
   cout<<"the sum the element of the matrix="<<sum<<endl;
   cou<<"the sum of diago="<<sum_dia<<endl;
   
   
    return 0;
}
