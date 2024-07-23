package find_non_duplicates_rc;

public class Solution {
    public int remove(int[] arr){
        int nextNonDuplicate = 1;
        if (arr.length == 0) return 0;
        for (int i = 1; i < arr.length; i++){
            if (arr[nextNonDuplicate - 1] != arr[i]){
                arr[nextNonDuplicate] = arr[i];
                nextNonDuplicate += 1;
            }
        }
        return nextNonDuplicate;
    }
}
