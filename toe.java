	enum Dir {
			NONE,
			VERT,
			HORIZ,
			DIAG;
	}	

public class toe {

	public static int checker(char[][] arr, int m) {
		int n = arr.length;
		int row1 =0;
		int col1=0;
		int row2=0;
		int col2=0;
		Dir dir = Dir.NONE;
		
		for(int i = 0; i <= n-m; i++ ) {
			int beg = i;
			int end = m -1 + i;

			if (arr[beg][beg] == 'x'  && arr[beg][end] == 'x')  {
				row1 = beg;
				col1 = beg +1;
				row2 = beg;
				col2 = end -1 ; 
				dir = Dir.HORIZ;
			} else if (arr[beg][beg] == 'x'  && arr[end][beg] == 'x')  {
				row1 = beg +1;
				col1 = beg;
				row2 = end -1;
				col2 = beg; 
				dir = Dir.VERT;
			} else if (arr[beg][beg] == 'x'  && arr[end][end] == 'x')  {
				row1 = beg +1;
				col1 = beg +1;
				row2 = end -1;
				col2 = end -1 ; 
				dir = Dir.DIAG;
			}else{ dir = Dir.NONE; }

			while(  dir != Dir.NONE && 
				  	arr[row1][col1] == 'x' &&
				  	arr[row2][col2] == 'x'	 )
			{
				if(row1 - row2 <= 1 || row1 - row2 <= 1) return 1;
				
				switch (dir) {
					case VERT: 
						row1 = beg +1;
						row2 = end -1;
								break;

					case HORIZ: 
						row1 = beg +1;
						row2 = end -1;
								break;

					case DIAG: 
						row1 = beg +1;
						col1 = beg +1;
						row2 = end -1;
						col2 = end -1; 
						break;
				}
			}
			dir = Dir.NONE;
		}
		return 0;

	}

	public static void printer (char[][] arr ) {
		for (int i=0; i < arr.length; i++) {
			for (int j=0; j < arr[i].length; j++) {
				System.out.print(" " + arr[i][j]);
			}
			System.out.println();
		}

	}

	public static void main (String [] args ) {
		char[][] arr = new char[][]{ 
			{'x','x','x','x'}, 
			{'o','o','o','o'},
			{'o','o','o','o'},
			{'o','o','o','o'} };

		char[][] arr2 = new char[][]{ 
			{'x','x','x','x','x'}, 
			{'o','o','o','o', 'o'},
			{'o','o','o','o', 'o'},
			{'o','o','o','o', 'o'},
			{'o','o','o','o', 'o'} };
		char[][] arr3 = new char[][]{ 
			{'o','o','o','o','o'}, 
			{'o','x','o','o', 'o'},
			{'o','o','x','o', 'o'},
			{'o','o','o','x', 'o'},
			{'o','o','o','o', 'x'} };

		char[][] arr4 = new char[][]{ 
			{'x','o','o','o','o'}, 
			{'x','x','o','o', 'o'},
			{'x','o','x','o', 'o'},
			{'x','o','o','o', 'o'},
			{'x','o','o','o', 'o'} };
		System.out.println(checker(arr, 4));
		System.out.println(checker(arr, 3));
		System.out.println(checker(arr2, 5));
		System.out.println(checker(arr2, 4));
		System.out.println(checker(arr3, 5));
		System.out.println(checker(arr3, 4));
		System.out.println(checker(arr4, 5));
		System.out.println(checker(arr4, 4));
		//printer(arr);

	}

}
