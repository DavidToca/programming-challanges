//this actually it's not my, but it got AC !

import java.io.IOException;
import java.util.StringTokenizer;


public class Problema1{
        public static int [] lista = new int [1000000];
        
        static String ReadLn (int maxLg)  // utility function to read from stdin
    {
        byte lin[] = new byte [maxLg];
        int lg = 0, car = -1;
        //String line = "";

        try
        {
            while (lg < maxLg)
            {
                car = System.in.read();
                if ((car < 0) || (car == '\n')) break;
                lin [lg++] += car;
            }
        }
        catch (IOException e)
        {
            return (null);
        }

        if ((car < 0) && (lg == 0)) return (null);  // eof
        return (new String (lin, 0, lg));
    }
        
        public static int ciclo(int n) {
                int ciclos = 1;
                while (n!=1) {
                        if (n%2 == 0) {
                                n = n/2;
                                if(n < 1000000){
                                        if(buscar(n)!= -1){
                                                return(ciclos+buscar(n));
                                        }
                                }
                        }else {
                                n = (n * 3) + 1;
                                if(n < 1000000){
                                        if(buscar(n)!= -1){
                                                return(ciclos+buscar(n));
                                        }
                                }
                        }
                        
                        ciclos ++;
                }
                return ciclos;
        }
        
        private static int buscar(int n) {
                        if (lista[n] != 0) {
                                return lista [n];
                        }
                return -1;
        }
        
        public static void main(String[] args) {
                String n = null;
                int max = 0;
                int tmp = 0;
                int inicio = 0;
                int fin = 0;
                
                
                while ((n = ReadLn(255))!= null) {
                        StringTokenizer token = new StringTokenizer(n);
                        int a = inicio = Integer.parseInt(token.nextToken());
                        int b = fin = Integer.parseInt(token.nextToken());
                        
                        if (inicio > fin) {
                                tmp = inicio;
                                inicio = fin;
                                fin = tmp;
                        }
                        
                        max = 0;
                        tmp = 0;
                        
                        for (int i = inicio; i <= fin; i++) {
                                
                                if(buscar(i) == -1){
                                        tmp = ciclo(i);
                                        lista[i] = tmp;
                                }else {
                                        tmp = buscar(i);
                                }
                                
                                if (tmp > max) {
                                        max = tmp;
                                }
                        }
                        
                        System.out.println(a+" "+b+" "+max);
                        max = 0;
                }
        }
}
