public class QuadraticFormula
{
    public static double quadPlus(double a, double b, double c) {
        return (-1*b)+Math.sqrt(((b*b) -4*a*c) / (2*a));
    }

    public static double quadMinus(double a, double b, double c) {
        return (-1*b)-Math.sqrt(((b*b) -4*a*c) / (2*a));
    }
}