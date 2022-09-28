import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        int multiply = A * B * C;
        String s = String.valueOf(multiply);
        int[] arr = new int[10];

        for(int i = 0; i < s.length(); i++) {
            arr[s.charAt(i)-'0']++;
        }

        for(int cnt : arr) {
            System.out.println(cnt);
        }
    }
}