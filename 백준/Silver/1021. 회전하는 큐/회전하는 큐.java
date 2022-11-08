import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

/**
 * 회전하는 큐 - 1021번
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        LinkedList<Integer> deque = new LinkedList<>();
        int[] arr = new int[M];

        for (int i = 0; i < N; i++) {
            deque.add(i + 1);
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int cnt = 0;
        for (int i = 0; i < M; i++) {
            int idx = deque.indexOf(arr[i]);

            if(idx <= deque.size() / 2) {
                while(deque.peekFirst() != arr[i]) {
                    deque.addLast(deque.pollFirst());
                    cnt++;
                }
            } else {
                for (int j = 0; j < deque.size() - idx; j++) {
                    deque.addFirst(deque.pollLast());
                    cnt++;
                }
            }
            deque.pollFirst();

        }
        System.out.println(cnt);

    }
}