This Python Script Is A Script Used To Play The Classic Hangman Game, In Which You Guess Letters To Solve Words Without Completing Hangman

In Main File "app.py", a Function From "assets.py" Is Called and Picks A Random Word From The "wordlist" Variable.<br>
The Main File Then Setups Board To Show How Many Characters Are In Chosen Word As Well As Lives Left and Letters Left.<br>
User Chooses A Letter and If Letter Is In Word, Then Characters In Word Are Updated and Letter Is Removed From List<br>
To Let You Know That It Has Been Used Already. If Letter Is Not In Word, Then Lives Decrease By One Thus Updating, <br>
Visual Display Of The Hangman. When Lives Are 0 and Hangman Is Complete, You Lose. If You Guessed The Word Correctly,<br>
Then You Win and You Can Choose To Play The Game Again With A Different Word. The Words From The WordList Are Deleted<br>
Each Game To Prevent Duplicates So You'll Have A New Word Each Time You Play Again. Words Can Be Added or Removed From<br>
WordList by Adding Them On A New Line In The "wordlist.txt" File Which Has 1000 Words By Default. New Words Can Only<br>
Contain Letters, Spaces, Commas(,), Apostrophes('), Periods(.), and Hypens(-). This Game Also Tells You How Many Words<br>
Are Left In Your Wordlist When It Shows The Scoreboard.

Python Used:

- For/While Loops
- Multiple Files
- Modules(String, PathLib-Path, and Random)
- External Assets("wordlist.txt")
- Conditional Statements
- Lists 
- Sets
- User Input
- Functions
- Comments
- Updating Variables