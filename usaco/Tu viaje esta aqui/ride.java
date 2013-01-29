/*
ID: alchemi3
LANG: JAVA
TASK: ride
*/
import java.io.FileReader;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * 
 */

/**
 * @author davidtoca
 *
 */
public class ride {

	/**
	 * @param args
	 */
	public static void main(String[] args)throws Throwable {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(new FileReader("ride.in"));
		
		System.setOut(new PrintStream("ride.out"));
		
		String cometa = sc.nextLine();

		String grupo = sc.nextLine();


		int sumaCometa = 1;

		for(int i = 0; i < cometa.length(); i++){

		    sumaCometa*= (int)cometa.charAt(i) - 64;

		}

		int sumaGrupo = 1;

		for(int i = 0; i < grupo.length(); i++){

		    sumaGrupo*= (int)grupo.charAt(i) - 64;

		}
		

		boolean go = sumaGrupo%47 == sumaCometa%47;

			
		System.out.println((go)?"GO":"STAY");
			
		
		
	}

}
















