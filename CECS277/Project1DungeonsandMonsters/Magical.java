// Magical.java - Anand Jasti
/** Interface for magical behaviors of an object */
public interface Magical{
  
  /** Final variable of magical menu */
  static final String MAGIC_MENU = "1. Magic Missile\n2. Fireball";

  /** Final variable for number of menu items */
  static final int NUM_MAGIC_MENU_ITEMS = 2;

  /** Method to make the object use magic missile */
  public String magicMissile(Entity e);

  /** Method to make the object use fireball */
  public String fireball(Entity e);
}