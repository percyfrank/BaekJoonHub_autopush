class Solution {
    public boolean solution(int x) {
        boolean answer = true;

        String harshad = String.valueOf(x);

        int sum = 0;
        for (int i = 0; i < harshad.length(); i++) {
            sum += (harshad.charAt(i) - '0');
        }

        if(x % sum == 0) answer = true;
        else answer = false;

        return answer;
    }
}