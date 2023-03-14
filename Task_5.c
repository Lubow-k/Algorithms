#include <stdlib.h>

void swap(int* arr, int i, int j) {
    int buf = arr[i];
    arr[i] = arr[j];
    arr[j] = buf;
}

void sift(int* arr, int i, int n) {
    int l, r, k;
    i++;
    while ((l = 2 * i) <= n) {
        r = (l + 1 <= n) ? l + 1 : i;
        if ((arr[i - 1] >= arr[l - 1]) && (arr[i - 1] >= arr[r - 1]))
            return;
        if (arr[l - 1] >= arr[r - 1])
            k = l;
        else
            k = r;
        swap(arr, i - 1, k - 1);
        i = k;
    }
}

void wiggleSort(int* nums, int numsSize) {
    int* sorted = (int*)malloc(numsSize * sizeof(int));

    for (int i = numsSize / 2; i >= 0; i--)
        sift(nums, i, numsSize);
    for (int i = numsSize - 1; i >= 0; i--) {
        sorted[i] = nums[0];
        nums[0] = nums[i];
        sift(nums, 0, i);
    }

    int k = numsSize / 2;
    int extra = (numsSize % 2) ? k : k - 1;
    for (int i = 0; i < k; i++) {
        nums[2 * i] = sorted[extra];
        nums[2 * i + 1] = sorted[numsSize - i - 1];
        extra--;
    }
    if (numsSize % 2) {
        nums[numsSize - 1] = sorted[0];
    }

    free(sorted);
}
