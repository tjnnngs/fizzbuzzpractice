private static void TrianglePrint()
    {
        for (int i = 0; i < 10; i++)
        {
            System.out.print(" * ");
            for (int j = 0; j < 10; j++)
            {                   
                if(j<i)
                    System.out.print(" * ");
                else
                    System.out.print("   ");            }
            System.out.println("");
        }
        System.out.println("");
    }