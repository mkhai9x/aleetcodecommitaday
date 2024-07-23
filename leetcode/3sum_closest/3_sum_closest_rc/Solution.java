

import java.util.*;
public class Solution {
    public int searchTriplet(int[] arr, int targetSum){
        Arrays.sort(arr);
        int closestSum = 0;
        double minDistance = Double.POSITIVE_INFINITY;
        for (int i = 0; i < arr.length - 2; i++){
            int left = i + 1;
            int right = arr.length - 1;
            while (left < right){
                int currSum = arr[i] + arr[left] + arr[right];
                int currDistance = Math.abs(currSum - targetSum);
                if (currDistance < minDistance){
                    closestSum = currSum;
                    minDistance = currDistance;
                }
                if (currSum > targetSum){
                    right -= 1;
                } else if (currSum < targetSum){
                    left += 1;
                } else {
                    return closestSum;
                }
            }


        }



        return closestSum;
    }
}
