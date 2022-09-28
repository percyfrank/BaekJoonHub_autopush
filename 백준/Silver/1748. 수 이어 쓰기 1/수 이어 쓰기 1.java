import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int n = N;
        int cnt = 0;
        int sum = 0;

        // 입력된 N의 자릿수 구하기
        while(true) {
            n  = (int) n / 10;
            cnt++;
            if (n == 0) break;
        }

        for (int i = 1; i < cnt; i++) {
            sum += (int) (i * (9 * Math.pow(10,i-1)));
        }

        sum += (int) (cnt * (N-Math.pow(10,cnt-1)+1));

        System.out.println(sum);
    }
}