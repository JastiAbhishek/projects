import java.util.*;
import java.io.*;

//EnemyGenerator.java - Abhishek Jasti
/** Factory to create random enemies to encounter on the map */

public class EnemyGenerator{
    /** representation of all enemies */
    private HashMap<String, Integer> enemies = new HashMap<String, Integer>();

    /** reads the file and adds the different enemies and their base hp to the hash map */
    public EnemyGenerator(){
        try{
            Scanner read = new Scanner(new File("Enemies.txt"));
            String[] w;
            String word;
            int hp;
            while(read.hasNextLine()){
                word = read.nextLine();
                w = word.split(",");
                word = w[0];
                hp = Integer.valueOf(w[1]);
                enemies.put(word, hp);
            }
        }
        catch(FileNotFoundException fnf){
            System.out.println("File Not Found!!");
        }
    }

    /** randomly selects an enemy from the map, then randomly selects an ablity type
     *  @param level represents the level the hero is on
     *  @return an enemy
     */
    public Enemy generateEnemy(int level){
        Set <String> keys = enemies.keySet();
        String[] key = keys.toArray(new String[0]);
        int r1 = (int)((Math.random()*enemies.size()-1)+1);
        int r2 = (int)((Math.random()*3)+1);
        if(r2 == 1){
            return new Warrior(key[r1]+" Warroir", enemies.get(key[r1])+(level-1*2));
        }
        else if(r2 == 2){
            return new Wizard(key[r1]+" Wizard", enemies.get(key[r1])+(level*2));
        }
        return new Ranger(key[r1]+" Ranger", enemies.get(key[r1])+(level*2));
    }

}
/** 
*Enemies*
Goblin, 2
Orc, 4
Giant Rat, 1
Kobold, 4
Gnoll, 3
Snake, 1
Froglok, 2
Troll, 5
*/

