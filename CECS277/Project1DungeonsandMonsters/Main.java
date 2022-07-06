/** Main.java - Creates a game where a user can explore a dungeon maze and
 *              fight monsters that they encounter along the way.
 */
class Main {
  /** Prompt the user to enter a name, then construct a Hero with that name.
   *  Display the Hero with the map and have the user choose a direction
   * @param args
   */
  public static void main(String[] args) {
    System.out.print("What is your name traveler?");
    String hero = CheckInput.getString();
    char ch='s';
    Hero h = new Hero(hero);
    EnemyGenerator eg = new EnemyGenerator();
    int userInput = 0;
    Map m = Map.getInstance();
    while(true){
      System.out.println(h);
      System.out.println("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit");
      userInput = CheckInput.getIntRange(1, 5);
      if(userInput==5){
        break;
      }
      else if(userInput==1){
        ch=h.goNorth();
      }
      else if(userInput==2){
        ch=h.goSouth();
      }
      else if(userInput==3){
        ch=h.goEast();
      }
      else if(userInput==4){
        ch=h.goWest();
      }

      if(ch=='x'){
        System.out.println("Location out of bounds.");
      }
      else if(ch=='n'){
        System.out.println("Nothing here.");
      }
      else if(ch=='s'){
        store(h);
      }
      else if(ch=='f'){
        if(h.hasKey()){
          h.levelUp();
          h.useKey();
        }
        else{
          System.out.println("Find a key to finish this level");
        }
      }
      else if(ch=='i'){
        int r = (int)((Math.random()*2)+1);
        if(r==1){
          h.pickUpKey();
          System.out.println("You found a Key!");
        }
        else{
          h.pickUpPotion();
          System.out.println("You found a Potion!");
        }
        m.removeCharAtLoc(h.getLocation());
      }
      else if(ch=='m'){
        Enemy e = eg.generateEnemy(h.getLevel());
        if(!monsterRoom(h, e)){
          break;
        }
      }
    }
    System.out.println("Game Over.");
  }

  /** Displays the enemy and then repeatedly prompts the user to fight, run
   *  away, or drink a potion. If they choose to fight, call the fight method.
   *  If they run away choose a random direction to move the Hero
   *  @param h represents the hero
   *  @param e represents the enemy
   *  @return true if the hero is still alive after the fight, false if the hero is dead
   */
  public static boolean monsterRoom(Hero h, Enemy e){
    int userInput;
    System.out.print("You've encountered a ");
    while(true){
      System.out.println(e+"\n1. Fight\n2. Run Away");
      if(h.hasPotion()){
        System.out.println("3. Drink Potion");
        userInput = CheckInput.getIntRange(1, 3);
      }
      else{
        userInput = CheckInput.getIntRange(1, 2);
      }

      if(userInput==1){
        fight(h, e);
      }
      else if(userInput==2){
        int r = (int)((Math.random()*4)+1);
        if(r==1){
          h.goNorth();
        }
        else if(r==2){
          h.goSouth();
        }
        else if(r==3){
          h.goEast();
        }
        else{
          h.goWest();
        }
        return true;
      }
      else if(userInput==3){
        h.heal();
        h.usePotion();
        System.out.println("Health regenerated to max health");
      }

      if(h.getHp()<=0){
        return false;
      }
      if(e.getHp()<=0){
        // random amount of gold dropped 2*hero's level - 5*hero's level
        int r = (int)((Math.random()*4*h.getLevel())+2*h.getLevel());
        h.collectGold(r);
        System.out.println(e.getName()+" dropped " + r + " gold coins.");
        Map.getInstance().removeCharAtLoc(h.getLocation());
        return true;
      }
    }
  }

  /** Dose a single round of damage by allowing the user to choose to do
   *  physical, magical, or ranged attack. Then, depending on their selection,
   *  displays the corresponding submenu. Those two selections are passed to
   *  the hero's attack method to attack the enemy. The enemy then attacks back
   *  if it is still alive
   *  @param h represents the hero
   *  @param e represents the enemy
   *  @return true
   */
  public static boolean fight(Hero h, Enemy e){
    System.out.println(h.getAttackMenue());
    int attackInput = CheckInput.getIntRange(1, h.getNumAttackMenuItems());
    System.out.println(h.getSubAttackMenue(attackInput));
    int subAttackInput = CheckInput.getIntRange(1, h.getNumSubAttackMenuItems(attackInput));
    System.out.println(h.attack(e, attackInput, subAttackInput));
    if(e.getHp()>0){
      System.out.println(e.attack(h));
    }
    return true;
  }

  /** Represents a store where the Hero can by potions or keys
   *  @param h represents the hero
   */
  public static void store(Hero h){
    int userInput;
    System.out.println("Welcome to the store. What would you like to buy?\n1. Health Potion - 25g\n2. Key - 50g\n3. Nothing, just browsing...");
    userInput = CheckInput.getIntRange(1, 3);
    if(userInput==1){
      if(h.spendGold(25)){
        h.pickUpPotion();
        System.out.println("Potion has been added to your inventory");
      }
      else{
        System.out.println("You don't have enough gold to by a Potion!");
      }
    }
    else if(userInput==2){
      if(h.spendGold(50)){
        h.pickUpKey();
        System.out.println("Key has been added to your inventory");
      }
      else{
        System.out.println("You don't have enough gold to by a key");
      }
    }
    else{}
  }
}