# MysteryCalculator
The Christmas Cracker gift.

There was one time my Christmas cracker contained a pack of six cards, the so-called Mystery Calculator, which provides a neat little party trick for the 
non-initiated. It goes like this. The six cards all have 32 numbers on them, all between 1 and 63 and arranged in a matrix of 4 rows and 8 columns per card. 
The unsuspecting participant is asked to randomly pick one card from the deck of 6 and to silently memorise one of the 32 numbers on that card. The card is
then handed back to the magician and the participant is asked to select from the 5 remaining cards those that also have the memorised number on them.

The magician, based on the initially chosen card as well as the cards selected in the second step, is then able to divine which was the number the 
participant had silently chosen in the first place. With a bit of magician's hocus pocus and mumbo jumbo, this neat little trick will draw some ooohs! and 
aaahs! from the party audience.

So what's the math behind the magic? All the magician has to do is to add the left hand corner numbers of the initial card and any other card where that 
number appears and the total is always the number the participant had silently memorised!

I had just started learning to program with Python. I coded a working version of The Mystery Calculator I could run in my terminal. It sat neglected 
for a while until I decided to learn how to share my python projects with others. This is my first effort. I used [Streamlit](https://docs.streamlit.io/) to
turn my python script into this web app.
