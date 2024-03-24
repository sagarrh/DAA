//this is kashvi's min max problem
#include <stdio.h>
int findmin(int a[],int low,int high){
    while(high>=low){
        if(low==high){
            return a[low];
        }
        else{
            int mid=(high+low)/2;
            int min1=findmin(a,low,mid);
            int min2=findmin(a,mid+1,high);
            int x=(min1>min2)?min2:min1;
            return x;
        }
    }
}
int findmax(int a[],int low,int high){
    while(high>=low){
        if(low==high){
            return a[low];
        }
        else{
            int mid=(high+low)/2;
            int max1=findmax(a,low,mid);
            int max2=findmax(a,mid+1,high);
            int x=(max1>max2)?max1:max2;
            return x;
        }
    }
}
int main() {
  int a[]={22,54,32,87,12};
  int length=sizeof(a)/sizeof(a[0]);
  int min=findmin(a,0,length-1);
  int max=findmax(a,0,length-1);
  printf("Minimum element is %d",min);
  printf("\nMaximum element is %d",max);
}