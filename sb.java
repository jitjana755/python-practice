import java.util.Scanner;
public class sb{
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("enter the number:");
        int n=sc.nextInt();
        if(n>999 && n<10000){
        System.out.print("is 4 digit number");
        }
        else{
            System.out.print("not 4 digit number:");
        }
    }
}