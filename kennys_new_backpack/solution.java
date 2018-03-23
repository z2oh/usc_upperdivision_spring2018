import java.util.Scanner;
import java.util.ArrayList;
import java.lang.Math;
//import java.lang.Math.pow;
public class solution
{
public static final int MAX_SIZE = 40;
public static final int BASE = 3;
public static ArrayList<Character> DIRECTIONS = new ArrayList<Character>(MAX_SIZE);
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int sum = 1;
		int level = 1;
		while(n > sum)
		{
			sum += (int) Math.pow(BASE, level++);
		}

		int index = n - (sum - (int) Math.pow(BASE, (level -1)));

		while(level-- > 1)
		{
			add_direction(index % BASE);
			index = (int) Math.ceil(index / BASE);
		}
		
		for(int i = DIRECTIONS.size()-1; i >-1; i--)
		{
			System.out.print(DIRECTIONS.get(i));
		}
		System.out.println();
	}

	public static void add_direction(int direct)
	{
		if(direct == 0)
		{
			DIRECTIONS.add('R');
		}
		else if(direct == 1)
		{
			DIRECTIONS.add('L');
		}
		else//2
		{
			DIRECTIONS.add('M');
		}
	}

}
