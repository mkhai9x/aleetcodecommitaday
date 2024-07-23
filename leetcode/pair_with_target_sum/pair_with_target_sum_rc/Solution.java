package pair_with_target_sum.pair_with_target_sum_rc;

public class Solution {
    public  int [] search(int[] arr, int targetSum){
        int left = 0, right = arr.length - 1;
        while (left < right){
            int sum = arr[left] + arr[right];
            if (sum < targetSum) {
                left += 1;
            } else if (sum > targetSum) {
                right -= 1;
            } else {
                return new int[] {left, right};
            }
        }

        return new int[] {-1,-1};
    }
}
