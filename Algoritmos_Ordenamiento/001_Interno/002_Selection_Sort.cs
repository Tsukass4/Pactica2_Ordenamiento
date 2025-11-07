using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Selection_Sort
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create an instance of the Selection_Sort class with an array of 10 random numbers
            Selection_Sort selection = new Selection_Sort(10);

            // Call the Sort method of the Selection_Sort class to perform selection sort
            selection.Sort();
        }
    }

    class Selection_Sort
    {
        private int[] data;
        private static Random generator = new Random();

        // Constructor to create an array of specified size filled with random numbers
        public Selection_Sort(int size)
        {
            data = new int[size];

            // Fill the array with random numbers between 20 and 90
            for (int i = 0; i < size; i++)
            {
                data[i] = generator.Next(20, 90);
            }
        }

        // Method to perform selection sort
        public void Sort()
        {
            // Display the original array elements before sorting
            Console.Write("\nSorted Array Elements :(Step by Step)\n\n");
            display_array_elements();

            int smallest;

            // Iterate through the array to perform selection sort
            for (int i = 0; i < data.Length - 1; i++)
            {
                smallest = i;

                // Find the index of the smallest element in the unsorted part of the array
                for (int index = i + 1; index < data.Length; index++)
                {
                    if (data[index] < data[smallest])
                    {
                        smallest = index;
                    }
                }

                // Swap the current element with the smallest element found
                Swap(i, smallest);

                // Display array elements after each swap (step-by-step)
                display_array_elements();
            }
        }

        // Method to swap two elements in the array
        public void Swap(int first, int second)
        {
            int temporary = data[first];
            data[first] = data[second];
            data[second] = temporary;
        }

        // Method to display array elements
        public void display_array_elements()
        {
            // Display each element of the array
            foreach (var element in data)
            {
                Console.Write(element + " ");
            }
            Console.Write("\n\n");
        }
    }
}