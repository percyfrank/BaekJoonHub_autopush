import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int num : scoville) {
            pq.add(num);
        }
        
        while(pq.peek() < K) {
            if(pq.size() == 1) {
                answer = -1;
                break;
            }
            
            int first = pq.poll();            
            int second = pq.poll();
            
            pq.add(first + second*2);
            
            answer++;
        }
        
        return answer;
    }
}