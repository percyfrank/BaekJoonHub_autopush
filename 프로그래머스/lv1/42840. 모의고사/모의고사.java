import java.util.*;
class Solution {
    public int calculate(int[] answers, int[] pattern) {
        int cnt = 0;

        for (int i = 0; i < answers.length; i++) {
            if(answers[i] == pattern[i % pattern.length]) {
                cnt++;
            }
        }
        return cnt;
    }

    public int[] solution(int[] answers) {

        int[][] pattern = {{1, 2, 3, 4, 5},{2, 1, 2, 3, 2, 4, 2, 5},{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        int cnt[] = new int[3];
        for (int i = 0; i < pattern.length; i++) {
            cnt[i] = calculate(answers,pattern[i]);
        }
        
        
        int maxcnt = Math.max(cnt[0],Math.max(cnt[1],cnt[2]));

        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < cnt.length; i++) {
            if(maxcnt == cnt[i]) list.add(i+1);
        }

        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}