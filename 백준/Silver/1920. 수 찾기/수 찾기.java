import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 수 찾기 - 1920번
 */
public class Main {
    static int N;
    static int M;
    static int[] A;
    static int[] arr;
    static StringBuffer sb = new StringBuffer();
    public static int binary(int[] arr, int target, int start, int end) {
        if(start > end) return 0;
        int mid = (start + end) / 2;
        if(arr[mid] == target) return 1;
        else if(arr[mid] > target) return binary(arr, target, start, mid - 1);
        else return binary(arr, target, mid + 1, end);
    }

    public static String findNumber() {
        Arrays.sort(A);
        for (int i = 0; i < M; i++) {
            int binary = binary(A, arr[i], 0, N-1);
            sb.append(binary).append("\n");
        }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N ; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        M = Integer.parseInt(br.readLine());
        arr = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M ; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        findNumber();
        System.out.println(sb);
    }
}