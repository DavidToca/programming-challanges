import java.util.Scanner;

class Main {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] array = new int[n];
        int total = 0;
        for(int i=0; i<n;i++){
            array[i] = sc.nextInt();
            total+=array[i];
            array[i]=total;
        }

        int cases = sc.nextInt();

        for(int i=0; i<cases;i++){
            int p = sc.nextInt();
            int q = sc.nextInt();

            if(p == 0){
                System.out.println(array[q]);
            } else {
                System.out.println(array[q]- array[p-1]);
            }
        }

    }
}