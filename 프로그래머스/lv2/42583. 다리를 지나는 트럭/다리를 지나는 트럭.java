import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> queue = new LinkedList<>();
        
        // 트럭 총 무게
        int sum = 0;
        
        for(int truck : truck_weights) {
            while(true) {
                // 다리를 건너는 트럭이 없을 경우
                if(queue.isEmpty()) {
                    queue.add(truck);
                    sum += truck;
                    answer++;
                    break;
                } 
                // 다리 위에 트럭이 있는 경우(3가지로 나뉨)
                else {
                    // 트럭이 꽉 찬 경우
                    if(queue.size() == bridge_length) {
                        sum -= queue.peek();
                        queue.poll();
                    }
                    // 다음 트럭이 다리에 오르면 최대 무게 초과인 경우
                    else if(sum + truck > weight) {
                        queue.add(0);
                        sum += 0;
                        answer++;
                    } 
                    // 다음 트럭이 다리에 올라도 최대 무게 이내인 경우
                    else {
                        queue.add(truck);
                        sum += truck;
                        answer++;   
                        break;
                    }  
                }  
            }
        }
        
        // 마지막 트럭이 다리에 올라간 시점까지 걸린 시간 + 다리의 길이
        return answer + bridge_length;
    }
}