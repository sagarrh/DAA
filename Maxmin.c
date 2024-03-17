#include <stdio.h>
#include<stdlib.h>
int* maxminn(int *a,int b,int n);
int main()
{
    int n;
    printf("Enter size of array");
    scanf("%d",&n);
    int a[n],i=0;
    printf("enter %d numbers",n);
    while(i<n)
        scanf("%d",&a[i++]);
    int *maxmin=maxminn(a,0,n-1);
    printf("MAX:%d",maxmin[0]);
    printf("MIN:%d",maxmin[1]);
    free(maxmin);
    return 0;

}
int *maxminn(int *a,int low,int high)
{
    int *returnthis = malloc(sizeof(int)*2);
    int mid;
    if(low<high-1)
    {
        mid=(low+high)/2;
        int *left=maxminn(a,low,mid);
        int *right=maxminn(a,mid+1,high);
        returnthis[0] = (left[0] > right[0]) ? left[0] : right[0];
        returnthis[1] = (left[1] < right[1]) ? left[1] : right[1];
    }
    else if(low==high-1)
    {
        returnthis[0]=(a[low]>a[high])?a[low]:a[high];
        returnthis[1]=(a[low]<a[high])?a[low]:a[high];

    }
    else{
        returnthis[0]=returnthis[1]=a[high];

    }
    return returnthis;

}