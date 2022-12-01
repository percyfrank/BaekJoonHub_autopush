import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < score.length; i++) {
            if(i < k) {
                pq.add(score[i]);
                answer[i] = pq.peek();
            }
            else if(i >= k) {
                if(pq.peek() <= score[i]) {
                    pq.poll();
                    pq.add(score[i]);
                    answer[i] = pq.peek();
                } else {
                    answer[i] = pq.peek();
                }
            }
        }
        return answer;
        
    }
}