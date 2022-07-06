// Fighter.java - Anand Jasti
/** Interface for fighter behaviors of an object */
public interface Fighter{
  
  /** Final variable of fighter menu */
  static final String FIGHTER_MENU = "1. Sword\n2. Axe";

  /** Final variable for number of menu items */
  static final int NUM_FIGHTER_MENU_ITEMS = 2;

  /** Method to make the object use sword */
  public String sword(Entity e);

  /** Method to make the object use axe */
  public String axe(Entity e);
}