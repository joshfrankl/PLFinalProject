package martella;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Created by jacobmartella on 5/9/16.
 */
public class JavaStreams {
    public static void main(String[] args) throws IOException {
        ArrayList<Attendance> attend = new ArrayList<>();
        ArrayList<Stadiums> stad = new ArrayList<>();

        String path = System.getProperty("user.dir") + "/src/";

        File file = new File(path + "mls-attendance.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String line;

        while ((line = br.readLine()) != null){
            String a = line.substring(1, line.length() - 2);
            List<String> empList = Arrays.asList(a.split(","));
            for (int i = 0;i<empList.size();i++){
                empList.set(i,empList.get(i).trim());
            }
            empList.get(0);
            Attendance at = new Attendance(Integer.parseInt(empList.get(0)),empList.get(1),empList.get(2),empList.get(3),empList.get(4),empList.get(5),empList.get(6),empList.get(7),empList.get(8),empList.get(9),empList.get(10),empList.get(11),empList.get(12), empList.get(12));
            attend.add(at);
        }

        br = new BufferedReader(new FileReader(path + "mls-stadiums.txt"));
        while ((line = br.readLine()) != null){
            String a = line.substring(1, line.length() - 2);
            List<String> empList = Arrays.asList(a.split(","));
            for (int i = 0;i<empList.size();i++){
                empList.set(i,empList.get(i).trim());
            }
            empList.get(0);
            Stadiums s = new Stadiums(Integer.parseInt(empList.get(0)),empList.get(1),empList.get(2),empList.get(3),empList.get(4),Integer.parseInt(empList.get(5)));
            stad.add(s);
        }

        System.out.println(Arrays.toString(attend.toArray()));
        System.out.println(Arrays.toString(stad.toArray()));

        // SELECT first_name, last_name, manager_id, salary FROM emp GROUP BY manager_id ORDER BY salary
        System.out.println("\nSELECT first_name, last_name, manager_id, salary FROM emp GROUP BY manager_id ORDER BY salary");
        attend.stream()
                .collect(Collectors.groupingBy(Attendance::getGameId)) // This creates a map with the key of dept_id and value list of employees for that dept_id
                .entrySet() // this converts map into set that can be streamed
                // e.g. {0:[e1,e2,...],1:[e3,e4,....],...}
                .stream()
                .map(kv -> kv.getValue())
                // this results in a streamed list of employees
                // l = [e1,e2,..]
                .forEach((l) -> {
                    // l = [e1,e2,...] from a given manager id
                    l.stream()
                            .sorted((e1, e2) -> e1.getAttendance()
                                    .compareTo(e2.getAttendance()))
                            .forEach(e -> {
                                String toPrint = e.getHomeTeam() + " " + e.getAwayTeam() + " " + e.getStadiumId() + " " + e.getAttendance();
                                System.out.println(toPrint);
                            });
                });

    }

}
