public class Imaginary
{
    public static String sqrt(int i) {
        if (i < 0) {
            return Math.sqrt(Math.abs(i)) + "i";
        }
        return Double.toString(Math.sqrt(i));
    }

    public static String sqrt(double i) {
        if (i < 0) {
            return Math.sqrt(Math.abs(i)) + "i";
        }
        return Double.toString(Math.sqrt(i));
    }
}