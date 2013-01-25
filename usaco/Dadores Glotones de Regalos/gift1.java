/*
ID: gift1
LANG: JAVA
TASK: gift1
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
public class gift1 {

	/**
	 * @param args
	 */
	public static void main(String[] args)throws Throwable {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(new FileReader("gift1.in"));
		
		System.setOut(new PrintStream("gift1.out"));
		
		int np = sc.nextInt();
		
		Map<String, Integer> recived = new HashMap<String, Integer>();
		Map<String, Integer> given = new HashMap<String, Integer>();
		
		List<String> orden = new ArrayList<String>();
		
		sc.nextLine();
		
		for (int i = 0; i <np; i++) {
			String name = sc.nextLine();
			orden.add(name);
			recived.put(name, 0);
			given.put(name, 0);
		}
		
		for (int i = 0; i < np; i++) {
			
			String name = sc.nextLine();
			
			int gonnaGive =sc.nextInt(),people = sc.nextInt();
			
			int givePerPeople = (people == 0)?0:gonnaGive/people;
			
			int rest = gonnaGive - (givePerPeople*people);
			
			recived.put(name, recived.get(name) + rest);
			
			given.put(name, gonnaGive);
			
			sc.nextLine();
			
			for (int j = 0; j < people; j++) {
				String giveme = sc.nextLine();
//				System.out.println(giveme);
				recived.put(giveme, recived.get(giveme) + givePerPeople);
				
			}
			
			
		}
		
		
		
		for (String person : orden) {
			
			int recibido = recived.get(person);
			
			int dado = given.get(person);
			
			System.out.println(person+" "+(recibido-dado));
			
		}
		
	}

}
