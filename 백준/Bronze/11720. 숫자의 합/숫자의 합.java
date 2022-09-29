import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        // 숫자 갯수, 배열
        int N = sc.nextInt();
        String s = sc.next();

        int sum = 0;

        for(int i = 0; i < N; i++) {
            sum += s.charAt(i)-'0';
        }

        System.out.println(sum);
    }
}