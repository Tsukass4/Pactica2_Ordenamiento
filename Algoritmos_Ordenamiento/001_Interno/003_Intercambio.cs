using System;

public class GFG {

    // Function for Exchange sort in Ascending order
    static void exchangeSort(int[] num, int size)
    {
        int i, j, temp;
        for (i = 0; i < size - 1; i++) {

            // Outer Loop
            for (j = i + 1; j < size; j++) {

                // Inner Loop
                // Sorting into ascending order if previous
                // element bigger than next element we swap
                // to make it in ascending order
                if (num[i] > num[j]) {

                    // Swapping
                    temp = num[i];
                    num[i] = num[j];
                    num[j] = temp;
                }
            }
        }
    }

    static public void Main()
    {

        // Code
        int[] arr = { 5, 1, 4, 2, 8 };

        // Function call
        exchangeSort(arr, 5);
        foreach(int i in arr) { Console.Write(i + " "); }
    }
}
