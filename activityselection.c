#include <stdio.h>
struct activity
{
    int start;
    int finish;
};

void swap(struct activity *a, struct activity *b) {
    struct activity temp = *a;
    *a = *b;
    *b = temp;
}

int activityselection(struct activity arr[],int n){
    //sorting it out
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            if(arr[j].finish>arr[j+1].finish)
            {
                swap(&arr[j],&arr[j+1]);
            }
        }
    }
    //printing one by one and adding to the selection 
    printf("activity : %d, %d",arr[0].start,arr[0].finish);
    int selected =1;
    int j=0;
    for(int i=1;i<n;i++)
    {
        if(arr[i].start>arr[j].finish)
        {
             printf("activity : %d, %d",arr[i].start,arr[i].finish);
            selected++;
            j=i;
        }
    }
    return selected;

    
}
int main() {
    struct activity arr[6] = {
        {5, 9},
        {1, 2},
        {3, 4},
        {0, 6},
        {5, 7},
        {8, 9}
    };

    int n = sizeof(arr) / sizeof(arr[0]);
    int nums = activityselection(arr, n);
    printf("max number of activity are %d", nums);
    return 0;
}