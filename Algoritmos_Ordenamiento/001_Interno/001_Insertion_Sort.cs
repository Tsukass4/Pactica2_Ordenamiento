using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CommonInsertion_Sort
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create an array of integers for sorting
            int[] numbers = new int[10] { 2, 5, -4, 11, 0, 18, 22, 67, 51, 6 };

            // Display original array elements
            Console.WriteLine("\nOriginal Array Elements :");
            PrintIntegerArray(numbers);

            // Perform Insertion Sort and display the sorted array elements
            Console.WriteLine("\nSorted Array Elements :");
            PrintIntegerArray(InsertionSort(numbers));
            Console.WriteLine("\n");
        }

        // Method implementing Insertion Sort algorithm
        static int[] InsertionSort(int[] inputArray)
        {
            for (int i = 0; i < inputArray.Length - 1; i++)
            {
                for (int j = i + 1; j > 0; j--)
                {
                    // Swap if the element at j - 1 position is greater than the element at j position
                    if (inputArray[j - 1] > inputArray[j])
                    {
                        int temp = inputArray[j - 1];
                        inputArray[j - 1] = inputArray[j];
                        inputArray[j] = temp;
                    }
                }
            }
            return inputArray; // Return the sorted array
        }

        // Method to print integer array elements
        public static void PrintIntegerArray(int[] array)
        {
            foreach (int i in array)
            {
                Console.Write(i.ToString() + "  "); // Display each element followed by a space
            }
        }
    }
}