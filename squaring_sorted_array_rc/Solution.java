package squaring_sorted_array_rc;

public class Solution {
    public int[] makeSquares(int[] arr) {
        int n = arr.length;
        int [] squares = new int[n];
        int start = 0; int end = n - 1;
        int squareIndex = n - 1;
        while (start <= end){
            int leftSquare = arr[start] * arr[start];
            int rightSquare = arr[end] * arr[end];
            if (leftSquare <= rightSquare) {
                squares[squareIndex] = rightSquare;
                end -= 1;
            } else {
                squares[squareIndex] = leftSquare;
                start += 1;
            }
            squareIndex -= 1;

        }
        return squares;

    }
}
