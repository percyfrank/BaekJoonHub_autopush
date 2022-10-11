import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 배열 합치기 - 11728번
 */
public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arrA = new int[N];
        int[] arrB = new int[M];
        int[] arrC = new int[N+M];
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            arrA[i] = Integer.parseInt(st1.nextToken());
        }

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for(int j = 0; j < M; j++) {
            arrB[j] = Integer.parseInt(st2.nextToken());

        }

        Arrays.sort(arrA);
        Arrays.sort(arrB);

        int a = 0;
        int b = 0;
        int c = 0;
        while(true) {
            if(arrA[a] >= arrB[b]) {
                arrC[c] = arrB[b];
                c++;
                b++;
                if(b == M) {
                    while(a != N) {
                        arrC[c] = arrA[a];
                        c++;
                        a++;
                    }
                    break;
                }
            } else{
                arrC[c] = arrA[a];
                c++;
                a++;
                if(a == N) {
                    while(b != M) {
                        arrC[c] = arrB[b];
                        c++;
                        b++;
                    }
                    break;
                }
            }
        }
        StringBuffer sb = new StringBuffer();
        for(int i : arrC) {
            sb.append(i).append(" ");
        }
        System.out.println(sb);
        
    }
}