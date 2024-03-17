#include <stdio.h>
void multiply(int size,int size2,int mat1[][size], int mat2[][size],int result[][size])
{
    for(int i=0;i<size2;i++)
    {
        for(int j=0;j<size;j++)
        {
            result[i][j]=0;
            for(int k=0;k<size;k++)
            {
                result[i][j]+=mat1[i][k]*mat2[k][j];
            }
        }
    }
}

int main() {
    int len,bred;
    printf("Enter size: ");
    scanf("%d%d",&len,&bred);
    len = len + 1;
    bred = bred + 1;

    int mat[len - 1][bred - 1];
    int mat2[len - 1][bred - 1]; 

    int i, j, k = 0;

  
    printf("Enter elements for mat[][]:\n");
    for (i = 0; i < len - 1; i++) {
        for (j = 0; j < bred - 1; j++) {
            printf("Enter the number on row %d and column %d: ", i + 1, j + 1);
            scanf("%d", &mat[i][j]);
        }
    }

    
    printf("\nEnter elements for mat2[][]:\n");
    for (i = 0; i < len - 1; i++) {
        for (j = 0; j < bred - 1; j++) {
            printf("Enter the number on row %d and column %d: ", i + 1, j + 1);
            scanf("%d", &mat2[i][j]);
        }
    }

 
    printf("\nMatrix mat[][]:\n");
    for (i = 0; i < len - 1; i++) {
        for (j = 0; j < bred - 1; j++) {
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }

   
    printf("\nMatrix mat2[][]:\n");
    for (i = 0; i < len - 1; i++) {
        for (j = 0; j < bred - 1; j++) {
            printf("%d ", mat2[i][j]);
        }
        printf("\n");
    }
    int result[len-1][bred-1];
    multiply(len-1,bred-1,mat,mat2,result);
    printf("\nResult Matrix is \n");
    for (i = 0; i < len - 1; i++) {
        for (j = 0; j < bred - 1; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }



    return 0;
}

