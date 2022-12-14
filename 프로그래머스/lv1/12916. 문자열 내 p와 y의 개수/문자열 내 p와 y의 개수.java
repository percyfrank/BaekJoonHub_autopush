class Solution {
    boolean solution(String s) {

        int p_cnt = 0;
        int y_cnt = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(c == 'p' || c == 'P') p_cnt++;
            else if (c == 'y' || c == 'Y') y_cnt++;
        }
        return p_cnt == y_cnt ? true : false;
    }

}