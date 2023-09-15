 # 2.2Implement a class called player that represents a cricket player. The player class should have a method called play() which prints" The player is playing cricket. Derive two classes, Batsman and Bowler, from the player class. Override the play()method in each derived class to print"The batsman is batting" and"The Bowler is bowling ", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.

class Player:
  def play(self):
    print("The player is playing cricket.")
    
class Batsman(Player):
    def play(self):
        print("The batsman is batting.") 

class Bowler(Player):
    def play(self):
        print("The bowler is bowling. ")

batsman = Batsman() 
bowler = Bowler() 

batsman.play() 
bowler.play()