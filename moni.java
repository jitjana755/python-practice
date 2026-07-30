import java.util.Scanner;
public class moni{
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the radius:");
        double r=sc.nextDouble();
        System.out.print("The area of the circle is:");
        double area=3.14159*r*r;
        System.out.println(area);
    }
}