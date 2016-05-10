import java.util.*;
import java.util.stream.Collectors;

public class ListComprehension {
    public static void executeStreams() {
        ArrayList<List<Object>> emp = new ArrayList<List<Object>>();
        List<Object> headers = Arrays.asList("ID", "LAST_NAME", "FIRST_NAME","USERID","START_DATE","COMMENTS","TITLE","SALARY","COMMISSION","DEPT_ID","MANAGER_ID");
        List<Object> e1 = Arrays.asList(1, "Martin", "Carmen", "martincu", "03-MAY-90", "", "President", 4500, "", 50, "");
        List<Object> e2 = Arrays.asList(10, "Jackson", "Marta", "jacksomt", "27-FEB-91", "", "Warehouse Manager", 1507, 0, 45, 2);
        List<Object> e3 = Arrays.asList(11, "Henderson", "Colin", "hendercs", "14-MAY-90", "", "Sales Representative", 1400, 10, 31, 3);
        List<Object> e4 = Arrays.asList(12, "Gilson", "Sam", "gilsonsj", "18-JAN-92", "", "Sales Representative", 1490, 12.5, 32, 3);
        List<Object> e5 = Arrays.asList(13, "Sanders", "Jason", "sanderjk", "18-FEB-91", "", "Sales Representative", 1515, 10, 33, 3);
        List<Object> e6 = Arrays.asList(14, "Dameron", "Andre", "dameroap", "09-OCT-91", "", "Sales Representative", 1450, 17.5, 35, 3);
        List<Object> e7 = Arrays.asList(15, "Hardwick", "Elaine", "hardwiem", "07-FEB-92", "", "Stock Clerk", 1400, "", 41, 6);
        List<Object> e8 = Arrays.asList(16, "Brown", "George", "browngw", "08-MAR-90", "", "Stock Clerk", 940, "", 41, 6);
        List<Object> e9 = Arrays.asList(17, "Washington", "Thomas", "washintl", "09-FEB-91", "", "Stock Clerk", 1200, "", 42, 7);
        List<Object> e10 = Arrays.asList(18, "Patterson", "Donald", "patterdv", "06-AUG-91", "", "Stock Clerk", 795, "", 42, 7);
        List<Object> e11 = Arrays.asList(19, "Bell", "Alexander", "bellag", "26-MAY-91", "", "Stock Clerk", 850, "", 43, 8);
        List<Object> e12 = Arrays.asList(2, "Smith", "Doris", "smithdj", "08-MAR-90", "", "VP, Operations", 2450, "", 41, 1);
        List<Object> e13 = Arrays.asList(20, "Gantos", "Eddie", "gantosej", "30-NOV-90", "", "Stock Clerk", 800, "", 44, 9);
        List<Object> e14 = Arrays.asList(21, "Stephenson", "Blaine", "stephebs", "17-MAR-91", "", "Stock Clerk", 860, "", 45, 10);
        List<Object> e15 = Arrays.asList(22, "Chester", "Eddie", "chesteek", "30-NOV-90", "", "Stock Clerk", 800, "", 44, 9);
        List<Object> e16 = Arrays.asList(23, "Pearl", "Roger", "pearlrg", "17-OCT-90", "", "Stock Clerk", 795, "", 34, 9);
        List<Object> e17 = Arrays.asList(24, "Dancer", "Bonnie", "dancerbw", "17-MAR-91", "", "Stock Clerk", 860, "", 45, 7);
        List<Object> e18 = Arrays.asList(25, "Schmitt", "Sandra", "schmitss", "09-MAY-91", "", "Stock Clerk", 1100, "", 45, 8);
        List<Object> e19 = Arrays.asList(3, "Norton", "Michael", "nortonma", "17-JUN-91", "", "VP, Sales", 2400, "", 31, 1);
        List<Object> e20 = Arrays.asList(4, "Quentin", "Mark", "quentiml", "07-APR-90", "", "VP, Finance", 2450, "", 10, 1);
        List<Object> e21 = Arrays.asList(5, "Roper", "Joseph", "roperjm", "04-MAR-90", "", "VP, Administration", 2550, "", 50, 1);
        List<Object> e22 = Arrays.asList(6, "Brown", "Molly", "brownmr", "18-JAN-91", "", "Warehouse Manager", 1600, "", 41, 2);
        List<Object> e23 = Arrays.asList(7, "Hawkins", "Roberta", "hawkinrt", "14-MAY-90", "", "Warehouse Manager", 1650, "", 42, 2);
        List<Object> e24 = Arrays.asList(8, "Burns", "Ben", "burnsba", "07-APR-90", "", "Warehouse Manager", 1500, "", 43, 2);
        List<Object> e25 = Arrays.asList(9, "Catskill", "Antoinette", "catskiaw", "09-FEB-92", "", "Warehouse Manager", 1700, "", 44, 2);

        emp.add(headers);emp.add(headers); emp.add(e1); emp.add(e2); emp.add(e3); emp.add(e4); emp.add(e5); emp.add(e6); emp.add(e7); emp.add(e8);
        emp.add(e9); emp.add(e10); emp.add(e11); emp.add(e12); emp.add(e13); emp.add(e14); emp.add(e15); emp.add(e16);
        emp.add(e17); emp.add(e18); emp.add(e19); emp.add(e20); emp.add(e21); emp.add(e22); emp.add(e23); emp.add(e24);
        emp.add(e25);

        System.out.println();

        // select * from emp;
        System.out.println("select * from emp;");
        emp.stream().filter(e -> emp.indexOf(e) > 0).forEach(e -> {System.out.println(e);});

        System.out.println();

        // select * from emp where salary > 1500;
        System.out.println("select * from emp where salary > 1500;");
        emp.stream().filter(e -> emp.indexOf(e) > 0 && Integer.parseInt(e.get(7).toString()) > 1500).forEach(e -> {System.out.println(e);});

        System.out.println();

        // select * from emp where salary > 1500 order by salary;
        System.out.println("select * from emp where salary > 1500 order by salary;");
        emp.stream().filter(e -> emp.indexOf(e) > 0 && Integer.parseInt(e.get(7).toString()) > 1500).sorted((emp1, emp2) -> Integer.compare(Integer.parseInt(emp1.get(7).toString()), Integer.parseInt(emp2.get(7).toString()))).forEach(e -> {System.out.println(e);});

        System.out.println();

        // select * from emp where salary > 1500 and id > 12;
        System.out.println("select * from emp where salary > 1500 and id > 12;");
        emp.stream().filter(e -> emp.indexOf(e) > 0 && Integer.parseInt(e.get(7).toString()) > 1500 && Integer.parseInt(e.get(0).toString()) > 12).forEach(e -> {System.out.println(e);});

        System.out.println();

        // select dept_id, avg(salary) from emp group by dept_id;
        System.out.println("select dept_id, avg(salary) from emp group by dept_id;");
        emp.stream().filter(e -> emp.indexOf(e) > 0).collect(Collectors.groupingBy(e -> e.get(9).toString())).entrySet().stream().map(kv -> kv.getValue())
                .forEach(employeeList -> {
                    double averageSalary = employeeList.stream().mapToDouble(e -> Double.parseDouble(e.get(7).toString())).average().getAsDouble();
                    String dept_id = employeeList.get(0).get(9).toString();
                    System.out.println(dept_id + " " + averageSalary);
                });

        System.out.println();

        // select distinct dept_id from emp order by dept_id;
        System.out.println("select distinct dept_id from emp order by dept_id;");
        emp.stream().filter(e -> emp.indexOf(e) > 0).map(e -> Integer.parseInt(e.get(9).toString())).distinct().sorted((dept1, dept2) -> Integer.compare(dept1, dept2)).forEach(e -> {System.out.println(e);});

    }
}
