import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 예산 - 2512번
 */
public class Main {

    static int N;
    static int[] budget;    // 예산
    static int M;           // 총 예산

    public static void findBudget(int[] budgets, int targetBudget) {  //

        Arrays.sort(budgets);
        int end = budgets[budgets.length-1];    //  150
        int start = targetBudget / budgets.length;    //  121

        // 121 ~ 130
        while(true) {
            if(start > end) {
                System.out.println(end);
                break;
            }
            int midBudget = (start + end) / 2;  // 135

            int sumBudget = 0;
            for (int budget : budgets) {
                if(budget < midBudget) sumBudget += budget;
                else sumBudget += midBudget;
            }

            if(sumBudget == targetBudget) {
                System.out.println(midBudget);
                break;
            } else if(sumBudget > targetBudget) {
                end = midBudget - 1;
            } else {
                start = midBudget + 1;
            }
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        budget = new int[N];
        for (int i = 0; i < N; i++) {
            budget[i] = Integer.parseInt(st.nextToken());
        }
        M = Integer.parseInt(br.readLine());

        findBudget(budget,M);

    }
}