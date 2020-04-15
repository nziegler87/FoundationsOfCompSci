import random

RESPONSES = ['As I see it, yes.', ' Ask again later.', 'Better not tell you now.',
            'Cannot predict now.', 'Concentrate and ask again.',
            'Don’t count on it.', 'It is certain.',
            'It is decidedly so.', 'Most likely.', 'My reply is no.',
            'My sources say no.', 'Outlook not so good.',
            'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.',
            'Very doubtful.', 'Without a doubt.', 'Yes.',
            'Yes – definitely.', 'You may rely on it.']

print("Welcome to magic eight ball. Ask me a question and I will predict the "
      "likelhood of that happening")

response = input("What is your question? Enter :q: to quit.\n").lower()

while response != ":q:":
    print(random.choice(RESPONSES))
    response = input("What is your question? Enter :q: to quit.\n").lower()
    
