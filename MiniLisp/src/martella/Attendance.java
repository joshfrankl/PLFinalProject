package src.martella;

/**
 * Created by jacobmartella on 5/9/16.
 */
public class Attendance {
    private int game_id;
    private String stadium_id;
    private String full_date;
    private String day_of_week;
    private String home_team;
    private String away_team;
    private String attendance;
    private String max_temp;
    private String mean_temp;
    private String min_temp;
    private String year;
    private String month;
    private String day;
    private String url;

    public Attendance(int game_id, String stadium_id, String full_date, String day_of_week, String home_team, String away_team, String attendance, String max_temp, String mean_temp, String min_temp, String year, String month, String day, String url) {
        this.game_id = game_id;
        this.stadium_id = stadium_id;
        this.full_date = full_date;
        this.day_of_week = day_of_week;
        this.home_team = home_team;
        this.away_team = away_team;
        this.attendance = attendance;
        this.max_temp = max_temp;
        this.mean_temp = mean_temp;
        this.min_temp = min_temp;
        this.year = year;
        this.day = day;
        this.month = month;
        this.url = url;
    }

    public int getGameId() {
        return game_id;
    }

    public String getStadiumId() {
        return stadium_id;
    }

    public String getFullDate() {
        return full_date;
    }

    public String getDayOfWeek() {
        return day_of_week;
    }

    public String getHomeTeam() {
        return home_team;
    }

    public String getAwayTeam() {
        return away_team;
    }

    public String getAttendance() {
        return attendance;
    }

    public String getMaxTemp() {
        return max_temp;
    }

    public String getMeanTemp() {
        return mean_temp;
    }

    public String getMinTemp() {
        return min_temp;
    }

    public String getYear() {
        return year;
    }

    public String getMonth() {
        return month;
    }

    public String getday() {
        return day;
    }

    public String getUrl() {
        return url;
    }
}
