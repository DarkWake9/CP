import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

//Write your code here

   static int B = 0;
   static int H = 0;
   static boolean flag;
    // Static block
    static
    {
        Scanner sc = new Scanner(System.in);
         B = sc.nextInt();
         H = sc.nextInt();
        sc.close();
        
        if (B<=0 || H<=0){
            System.out.println("java.lang.Exception: Breadth and height must be positive");
            flag = false;
        }
        else{
            flag = true;
        }
    }


public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class


