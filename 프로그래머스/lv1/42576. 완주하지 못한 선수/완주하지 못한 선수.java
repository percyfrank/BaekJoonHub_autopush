import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String,Integer> map = new HashMap<>();
        
        for(String key : participant) {
            map.put(key, map.getOrDefault(key,0) + 1);
            // System.out.println(map.get(key));
        }
        
        for(String complete : completion) {
            if(map.containsKey(complete)) {
                map.put(complete,map.getOrDefault(complete,0) - 1);
                // System.out.println(map.get(complete));
            }
        }
        
        for(String key : map.keySet()) {
            if(map.get(key).equals(0)) {
            }
            else {
                answer = key;
            }
        }
        
        return answer;
        
    }
}