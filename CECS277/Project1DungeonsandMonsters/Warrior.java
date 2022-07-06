// Warrior.java - Abhishek Jasti
/** Warrior.java - a representation of a warrior*/
public class Warrior extends Enemy implements Fighter{
  
  /** Initializes the warrior's name
    * @param n the name of the warrior
    * @param mHp warrior's max hp
  */
  public Warrior(String n, int mHp){
    super(n, mHp);
  }

  /** Describing the warrior's use of a sword
    * @param e some entity to attack with a sword
    * @return string representiton of the attack
    */
  @Override
  public String sword(Entity e){
    // Random Dmg = 2-5
    int r = (int)((Math.random()*4)+2);
    e.takeDamage(r);
    return super.getName() + " slashes " + e.getName() + " for " + r + " damage.";
  }

  /** Describing the warrior's use of an axe
    * @param e some entity to attack with an axe
    * @return string representiton of the attack
    */
  @Override
  public String axe(Entity e){
    // Random Dmg = 3-7
    int r = (int)((Math.random()*5)+3);
    e.takeDamage(r);
    return super.getName() + " hits " + e.getName() + " with an Axe for " + r + " damage.";
  }

  /** Attacking hero with warrior's choice of weapons
    * @param h representing the Hero
    * @return string representiton of the attack
    */
  @Override
  public String attack(Hero h){
    int r = (int)((Math.random()*2)+1);
    if(r==1){
      return sword(h);
    }
    return axe(h);
  }
}