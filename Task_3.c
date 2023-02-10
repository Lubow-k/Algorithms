int search(int* nums, int numsSize, int target){
    int low, high, middle;
    low = 0;
    high = numsSize - 1;
    while (low <= high) {
        middle = (low + high) / 2;
        if (target < nums[middle]) 
            high = middle - 1;
        else if (target > nums[middle])
            low = middle + 1;
        else
            return middle;
    }
    return -1;
}
