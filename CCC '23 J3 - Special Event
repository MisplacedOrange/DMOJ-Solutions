import java.io.*;
import java.util.StringTokenizer;
import java.util.Scanner;
import java.util.ArrayList;


public class Main {
	public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int people = Integer.parseInt(input.nextLine());


        String lines[] = new String[people];

        for (int i = 0; i < people; i++ ) {
            lines[i] = input.nextLine();
        }

        int cols = lines[0].length();

        int[] attendance = new int[cols];
        
        for (int row = 0; row < lines.length; row++ ) {
            for (int col = 0; col < cols; col++ ) {
                char attend = lines[row].charAt(col);
                if (attend == 'Y') {
                    attendance[col]++;
                }
            }
        }

            int MaxY = 0;

        for (int i = 0; i < attendance.length; i++) {
            if (attendance[i] > MaxY) {
                MaxY = attendance[i];
            }
        }

        ArrayList<Integer> MaxCol = new ArrayList<>();

        for (int i = 0; i < attendance.length; i++) {
            if (attendance[i] == MaxY) {
                MaxCol.add(i);
            }
        }
        
        for (int i = 0; i < MaxCol.size(); i++) {
            System.out.print(MaxCol.get(i) + 1);
            if (i != MaxCol.size() - 1) {
                System.out.print(",");
            }
        }

	}
}
