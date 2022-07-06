// Ranger.java - Abhishek Jasti
/** Ranger.java - representation of a ranger*/
public class Ranger extends Enemy implements Archer{
  
  /** Initializes the ranger's name
    * @param n the name of the ranger
    * @param mHp ranger's max hp
  */
  public Ranger(String n, int mHp){
    super(n, mHp);
  }

  /** Describing the ranger's use of an arrow
    * @param e some entity to attack with an arrow
    * @return string representiton of the attack
    */
  @Override
  public String arrow(Entity e){
    // Random Dmg = 3-5
    int r = (int)((Math.random()*3)+3);
    e.takeDamage(r);
    return super.getName() + " shoots " + e.getName() + " with an Arrow for " + r + " damage.";
  }

  /** Describing the ranger's use of a fire arrow
    * @param e some entity to attack with a fire arrow
    * @return string representiton of the attack
    */
  @Override
  public String fireArrow(Entity e){
    // Random Dmg = 5-10
    int r = (int)((Math.random()*6)+5);
    e.takeDamage(r);
    return super.getName() + " flames " + e.getName() + " with an Fire Arrow for " + r + " damage.";    
  }

  /** Attacking hero with ranger's choice of weapons
    * @param h representing the Hero
    * @return string representiton of the attack
    */
  @Override
  public String attack(Hero h){
    int r = (int)((Math.random()*2)+1);
    if(r==1){
      return arrow(h);
    }
    return fireArrow(h);
  }
}