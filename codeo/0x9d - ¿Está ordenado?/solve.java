import java.util.Scanner;


class Main{

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] array = new int[n];

        for(int i=0; i<n; i++){
            array[i] = sc.nextInt();
        }

        int last_number = array[0];

        for(int i=1; i<n; i++){
            if(last_number > array[i]){
                System.out.println("Desordenado");
                return;
            }

            last_number = array[i];
        }
        System.out.println("Ordenado");

    }
}