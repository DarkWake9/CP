import java.util.*;
import java.io.*;
import java.lang.Math.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            for(int j=0;j<n;j++){
                double temp = a;
                for (int k = 0; k <= j; k++){
                    temp = temp + (Math.pow(2,k)) * b; 
                }
                System.out.print((int) temp + " ");
            }
            if (i != t - 1){
                System.out.println();
            }
        }
        in.close();   
    }
}