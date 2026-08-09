import java.util.*;

public class Solution {
    public int[] solution(int []arr) { 
        Deque<Integer> queue = new ArrayDeque<>();
        
        for (int i = 0; i < arr.length; i++) {
            if (queue.isEmpty() || queue.peekLast() != arr[i]) {
                queue.addLast(arr[i]);
            }
        }
        
        int size = queue.size();
        int[] answer = new int[size];
        
        for (int i = 0; i < size; i++) {
            answer[i] = queue.pollFirst();
        }
        
        return answer;
    }
}