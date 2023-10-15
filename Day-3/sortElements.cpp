#include <iostream>
using namespace std;
// void takeElements(int size, int arr[])
// {
  
//     for(int i=0;i<size;i++)
//     {
//         cin>>arr[i]<<" ";
//     }
// }
// void printElements(int arr[],int size)
// {
//       for(int i=0;i<size;i++)
//     {
//         cout<<arr[i]<<" ";
//     }

// }
int main()
{

int score[100];
int size;
cout<<"Enter the score of student"<<endl;
cin>>size;
for(int i=0;i<size;i++)
{
    cin>>score[i];
}

cout<<" Score of Students: ";

for(int i=0;i<size;i++)
{
    cout<<score[i] <<" ";
}

for(int i=0;i<size;i++)
// {
//     if(score[i]> score[i+1])
//     {
//         swap(score[i],score[i+1]);
//     }
    
//     cout<<score[i];
// }


return 0;
}