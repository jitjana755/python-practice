import java.util.Scanner;
public class triangle{
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("1st number:");
        int a=sc.nextInt();
           System.out.print("enter 2st number:");
             int b=sc.nextInt();
             System.out.print("enter 3st number:");
              int c=sc.nextInt();
              if(a+b>c && b+a>c && c+a>b){
                 System.out.print(" vailed triangle ");
              }
              else{
                 System.out.println("not vailed triangle");
              }
    }
}