import java.util.Scanner;
public class greater{
public static void main(String [] args){
    Scanner sc=new Scanner(System.in);
    System.out.print(" enter the number:");
    int a=sc.nextInt();
    System.out.print(" enter the number:");
    int b=sc.nextInt();
    System.out.print(" enter the number:");
    int c=sc.nextInt();
    if(a>b && a>c){
      System.out.println(" greater then number");
    }
    else if(b>a && b>c){
        System.out.println(" not greater then number");
    }
    else{
        System.out.println("qual number");
    }
}
}
