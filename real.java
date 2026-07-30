import java.util.Scanner;
public class real{
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
            System.out.print(" enter number ");
            double n=sc.nextDouble(); // x=3.1445
            int x= (int)n;
            if(n-x> 0)
                {
                System.out.println("is integer number:");
        
            }
            else{
              System.out.println("is not integer number:");
            }
        }
    }
