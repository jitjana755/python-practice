import java.util.Scanner;
public class ju{
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("enter the number:");
        int n=sc.nextInt();
        if(n%5 ==0 || n%3 ==0){
         System.out.print("4 digit 3 divisible ");
        }
        else{
             System.out.print("4 digit 3 divisible not");
        }
    }
}