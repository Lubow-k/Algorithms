int search(int* nums, int numsSize, int target){
    int low, high, middle;
    low = 0;
    high = numsSize - 1;
    while (low <= high) {
        middle = (low + high) / 2;
        if (target == nums[middle])
            return middle;
        else if (target < nums[middle])
            high = middle - 1;
        else
            low = middle + 1;
    }
    return -1;
}
