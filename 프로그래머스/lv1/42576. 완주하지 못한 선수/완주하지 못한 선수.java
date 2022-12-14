import java.util.*;

class Solution {
    public static String solution(String[] participant, String[] completion) {

        Map<String, Integer> map = new HashMap<>();
        for (String s : participant) {
            map.put(s, map.getOrDefault(s, 0) + 1);
        }

        String answer = "";
        for (String s : completion) {
            map.put(s, map.get(s) - 1);
        }

        for(String s : map.keySet()) {
            if(map.get(s) != 0) {
                answer = s;
            }
        }
//         }
//         Set set = map.entrySet();
//         Iterator it = set.iterator();

//         while (it.hasNext()) {
//             Map.Entry e = (Map.Entry) it.next();
//             if ((Integer) e.getValue() != 0) {
//                 answer = (String) e.getKey();
//             }
//         }
        return answer;
    }
}