public class Solution {
    public boolean isHappy(int n) {
        int fast = n, slow = n;
        do {
            fast = this.calculateSumSquare(this.calculateSumSquare(fast));
            slow = this.calculateSumSquare(slow);

        } while (slow != fast);
        if (slow == 1) return true;
        else return false;

    }

    public int calculateSumSquare(int num){
        int sum = 0;
        while (num > 0){
            int digit = num % 10;
            sum += digit * digit;
            num = num / 10;
        }
        return sum;

    }
}
