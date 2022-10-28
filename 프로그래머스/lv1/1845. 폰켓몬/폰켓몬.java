
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] nums) {
        // 폰켓몬 종류가 중복되어도 제거된다.
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }

        int num = nums.length / 2;

        // set의 개수와 num을 비교해서 큰 값을 return하도록 설계
        
        if(num < set.size()) return num;
        else return set.size();
    }
}