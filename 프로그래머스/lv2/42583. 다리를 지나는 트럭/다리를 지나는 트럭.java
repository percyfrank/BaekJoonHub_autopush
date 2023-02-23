import java.util.*;

class Solution {
    
    class Truck {
        int weight;
        int move;
        
        public Truck(int weight) {
            this.weight = weight;
            this.move = 1;
        }
        
        public void moving() {
            this.move++;
        }
    }
    
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        
        Queue<Truck> wait = new LinkedList<>();
        Queue<Truck> move = new LinkedList<>();
        
        // 대기 큐에 전부 넣기
        for(int truck : truck_weights) {
            wait.offer(new Truck(truck));
        }
        
        // 다리 위에 올라와있는 트럭의 총 무게
        int curWeight = 0;
        
        //  모든 트럭이 다리를 건넜을 때 걸린 최단 시간
        int answer = 0;
        
        while(!wait.isEmpty() || !move.isEmpty()) {
            
            // 다리에 올라온 순간 시간 +1
            answer++;
            
            // 다리 건너는 트럭이 없는 경우
            if(move.isEmpty()) {
                Truck t = wait.poll();
                curWeight += t.weight;
                move.offer(t);
                continue;
            }
            
            // 여기서부턴 다리에 트럭이 있는 경우
            // 다리 위에 있는 모든 트럭 한 칸씩 이동
            for(Truck t : move) {
                t.moving();
            }
            
            // 다리에 트럭이 꽉 찬 경우
            // 맨 앞에 있는 트럭의 move가 다리 길이를 넘어설 경우
            if(move.peek().move > bridge_length) {
                curWeight -= move.poll().weight;
            }
            
            // 다음 트럭이 다리에 올라도 최대 무게 이내인 경우
            if(!wait.isEmpty() && curWeight + wait.peek().weight <= weight) {
                Truck t = wait.poll();
                curWeight += t.weight;
                move.add(t);
            }
        }
        
        return answer;
    }
}