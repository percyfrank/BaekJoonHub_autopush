import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i= 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int x = Integer.parseInt(br.readLine());

        int cnt = 0;

        Arrays.sort(arr);
        for(int i = 0; i < n-1; i++) {
            for(int j = i+1; j < n; j++) {
                if (arr[i] + arr[j] > x) {
                    break;
                } else if (arr[i] + arr[j] == x) {
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
        br.close();
    }
}