import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        Deque<Integer> deque = new LinkedList<>();
        
        deque.add(arr[0]);
        
        for(int i=1; i<arr.length; i++) {
            if(arr[i]!=deque.peekLast()) {
                // System.out.println(arr[i]);
                deque.offer(arr[i]);
                
            }
        }
        
        int[] answer = new int[deque.size()];
        while(!deque.isEmpty()) {
            for(int i=0; i<answer.length; i++) {
                answer[i] = deque.pollFirst();
            }
        }
        
        // System.out.println(Arrays.toString(answer));

        return answer;
    }
}