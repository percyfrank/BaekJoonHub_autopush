import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] % divisor == 0) list.add(arr[i]);
        }
        if(list.size() == 0) list.add(-1);
        else Collections.sort(list);

        int[] answer = new int[list.size()];
        int size = 0;
        for (Integer temp : list) {
            answer[size++] = temp;
        }

        return answer;
    }
}