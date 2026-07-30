import java.util.Scanner;

public class bb {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter length: ");
        int length = sc.nextInt();

        System.out.print("Enter breadth: ");
        int breadth = sc.nextInt();

        //int area = length * breadth;
        //int perimeter = 2 * (length + breadth);

       // System.out.println("Area = " + area);
        //System.out.println("Perimeter = " + perimeter);

        if (length > breadth) {
            System.out.println("Area is greater than perimeter.");
        } else {
            System.out.println("Area is not greater than perimeter.");
        }

        sc.close();
    }
}