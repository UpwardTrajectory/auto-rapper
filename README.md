# Auto-rapper:
We're trying to construct a Rap generator that will have adjustable styles, lengths, and temperature. Ideally the user would be able to use their own input to start things off, similar to [talk to transformer](https://talktotransformer.com/)


## The Data
We have access to lyrics from all publicly available songs.

## The Plan
Access the Genius.com API through the lyricsgenius python package to get lyrics from prolific rappers, then train models to learn the unique styles of each.

## The Preperation
Take lyrics from all songs by each rapper and place them in unique .txt files to be used when fine tuning the model.

## The Modeling
We used google colab with a gpu to Retrain gpt-2's 345mb model on each of the rappers, then saved each uniquely retrained model for future use.

## The Results
We have a simple generator that can make relatively cohesive raps based off of the chosen rapper's style and the prefix text.

### Next steps
Ideally deploying the auto rapper to the web as a flask app would be nice, also increasing the number of rapper models

### Where credit is due:

We borrow heavily from the code in [this repo](https://github.com/minimaxir/gpt-2-simple) and [this](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce) google colab which is also linked in the repo.


[OpenAI's official GPT-2 repo (MIT License)](https://github.com/openai/gpt-2)
