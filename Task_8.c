bool isIdealPermutation(int* nums, int numsSize){
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] - i > 1 || i - nums[i] > 1)
            return 0;
    }
    return 1;
}
