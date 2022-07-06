import java.awt.*;
// Hero.java - Anand Jasti

/** Hero class describes the character that represents the user */
public class Hero extends Entity implements Fighter, Magical, Archer{

  /** represents the location of the Hero on the map */
  private Point loc;

  /** represents what level of the map the hero is on */
  private int level;

  /** represents how much gold the hero has */
  private int gold;

  /** represents how many keys the hero has */
  private int keys;

  /** represents how many potions the hero has */
  private int potions;

  // /** represents the map */
  // public Map m = new Map();

  /** Initializes the Hero class with name, level, hp, gold, potions, and keys
   *  @param n the name of the hero 
   */
  public Hero(String n){
    super(n, 25);
    Map m = Map.getInstance();
    level = 1;
    gold = 25;
    keys = 0;
    potions = 1;
    m.loadMap(level);
    loc = m.findStart();
  }

  /** String representation of the Hero 
   *  @return string representation of the Hero
   */
  @Override
  public String toString(){
    Map m = Map.getInstance();
    return super.toString() + "\nLevel: " + level + "\nGold: " + gold + "\nP: " + potions + " K: " + keys+ "\n"+m.mapToString(loc);
  }

  /** Gets the heros location
   *  @return the location of the hero
   */
  public Point getLocation(){
    return loc;
  }

  /** This method increments the Hero's level and loads the next map */
  public void levelUp(){
    level++;
    Map m = Map.getInstance();
    m.loadMap(level);
  }

  /** Gets the hero's level
   *  @return the hero's level
   */
  public int getLevel(){
    return level;
  }

  /** Updates the hero's location to the North
   *  @return the character at the new location
   */
  public char goNorth(){
    Map m = Map.getInstance();
    if(loc.getX()>0){
      loc.setLocation(loc.getX()-1, loc.getY());
      m.reveal(loc);
      return m.getCharAtLoc(loc);
    }
    return 'x';
  }

  /** Updates the hero's location to the South
   *  @return the character at the new location
   */
  public char goSouth(){
    Map m = Map.getInstance();
    if(loc.getX()<4){
      loc.setLocation(loc.getX()+1, loc.getY());
      m.reveal(loc);
      return m.getCharAtLoc(loc);
    }
    return 'x';
  }

  /** Updates the hero's location to the East
   *  @return the character at the new location
   */
  public char goEast(){
    Map m = Map.getInstance();
    if(loc.getY()>0){
      loc.setLocation(loc.getX(), loc.getY()-1);
      m.reveal(loc);
      return m.getCharAtLoc(loc);
    }
    return 'x';
  }
  /** Updates the hero's location to the West
   *  @return the character at the new location
   */
  public char goWest(){
    Map m = Map.getInstance();
    if(loc.getY()<4){
      loc.setLocation(loc.getX(), loc.getY()+1);
      m.reveal(loc);
      return m.getCharAtLoc(loc);
    }
    return 'x';
  }

  /** Make Attack menu
   *  @return String representation of the Attack menu
   */
  public String getAttackMenue(){
    return "1.Physical\n2.Magical\n3.Ranged";
  }

  /** @return the number of items in the Attack menu */
  public int getNumAttackMenuItems(){
    return 3;
  }
  
  /** @param choice represents the users choice for attack
   *  @return String representation of the SubAttack menu
   */
  public String getSubAttackMenue(int choice){
    if(choice==1){
      return Fighter.FIGHTER_MENU;
    }
    else if(choice==2){
      return Magical.MAGIC_MENU;
    }
    else{
      return Ranger.ARCHER_MENU;
    }
  }

  /** @param choice represents the users choice for attack
   *  @return the number of items in the subAttack menu */
  public int getNumSubAttackMenuItems(int choice){
    if(choice==1){
      return Fighter.NUM_FIGHTER_MENU_ITEMS;
    }
    else if(choice==2){
      return Magical.NUM_MAGIC_MENU_ITEMS;
    }
    else{
      return Ranger.NUM_ARCHER_MENU_ITEMS;
    }
  }

  /** Should call the selected ability method 
   *  @param e represents the enemy to attack
   *  @param choice represents the type of Attack
   *  @param subChoice represents the choice of wepon to use
   *  @return String representation of the attack
  */
  public String attack(Enemy e, int choice, int subChoice){
    if(choice == 1){
      if(subChoice == 1){
        return sword(e);
      }
      else{
        return axe(e);
      }
    }
    else if(choice == 2){
      if(subChoice == 1){
        return magicMissile(e);
      }
      else{
        return fireball(e);
      }
    }
    else{
      if(subChoice == 1){
        return arrow(e);
      }
      else{
        return fireArrow(e);
      }
    }
  }

  /** @return the amount of gold the hero has */
  public int getGold(){
    return gold;
  }

  /** Adds to the amount of gold the hero has
   *  @param g the amount of gold to add to the hero's gold 
  */
  public void collectGold(int g){
    gold+=g;
  }

  /** Removes the amount of gold the hero has
   *  @param g the amount of gold to remove
   *  @return true if the gold is spent, false if there is no money left
   */
  public boolean spendGold(int g){
    if(gold>=g){
      gold-=g;
      return true;
    }
    return false;
  }

  /** @return true if a hero has a key false if the hero dosen't have a key */
  public boolean hasKey(){
    if(keys>0){
      return true;
    }
    return false;
  }

  /** adds to the amount of keys the hero has */
  public void pickUpKey(){
    keys++;
  }

  /** @return true and decrement keys if hero has a key, false if the hero dosen't */
  public boolean useKey(){
    if(keys>0){
      keys--;
      return true;
    }
    return false;
  }

  /** @return true if a the hero has as potion, flase if the hero dosen't have any potions */
  public boolean hasPotion(){
    if(potions>0){
      return true;
    }
    return false;
  }

  /** adds to the amount of potion the hero has */
  public void pickUpPotion(){
    potions++;
  }

  /** @return ture and decrement potions if hero has a potion, false if the hero dosen't */
  public boolean usePotion(){
    if(potions>0){
      
      potions--;
      return true;
    }
    return false;
  }

  /** Use sword to attack the enemy between 2-5 damage
   *  @param e represents the enemy
   *  @return string representation of the attack
   */
  @Override
  public String sword(Entity e){
    int r = (int)((Math.random()*4)+2);
    e.takeDamage(r);
    return super.getName() +" slashes " + e.getName() + " for " + r + " damage.";
  }


  /** Use axe to attack the enemy between 3-7 damage
   *  @param e represents the enemy
   *  @return string representation of the attack
   */
  @Override
  public String axe(Entity e){
    int r = (int)((Math.random()*5)+3);
    e.takeDamage(r);
    return super.getName() +" hits " + e.getName() + " with an Axe for " + r + " damage.";
  }

  /** Use magic missile to attack the enemy between 3-6 damage
   *  @param e represents the enemy
   *  @return string representation of the attack
   */
  @Override
  public String magicMissile(Entity e){
    int r = (int)((Math.random()*4)+3);
    e.takeDamage(r);
    return super.getName() +" missiles " + e.getName() + " with Magic Missile for " + r + " damage.";
  }

  /** Use fireball to attack the enemy between 4-8 damage
   *  @param e represents the enemy
   *  @return string representation of the attack
   */
  @Override
  public String fireball(Entity e){
    int r = (int)((Math.random()*5)+4);
    e.takeDamage(r);
    return super.getName() +" fireballs " + e.getName() + " for " + r + " damage.";
  }

  /** Use arrow to attack the enemy between 3-5 damage
   *  @param e represents the enemy
   *  @return string representation of the attack
   */
  @Override
  public String arrow(Entity e){
    int r = (int)((Math.random()*3)+3);
    e.takeDamage(r);
    return super.getName() +" shoots " + e.getName() + " with an Arrow for " + r + " damage.";
  }

  /** Use fire arrow to attack the enemy between 5-10 damage
   *  @param e represents the enemy
   *  @return string representation of the attack
   */
  @Override
  public String fireArrow(Entity e){
    int r = (int)((Math.random()*6)+5);
    e.takeDamage(r);
    return super.getName() +" flames " + e.getName() + " with a Fire Arrow for " + r + " damage.";
  }
}