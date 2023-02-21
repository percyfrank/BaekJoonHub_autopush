import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {

        
        // 작업일 수 배열 
        int[] works = new int[progresses.length];
        for(int i=0; i<progresses.length; i++) {
            int remain = 100-progresses[i];
            if(remain%speeds[i]==0) works[i] = remain/speeds[i];
            else works[i] = remain/speeds[i] + 1;
        }
        
        System.out.println(Arrays.toString(works));
        
//         int count = 0;
//         int idx = works[0];
//         for(int i=0; i<works.length-1;i++) {
//             if(idx < works[i+1]) {
//                 count++;                
//             }
//         }
        
        
    
        List<Integer> list = new ArrayList<>();
        
        int j = 0;
        int cnt = 1;
        int max = works[0];
        for(int i=0; i<works.length-1; i++) {
            if(max >= works[i+1]) {
                cnt++;
            } else {
                list.add(cnt);
                cnt = 1;
                max = works[i+1];
            }
        }
        list.add(cnt);
        
        int[] answer = new int[list.size()];
        int i = 0;
        for(Integer num : list) {
            answer[i++] = num;
        }
        
        
        return answer;
    }
}