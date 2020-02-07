'''
    Nathanial Ziegler
    CS 5001
    February 11, 2020
    HW 5
    Description:
        UPDATE
'''

################################################
#
# Training Data - We know who said what
#
################################################

JAKE = ["I work best alone except when it comes to sex but sometimes "
        "including sex",
        "I love your face and I love your butt",
        "For the last time orangina is not orange soda",
        "That's where the blood's supposed to be",
        "I'd like your eight dollarest bottlest of wine please",
        "Title of your sex tape",
        "Guys Captain Holt has no pants on",
        "I'm fancy one time I had coffee flavored ice cream",
        "You know how I'm kind of a sexy bad boy",
        "You are orangina and I am orange soda"]

ROSA = ["I'm going to break those little fingers",
        "No one knows where I live",
        "If anything happened I would kill everyone in this room",
        "Grandpa beat cancer so now I look like an idiot",
        "I just forget stuff like a cool person",
        "I'd rather walk into the freezing ocean",
        "I'm gonna punch him so hard in the mouth",
        "Your entire life is garbage",
        "My body is terrified of me",
        "Anyone over the age of six celebrating a birthday should go to hell",
        "All smiling is horrible",
        "I doused your beard in chloroform",
        "Friendship is crap",
        "I am beating the hell out of him"]

HOLT = ["Wuntch time is over no regrets"
        "I've worked the better part of my years on earth overcoming "
        "every prejudice and fighting for the position I hold and now "
        "I feel it being ripped from my grasp and with it the very essence "
        "of what defines me as a man",
        "I went back to my office to do everyones paperwork, but I did "
        "no paperwork I started to plot my revenge",
        "I have original no flavor and whole wheat no flavor",
        "It has been a true pleasure to watch your distracting childish "
        "rivalry evolve into a distracting childish marriage",
        "Wuntch but if you're here who's guarding Hades",
        "Nothing is okay Wuntch is circling me like a shark frenzied by chum",
        "Do not trust any child that chews bubble gum flavored bubble gum",
        "Wuntch I never thought I would see you this high without a broom under "
        "you",
        "When someone steps up and says who they are the world becomes a "
        "better more interesting place",
        "If you steal my watch by midnight I will do your paperwork for a week"]

GINA = ["Hi Gina Linetti the human form of the 100 Emoji",
        "In a way we were all Gina Linetti today",
        "My mom is marrying shudder Charles dad toilet emoji",
        "Ew What can Charles Boyle do that I can't",
        "I am prepared to light Charles on fire in protest",
        "The only thing I am not good at is modesty because I am great at it",
        "You should be wailing you stone-cold bitch",
        "I'm incorporating Emoji into my speech to  express myself winky face",
        "Dress it up however you want that's some disgusting animal "
        "kingdom nonsense",
        "How is it possible that a spirit such as yourself even knows Charles",
        "Sure I'd love to see Charles get punched",
        "Do you know how many basic bitches would kill to have the "
        "same personality as me",
        ]

STOPWORDS = ["i", "a", "an", "of", "and", "to", "the", "is", "in", "it", "do",
             "you", "your", "that", "me", "my", "i'd", "i'm", "by", "as",
             "for", "but"]

################################################
#
# Testing Data - Who said it?
#
################################################

TESTING = ["A place where everybody knows your name is hell",
           "If I die turn my tweets into a book",
           "Yet I a Captain am no longer able to command my vessel my precinct "
           "from my customary helm, my office",
           "You move well Wuntch must be all the extra legs you crab",
           "Anyone over the age of six celebrating a birthday should go to hell",
           "All the orange soda spilled out of my cereal",
           "Fine but in protest I'm walking over there extremely slowly",
           "I want all your paperwork in by tomorrow",
           "I'm so confused I don't know what's happening right now "
           "title of your sex tape",
           "All smiling is horrible"]
