import java.util.Scanner;
public class solution
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		String directs = new String();
		long n = sc.nextLong();
		int mod;
		String step;
		while(n > 1)
		{
			mod = (int) Math.floorMod(n,3);
			//mod = (int) n % 3;
			n = (n + 1) / 3;
			if(mod == 0)
			{
				step = "M";
			}
			else if(mod == 1)
			{
				step = "R";
			}
			else//2
			{
				step = "L";
			}

			directs = step + directs;
		}
		System.out.println(directs);
	}
}
