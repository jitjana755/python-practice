import java.util.Scanner;
public class studentcode{
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("enter the number:");
        int b=sc.nextInt();
        if(b%5 == 0){
            System.out.print(" 5 divisible number");

        }else if(b%3 == 0){
            System.out.println(" 3 divisiable number:");
        }else if(b%5 == 0 ){
        }
             else if(b%3 ==0){
         System.out.println("both divisiable");
        }
        else{
            System.out.println("not both divisiable");
        }
       
    }
}