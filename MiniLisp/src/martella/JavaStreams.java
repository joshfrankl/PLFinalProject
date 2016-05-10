package src.martella;

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
        ArrayList<Attendance> attend = new ArrayList<Attendance>();
        ArrayList<Stadiums> stad = new ArrayList<Stadiums>();

        String path = System.getProperty("user.dir") + "/src/";

        File file = new File(path + "mls-attendance.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String line;

        while ((line = br.readLine()) != null){
            String a = line.substring(1, line.length() - 2);
            List<String> mlsList = Arrays.asList(a.split(","));
            for (int i = 0;i<mlsList.size();i++){
                mlsList.set(i,mlsList.get(i).trim());
            }
            mlsList.get(0);
            Attendance at = new Attendance(Integer.parseInt(mlsList.get(0)),mlsList.get(1),mlsList.get(2),mlsList.get(3),mlsList.get(4),mlsList.get(5),mlsList.get(6),mlsList.get(7),mlsList.get(8),mlsList.get(9),mlsList.get(10),mlsList.get(11),mlsList.get(12), mlsList.get(12));
            attend.add(at);
        }

        br = new BufferedReader(new FileReader(path + "mls-stadiums.txt"));
        while ((line = br.readLine()) != null){
            String a = line.substring(1, line.length() - 2);
            List<String> mlsList = Arrays.asList(a.split(","));
            for (int i = 0;i<mlsList.size();i++){
                mlsList.set(i,mlsList.get(i).trim());
            }
            mlsList.get(0);
            Stadiums s = new Stadiums(Integer.parseInt(mlsList.get(0)),mlsList.get(1),mlsList.get(2),mlsList.get(3),mlsList.get(4),Integer.parseInt(mlsList.get(5)));
            stad.add(s);
        }

        System.out.println(Arrays.toString(attend.toArray()));
        System.out.println(Arrays.toString(stad.toArray()));

        System.out.println();
        System.out.println();

        attend.stream()
                .collect(Collectors.groupingBy(Attendance::getGameId))
                .entrySet() // this converts map into set that can be streamed
                // e.g. {0:[e1,e2,...],1:[e3,e4,....],...}
                .stream()
                .map(kv -> kv.getValue())
                // this results in a streamed list
                .forEach((l) -> {
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
