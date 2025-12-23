import java.io.*;
import java.util.StringTokenizer;
import java.util.Scanner;


public class Main {
    
	public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int r = Integer.parseInt(input.nextLine());
        int g = Integer.parseInt(input.nextLine());
        int b = Integer.parseInt(input.nextLine());

        int p = r*3+g*4+b*5;

        System.out.println(p);


	}
}
