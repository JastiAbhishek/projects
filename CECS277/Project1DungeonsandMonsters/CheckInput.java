import java.util.Scanner;


public class CheckInput {
		
		public static int getInt() {
		Scanner in = new Scanner( System.in );
		int input = 0;
		boolean valid = false;
		while( !valid ) {
			if( in.hasNextInt() ) {
				input = in.nextInt();
				valid = true;
			} else {
				in.next(); //clear invalid string
				System.out.println( "Invalid Input." );
			}
		}
		return input;
	}
	
	/**
	 * Checks if the inputted value is an integer and 
	 * within the specified range (ex: 1-10)
	 * @param low lower bound of the range.
	 * @param high upper bound of the range.
	 * @return the valid input.
	 */
	public static int getIntRange( int low, int high ) {
		Scanner in = new Scanner( System.in );
		int input = 0;
		boolean valid = false;
		while( !valid ) {
			if( in.hasNextInt() ) {
				input = in.nextInt();
				if( input <= high && input >= low ) {
					valid = true;
				} else {
					System.out.println( "Invalid Range." );
				}
			} else {
				in.next(); //clear invalid string
				System.out.println( "Invalid Input." );
			}
		}
		return input;
	}
	/**
	 * Checks if the inputted value is a non-negative integer.
	 * @return the valid input.
	 */
	public static int getPositiveInt( ) {
		Scanner in = new Scanner( System.in );
		int input = 0;
		boolean valid = false;
		while( !valid ) {
			if( in.hasNextInt() ) {
				input = in.nextInt();
				if( input >= 0 ) {
					valid = true;
				} else {
					System.out.println( "Invalid Range." );
				}
			} else {
				in.next(); //clear invalid string
				System.out.println( "Invalid Input." );
			}
		}
		return input;
	}

	/**
	 * Checks if the inputted value is a double.
	 * @return the valid input.
	 */
	public static double getDouble() {
		Scanner in = new Scanner( System.in );
		double input = 0;
		boolean valid = false;
		while( !valid ) {
			if( in.hasNextDouble() ) {
				input = in.nextDouble();
				valid = true;
			} else {
				in.next(); //clear invalid string
				System.out.println( "Invalid Input." );
			}
		}
		return input;
	}
	
	/**
	 * Takes in a string from the user.
	 * @return the inputted String.
	 */
	public static String getString() {
		Scanner in = new Scanner( System.in );
		String input = in.nextLine();
		return input;
	}

	/**
	 * Takes in a yes/no from the user.
	 * @return true if yes, false if no.
	 */
	public static boolean getYesNo(){
		boolean valid = false;
		while( !valid ) {
			String s = getString();
			if( s.equalsIgnoreCase("yes") || s.equalsIgnoreCase("Y") ) {
				return true;
			} else if( s.equalsIgnoreCase("no") || s.equalsIgnoreCase("N") ) {
				return false;
			} else {
				System.out.println( "Invalid Input." );
			}
		}
		return false;
	}	
}
