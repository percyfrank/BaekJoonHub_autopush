import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        
        // 높은 숫자 우선하는 우선순위 큐 선언
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for(Integer priority : priorities) {
            pq.add(priority);
        }
        // System.out.println(pq);
        
        int answer = 0;
        // 우선 순위 큐가 빌 때 까지 반복
        while(!pq.isEmpty()) {
            for(int i=0; i<priorities.length; i++) {
                // 값이 일치하는 경우 인쇄 순서+1
                if(pq.peek()==priorities[i]) {
                    answer++;
                    pq.poll();
                    // 위치까지 일치하는 경우 answer 반환
                    if(location==i) return answer;
                }
            }
        }
        
        return answer;
    }
}