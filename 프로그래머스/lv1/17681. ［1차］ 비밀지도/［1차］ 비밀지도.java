class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {

        int[][] map1 = new int[n][n];
        int[][] map2 = new int[n][n];
        String[] answer = new String[n];

        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= n; j++) {
                map1[i][n-j] = arr1[i] % 2;
                map2[i][n-j] = arr2[i] % 2;
                arr1[i] /= 2;
                arr2[i] /= 2;
            }
        }

        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(map1[i][j] == 1 || map2[i][j] == 1) {
                    sb.append("#");
                } else {
                    sb.append(" ");
                }
            }
            answer[i] = sb.toString();
            sb = new StringBuffer();
        }
        return answer;
    }
}