import java.util.Scanner;
public class business{
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
         System.out.print("enter x:");
        int x=sc.nextInt();
       System.out.print("enter y:");
        int y=sc.nextInt();
        //System.out.print("enter y:");
        if(x<y){
            System.out.println("my business profit");
            
        }
        else{
            System.out.println("my business loss");
        }
    }

}