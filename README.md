# Dice-Game

This file contains instructions and other important infomation reguarding the game.
	
				\\\\\		/////\\\\\		  //////		////////
				//  \\			/\			   ///			  /
				//   \\			/\			  //				  \\\\
				//   //			/\			  \\				  ////
				//  //			/\			   \\\			  /
				/////		/////\\\\\\		  \\\\\\		////////
				
				
				   /////	    /\		   ////  \\\\		  |/////
				 //			     /  \		   // //\\ \\		  |___
				 //  ////	  ///\\\	  //        \\		|
				  ////		 //    \\	  //        \\	  |/////
   
   
The game is similar to the game snakes and ladders. It is a digitalized boardgame where the first player to the end of the board wins the
game. There are two players and they both role two six-sided dice and the results are combined to get the total movement magnitude that the
player will move. If the player roles the same value on both dice then the results are added and the player will go that amount of spaces
backwards instead of the forwards for normal roles. The first player is randomized as either Player 1 or 2. There are externally loaded
obstacles that appear on the first role of the dice. These obstacles have the effect of moving the player either forwards or backwards a
specific amount. This can all be edited in external .txt files as later detailed in this file.


Instructions:


How to edit external files:

Messages (win.txt, start.txt, and double.txt)

The text in these files is what is displayed ingame when the event is triggered. Therefore one can put any text into the file if they want
to change the messages ingame.

Obstacles

"42_-_3,10_-_16,3_-_2,19_-_4". This is the defalt obstacle arrangement. There are 4 obstacles and 3 pieces of infomation per obstacle.
The obstacles are seaperated by commas (","), the internal data is seperated by underscores ("_"). The first piece of infomation is the
obstacles location. The second is the direction of movement. There are two valid options for this section: "-" for moving backwards, and
"+" or moving forwards. The final piece of infomation is the magnitude, or how far forwards or backwards the obstacle will send the player.
Using the defalt as an example, 42 is the location on the board, it goes backwards and the magnitude is 3. This means that when the player
hits the 42nd square they will be moved backwards 3 spaces. Only ever have 4 obstacles. More will crash the program, and only use a whole number
for the first and last pieces of infomation. Use only a "+" or "-" for the 2nd piece.
