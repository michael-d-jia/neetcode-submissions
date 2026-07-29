class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = 1;

        for (int i = left; i < numbers.length - 1; i++) {
            for (int j = right; j < numbers.length; j++) {
                if (numbers[i] + numbers[j] == target) {
                    return new int[] { i+1, j+1 };
                }
            }
        }

        return new int[] {};
    }
}
