public class Day2
{
    public static void Missing()
    {
        int arr [] = {1,2,3,5};
    

        for (int i = 0; i < arr.length-1; i++) {
            if(arr[i+1]!=1+arr[i])
            {
                System.out.println("Missing number is :"+(arr[i]+1));
            }

        }
    }
    public static void main(String[] args)
     {
       Missing();
    }
}