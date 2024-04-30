#include<stdio.h>
int weight[3][2]={{24,18},{25,15},{15,20}};
void knapsack(int weight[][2],int total)
{
    float solution[3];
    for(int i=0;i<3;i++)
    solution[i]=0;
    int cumulative=0;
    for(int i=0;i<3;i++)
    {
        if(cumulative+weight[i][1]<=total)
        {
            solution[i]=1.0;
        cumulative=weight[i][1]+cumulative;
        }
        else
        {
            solution[i]=(float)(total-cumulative)/weight[i][1];
            cumulative=total;
            break;
        }
    }
    for(int i=0;i<3;i++)
    printf("%f",solution[i]);
    float profit=0;
    for(int i=0;i<3;i++)
    {
        profit=profit+solution[i]*weight[i][0];

    }
    printf("total profit is %f",profit);


}
int main()
{
    float pw[3];
    for(int i=0;i<sizeof(weight)/sizeof(weight[0]);i++)
    {
        pw[i]=(float)weight[i][0]/weight[i][1];
    }
    //bubble sort
    for(int i=0;i<sizeof(weight)/sizeof(weight[0]);i++)
    {
        for(int j=0;j<sizeof(weight)/sizeof(weight[0])-i-1;j++)
        {
            if(pw[j+1]>pw[j])
            {
                float temp=pw[j+1];
                pw[j+1]=pw[j];
                pw[j]=temp;

                int temp1=weight[j+1][0];
                weight[j+1][0]=weight[j][0];
                weight[j][0]=temp1;


                 int temp2=weight[j+1][1];
                weight[j+1][1]=weight[j][1];
                weight[j][1]=temp2;
                

                
            }
        }

    }
     for(int i = 0; i < 3; i++) {
        printf("%f", pw[i]);
    }

    for(int i=0;i<3;i++)
    {
        printf("%d%d ,",weight[i][0],weight[i][1]);
    }
    int total=20;
    knapsack(weight,total);

    
    


}