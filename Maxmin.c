#include<stdio.h>
void maxmin(int arr[], int low, int high, int *max, int *min) {
    int mid, max1, min1, max2, min2;
    if (low == high) {
        *max = arr[low];
        *min = arr[low];
        return;
    }

    if (low == high - 1) {
        if (arr[low] > arr[high]) {
            *max = arr[low];
            *min = arr[high];
        } else {
            *max = arr[high];
            *min = arr[low];
        }
        return;
    }

    mid = low + (high - low) / 2;
    maxmin(arr, low, mid, &max1, &min1);
    maxmin(arr, mid + 1, high, &max2, &min2);
    *max = (max1 > max2) ? max1 : max2;
    *min = (min1 < min2) ? min1 : min2;
}

int main() {
    int arr[3] = {10, 5, 20};
    int n = sizeof(arr) / sizeof(int);
    int max, min;
    maxmin(arr, 0, n - 1, &max, &min); // Corrected: pass n - 1 as high
    printf("Max and min numbers are %d, %d\n", max, min);
    return 0;
}
