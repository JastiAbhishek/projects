
public abstract class Enemy extends Entity{
  public Enemy(String n, int mHp){
    super(n,mHp);
  }

  public abstract String attack(Hero h);
}
