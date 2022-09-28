import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception{

        Scanner sc = new Scanner(System.in);
        StringBuffer sb = new StringBuffer();

        int[] count = new int[26];
        String s = sc.nextLine();

        for(int i = 0 ; i < s.length(); i++) {
            count[(int)(s.charAt(i)-'a')]++;
        }

        for(int cnt : count) {
            System.out.print(cnt + " ");
        }
    }
}