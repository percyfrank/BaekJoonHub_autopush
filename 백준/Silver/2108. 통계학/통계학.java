import java.util.Arrays;
import java.util.Scanner;

/**
 * 통계학 - 2108번
 */
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        double sum = 0;
        for(int i = 0; i < N; i++) {
            sum += arr[i];
        }
        double mean = sum / N;

        //산술평균
        System.out.println(Math.round(mean));

        //오름차순 정렬
        Arrays.sort(arr);

        // 중앙값
        int mid = N / 2;
        System.out.println(arr[mid]);

        //최빈값
        boolean flag = true; //최빈값이 첫번째이면 false 두번째이면 true
        int mod = arr[0]; //최빈값(정수가 한개일 땐 그 즉시 최빈값)
        int max = Integer.MIN_VALUE; //최빈값 빈도의 최댓값
        int cnt = 0; //최빈값이 몇번 등장하는지

        for(int i = 0; i < N-1; i++) {
            if(arr[i] == arr[i+1]) {
                cnt++;
            } else {
                cnt = 0;
            }

            if(max < cnt) {
                max = cnt;
                mod = arr[i];
                flag = false;
            } else if(max == cnt && flag == false) {
                mod = arr[i];
                flag = true;
            }
        }
        System.out.println(mod);

        //범위
        System.out.println(arr[N - 1] - arr[0]);
    }

}