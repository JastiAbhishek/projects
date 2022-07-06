// Archer.java - Anand Jasti
/** Interface for archer behaviors of an object */
public interface Archer{
  
  /** Final variable of archer menu */
  static final String ARCHER_MENU = "1. Arrow\n2. Fire Arrow";

  /** Final variable for number of menu items */
  static final int NUM_ARCHER_MENU_ITEMS = 2;

  /** Method to make the object use arrow */
  public String arrow(Entity e);

  /** Method to make the object use fire arrow */
  public String fireArrow(Entity e);
}