import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 귀여운 라이언 - 15565번
 */
public class Main {
    public static void two_pointer(int N, int K, int[] arr) {

        int left = 0;
        int right = 0;
        int cnt = 0;
        int size = Integer.MAX_VALUE;

        while(right < N) {
            if(cnt < K){
                if(arr[right] == 1){
                    cnt++;
                }
                right++;
            }
            else {
                if(arr[left] == 1) {
                    size = Math.min(size,right-left);
                    cnt--;
                }
                left++;
            }
        }

        while(left < N) {
            if(cnt < K) break;
            if(arr[left] == 1) {
                size = Math.min(size, right - left);
                cnt--;
            }
            left++;

        }

        if(size == Integer.MAX_VALUE)
            System.out.println(-1);
        else
            System.out.println(size);

    }
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        two_pointer(N,K,arr);
    }
}