namespace DayFour
{
    internal class Program
    {
        static void Main(string[] args)
        {
            part1();
            part2();
        }

        public static void part1()
        {
            string filePath = "input.txt";

            string[] lines = File.ReadAllLines(filePath);

            int rows = lines.Length;
            int columns = lines[0].Length;
            int total = 0;
            char[,] data = new char[rows, columns];


            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < columns; j++)
                {
                    data[i, j] = lines[i][j];
                }
            }

            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < columns; j++)
                {
                    // Horizontal normal
                    if (data[i, j] == 'X' && (j <= columns - 4))
                    {
                        if (data[i, j + 1] == 'M' && data[i, j + 2] == 'A' && data[i, j + 3] == 'S')
                        {
                            total++;
                        }
                    }
                    // Horizontal backwards
                    if (data[i, j] == 'X' && (j >= 3))
                    {
                        if (data[i, j - 1] == 'M' && data[i, j - 2] == 'A' && data[i, j - 3] == 'S')
                        {
                            total++;
                        }
                    }
                    // Vertical normal
                    if (data[i, j] == 'X' && (i <= rows - 4))
                    {
                        if (data[i + 1, j] == 'M' && data[i + 2, j] == 'A' && data[i + 3, j] == 'S')
                        {
                            total++;
                        }
                    }
                    // Vertical backwards
                    if (data[i, j] == 'X' && (i >= 3))
                    {
                        if (data[i - 1, j] == 'M' && data[i - 2, j] == 'A' && data[i - 3, j] == 'S')
                        {
                            total++;
                        }
                    }
                    // Diagonal NW -> SE
                    if (data[i, j] == 'X' && (i <= rows - 4) && (j <= columns - 4))
                    {
                        if (data[i + 1, j + 1] == 'M' && data[i + 2, j + 2] == 'A' && data[i + 3, j + 3] == 'S')
                        {
                            total++;
                        }
                    }
                    // Diagnoal SE -> NW
                    if (data[i, j] == 'X' && (i >= 3) && (j >= 3))
                    {
                        if (data[i - 1, j - 1] == 'M' && data[i - 2, j - 2] == 'A' && data[i - 3, j - 3] == 'S')
                        {
                            total++;
                        }
                    }
                    // Diagonal NE -> SW
                    if (data[i, j] == 'X' && (i <= rows - 4) && (j >= 3))
                    {
                        if (data[i + 1, j - 1] == 'M' && data[i + 2, j - 2] == 'A' && data[i + 3, j - 3] == 'S')
                        {
                            total++;
                        }
                    }
                    // Diagonal SW -> NE
                    if (data[i, j] == 'X' && (i >= 3) && (j <= columns - 4))
                    {
                        if (data[i - 1, j + 1] == 'M' && data[i - 2, j + 2] == 'A' && data[i - 3, j + 3] == 'S')
                        {
                            total++;
                        }
                    }
                }
            }

            Console.WriteLine(total);
        }

        public static void part2()
        {
            string filePath = "input.txt";

            string[] lines = File.ReadAllLines(filePath);

            int rows = lines.Length;
            int columns = lines[0].Length;
            int counter = 0;
            int total = 0;
            char[,] data = new char[rows, columns];


            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < columns; j++)
                {
                    data[i, j] = lines[i][j];
                }
            }

            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < columns; j++)
                {
                    counter = 0;
                    if (data[i, j] == 'A' && (i != 0 && i != rows - 1) && (j != 0 && j != columns - 1))
                    {
                        // NW
                        if (data[i - 1, j - 1] == 'M')
                        {
                            // SE
                            if (data[i + 1, j + 1] == 'S')
                            {
                                counter++;
                            }
                        }
                        // NW
                        else if (data[i - 1, j - 1] == 'S')
                        {
                            // SE
                            if (data[i + 1, j + 1] == 'M')
                            {
                                counter++;
                            }
                        }

                        // NE
                        if (data[i - 1, j + 1] == 'M')
                        {
                            //SW
                            if (data[i + 1, j - 1] == 'S')
                            {
                                counter++;
                            }
                        }
                        // NE
                        else if (data[i - 1, j + 1] == 'S')
                        {
                            if (data[i + 1, j - 1] == 'M')
                            {
                                counter++;
                            }
                        }
                    }

                    if (counter == 2)
                    {
                        total++;
                    }
                }

            }

            Console.WriteLine(total);
        }
    }
}
