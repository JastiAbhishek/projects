// Wizard.java - Abhishek Jasti
/** Wizard.java -  a representation of a wizard*/
public class Wizard extends Enemy implements Magical{
  
  /** Initializes the wizard's name
    * @param n the name of the wizard
    * @param mHp wizard's max hp
  */
  public Wizard(String n, int mHp){
    super(n, mHp);
  }

  /** Describing the wizard's use of a magic missile
    * @param e some entity to attack with a magic missile
    * @return string representiton of the attack
    */
  @Override
  public String magicMissile(Entity e){
    // Random Dmg = 3-6
    int r = (int)((Math.random()*4)+3);
    e.takeDamage(r);
    return super.getName() + " missiles " + e.getName() + " with Magic Missile for " + r + " damage.";
  }

  /** Describing the wizard's use of a fire ball
    * @param e some entity to attack with a fire ball
    * @return string representiton of the attack
    */
  @Override
  public String fireball(Entity e){
    // Random Dmg = 4-8
    int r = (int)((Math.random()*5)+4);
    e.takeDamage(r);
    return super.getName() + " fireballs " + e.getName() + " for " + r + " damage.";
  }

  /** Attacking hero with wizard's choice of weapons
    * @param h representing the Hero
    * @return string representiton of the attack
    */
  @Override
  public String attack(Hero h){
    int r = (int)((Math.random()*2)+1);
    if(r==1){
      return magicMissile(h);
    }
    return fireball(h);
  }
}