import java.util.Scanner;
public class ternaryvariable{
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("enter the number:");
        int n=sc.nextInt();
        int jit= (n>=0) ? 100: 0;
        System.out.println(jit);

    }
}