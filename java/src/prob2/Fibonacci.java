package prob2;

public class Fibonacci {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		int fsum = 2;
		int sum = 2;
		int fib1 = 1;
		int fib2 = 2;
		
		while (fsum <= 4000000)
		{
			fsum = fib1 + fib2;
			fib1 = fib2;
			fib2 = fsum;
			
			if (fsum%2 == 0)
			{
				sum += fsum;
			}
		}
		
		
		System.out.println(sum);


	}

}
