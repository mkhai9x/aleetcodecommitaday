

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TripletSumCloseToTargetTest {
    Solution solution;

    @BeforeEach
    void setUp(){
        solution = new Solution();
    }

    @Test
    @DisplayName("Test Case 1")
    void testCase1(){
        assertEquals(solution.searchTriplet(new int[] {-1,0,2,3}, 3), 2);
    }

    @Test
    @DisplayName("Test Case 2")
    void testCase2(){
        assertEquals(solution.searchTriplet(new int[] {-3,-1,1,2}, 1), 0);
    }

    @Test
    @DisplayName("Test Case 3")
    void testCase3(){
        assertEquals(solution.searchTriplet(new int[] {1,0,1,1}, 100), 3);
    }


    @Test
    @DisplayName("Test Case 4")
    void testCase(){
        assertEquals(solution.searchTriplet(new int[] {0,0,0,0}, 0), 0);
    }

    @Test
    @DisplayName("Test Case 5")
    void testCase5(){
        assertEquals(solution.searchTriplet(new int[] {-1,2,1,-4}, 1), 2);
    }


}