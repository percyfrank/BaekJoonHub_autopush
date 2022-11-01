class Solution {
    public int solution(int n) {

        int[] arr = new int[n + 1];
        int answer = 0;

        for (int i = 2; i < Math.sqrt(n) + 1; i++) {
            if (arr[i] == 0) {
                int j = 2;
                while (j * i <= n) {
                    arr[i * j] = 1;
                    j++;
                }
            }
        }

        for (int i = 2; i < n + 1; i++) {
            if(arr[i] == 0) {
                answer++;
            }
        }

        return answer;
    }
}