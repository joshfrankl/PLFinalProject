package martella;

/**
 * Created by jacobmartella on 5/9/16.
 */
public class Stadiums {
    private int stadium_id;
    private String stadium_name;
    private String team_name;
    private String city;
    private String state;
    private int capacity;

    public Stadiums(int stadium_id, String stadium_name, String team_name, String city, String state, int capacity) {
        this.stadium_id = stadium_id;
        this.stadium_name = stadium_name;
        this.team_name = team_name;
        this.city = city;
        this.state = state;
        this.capacity = capacity;
    }

    public int getStadiumId() {
        return stadium_id;
    }

    public String getStadiumName() {
        return stadium_name;
    }

    public String getTeamName() {
        return team_name;
    }

    public String getCity() {
        return city;
    }

    public String getState() {
        return state;
    }

    public int getCapacity() {
        return capacity;
    }

}
