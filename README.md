# auto-rapper:
We are to construct a Rap generator that will have adjustable styles, lengths, and temperature.


#The Data
We have access to lyrics from all publicly available songs.

#The Plan
Access the Genius.com API to get lyrics for prolific rappers, then train models to learn the unique styles of each.

#The Preperation
Take all lyrics by each rapper and place them in unique .txt files,

#The Modeling
Retrain gpt-2 on each of the rappers, saving their respective models for future use.

#The Results
We have a simple generator that can make relatively cohesive raps based on the seed text.
