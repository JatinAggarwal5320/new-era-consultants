import java.util.ArrayList;

public class StudentInfo {
    public static void main(String[] args) {
        ArrayList<Integer> ages = new ArrayList<>();
        ArrayList<Double> temperatures = new ArrayList<>();
        ArrayList<Boolean> attendance = new ArrayList<>();

        ages.add(19);           
        temperatures.add(98.6); 
        attendance.add(true);   

        ages.add(20);
        temperatures.add(99.1);
        attendance.add(false);

        ages.add(18);
        temperatures.add(97.9);
        attendance.add(true);

        System.out.println("Student Data:\n");

        for (int i = 0; i < 3; i++) {
            int age = ages.get(i);                  
            double temp = temperatures.get(i);      
            boolean isPresent = attendance.get(i);  

            System.out.println("Student " + (i + 1) + ":");
            System.out.println("Age: " + age);
            System.out.println("Temperature: " + temp + "°F");
            System.out.println("Present Today: " + (isPresent ? "Yes" : "No"));
            System.out.println();
        }
    }
}
