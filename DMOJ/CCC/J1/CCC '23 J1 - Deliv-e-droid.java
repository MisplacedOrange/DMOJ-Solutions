// Source: https://usaco.guide/general/io

import java.io.*;
import java.util.StringTokenizer;
import java.util.Scanner;
// import java.util.ArrayList;


public class Main {
    
	public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int sixseven = Integer.parseInt(input.nextLine());
        int fourtyone = Integer.parseInt(input.nextLine());

        int p = sixseven * 50;
        int pl = fourtyone * 10;
        int t = 0;

        if (sixseven > fourtyone) {
            t += 500;
        }
        int sigma = p - pl + t;
        System.out.println(sigma);

	}
}
