package prob3;

public class PrimeCompositeNumber {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		double target = 600851475143.0;
		boolean stop = false;
		while (stop == false)
		{
			double j = 2;
			if (fermat(j) == true)
			{
				double result = target / j;
				if (result < 0.000001)
					
			}
			
		}
		

	}
	
	public static boolean fermat(double p)
	{
		int prod = 0;
		for (int i = 0; i < p; i++)
		{
			prod *= p;
		}
		
		if (prod % p == 0)
		{
			return true;
		}
		
		else
		{
			return false;
		}
		
		//A^p-A divs P
	}

}
