
/* UVA 10018 - Reverse And Add
   David Felipe Toca
   david.virusfel@gmail.com
   Accepted
   simulation
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {

        public static void main(String[] args)throws IOException {
                 
                BufferedReader buffer=new BufferedReader(new InputStreamReader(System.in));

                
                int cases=Integer.parseInt(buffer.readLine());

                while (cases--!=0) {
                        
                        int iteraciones=0;
                        String number,reverse;
                        number=buffer.readLine();
                        
                        do {
                                iteraciones++;
                                
                                 reverse=new StringBuilder(number).reverse().toString();
                                
                                 number=""+(Long.parseLong(number)+Long.parseLong(reverse));
                                 
                        } while (!number.equals(new StringBuilder(number).reverse().toString()));
                        
                        System.out.println(iteraciones+" "+number);
                        
                        
                }
        }

}
