import java.util.*;
import java.io.*;

class Solution {
    public static void main(String args[]) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for(int test_case = 0; test_case < T; test_case++) {
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            long result = 0;
            int max = arr[N - 1];
            for (int i = N-2; i >= 0  ; i--) {
                if(arr[i] > max) {
                    max = arr[i];
                } else {
                    result += max-arr[i];
                }
            }
            System.out.printf("#%d %d\n",test_case+1,result);
        }
    }
}