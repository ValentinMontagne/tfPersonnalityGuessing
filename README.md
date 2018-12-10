#Quizz Messenger:

The project is about two step, one is about quizz the user and get his or her personality.
For this, we will use tensorflow to handle the results of the quizz.

##It will be 5 personality:

-   Sportive
-   Geek
-   Artist
-   NightLife
-   Crazy

##And this is the 6 questions for the quizz:

    1.  When it rain outdoor and you are stuck to home, what did you do ?

        0)  Outdoor? What is this, I just need a computer and some food.
        1)  I will take some papers and colors to draw what I have in mind.
        2)  Rainning ? No problem, cold water help, let's go running !
        3)  The answer D.
        4)  Outdoor ? During the day ? No way !
    
    2.  Your mom' comes to you with some stuff she bring from the market, what is it ?

        0)  Some healthy food.
        1)  A new gaming mouse.
        2)  Lot of painting tools.
        3)  This answer looks good right ?
        4)  Some soju.

    3.  When you are watching the sky, what are you seeing ?

        0)  The roof of my home.
        1)  Too dark, just all the stars and moon.
        2)  So many things flying fluffy and white !
        3)  Trying to follow the clouds while watching the sky.
        4)  The answer E.

    4.  You find a magical artefact, you have one wish, what did you choose ?

        0)  Be fucking rich, pubs, cars, women everything will be mine !
        1)  Be the world strongest man in all disciplines.
        2)  Be in a game, where you have all rights and control on this virtual world.
        3)  Another wish.
        4)  Create the most known masterpiece in the world.

    5.  You did something wrong to your best friend, what will you do to be forgiven ?

        0)  I will buy to him a new skin on League of legends.
        1)  Drawing him/her mad to you and after the reconciliation.
        2)  Nothing.
        3)  Buy some alcohol, finding a good plan for tonight and going together.
        4)  You will do some Karate or Judo to speak with your punchs.

##Results

-   Sportive => [2, 0, 3, 1, 4]
-   Geek => [0, 1, 0, 2, 0]
-   Artist => [1, 2, 2, 4, 1]
-   NightLife => [4, 4, 1, 0, 3]
-   Crazy => [3, 3, 4, 3, 2]

##Sportive

Good job ! You are a person who really like to be healthy and take care of your body !
You are someone who do a lot of sports and will have a great future in your club !

##Geek

Your life is about games, mangas, comics and so much things !
You have a powerful passion and you will never failed with a computer in your hands !

##Artist

Ow ! You are an artist, someone who is really sensible and can imagine everything, you have a talent to draw or art.
You will be the next Picasso or Akira Toriyama !

##Nightlife

You are the kind of person who live during the night, your heart is beating in the same rythm than the music clubs.
Take some soju and have fun !

##Crazy

Your mom' said to you that you are "Really special".

##Example Data with results:

[
    [2, 0, 3, 1, 4],
    [2, 4, 3, 1, 4],
    [2, 1, 3, 1, 1],
    [0, 1, 2, 2, 3],
    [0, 1, 0, 2, 0],
    [0, 0, 1, 2, 0],
    [1, 2, 2, 4, 1],
    [3, 2, 3, 4, 3],
    [1, 4, 2, 4, 1],
    [4, 4, 1, 0, 3],
    [4, 0, 1, 0, 3],
    [3, 4, 1, 0, 3],
    [3, 3, 4, 3, 2],
    [3, 3, 3, 3, 2],
    [3, 3, 4, 3, 4],
]

[
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
]