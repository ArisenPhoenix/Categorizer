from collections import OrderedDict

CATS = ["Meow", "Cat", "Me-Ow", "Purr", "Feline", "Tiger", "Ocelot", "Calico"]
CATS_SUB = [""]
CATS_SOUNDS = ["Pur"]

CAT_DICT = OrderedDict({
    "main": CATS,
    "word": CATS_SUB,
    "phonics": CATS_SOUNDS
})


def cat_callback(match_text: str, debug) -> True | False:
    """Your Call Back Here: Should Return A Truthy Value or False"""
    for item in match_text.split(" "):
        # You Could Use Regex Here Or Something else
        if debug:
            print("Whatever Debug Text You Want To Display")
            #     Debug is specified by passing A truthy value into the categorizer class
        # Pseudo Code
        if item == "REGEX MATCH...":
            return True
    return False


DOGS = ["Ruff", "Dog", "Howl", "Canine", "Wolf", "Bear", "Great Dane"]
DOGS_SUB = ["ff", "Ruf", "Wuf"]
DOGS_SOUNDS = ["Gr"]
DOG_DICT = {
    "main": DOGS,
    "word": DOGS_SUB,
    "phonics": DOGS_SOUNDS
}


def dog_callback(match_text: str, debug: bool | str):
    """Your Call Back Here: Should Return A Truthy Value or False These Callbacks Can Be As Complicated As You Like"""
    if "K-9".lower() in match_text.lower():
        return True
    if debug:
        print("No Matches Found")
    return False




CAT_DOG_TEMPLATE = OrderedDict({
    """
    This Is A Simple Single Level Categorization If You Wanted Sub Categories You Would Repeat
    This Process And Place The Templates Inside Of 'sub' Which Would Then Allow For Further Sub-Categories
    The Categorizer Will Nest The Items Inside Directories of The Key, So In This Case The Top Level Directories
    Would Be 'cats', 'dogs', 'Others'. They Keys May Be Named Anything You Like So Long As They Are ASCII, So Typical
    Strings.
    """
    "cats": {
        "verify": CAT_DICT,
        "callback": cat_callback,
        "sub": "__EMPTY__"
    },
    "dogs": {
        "verify": DOG_DICT,
        "callback": dog_callback,
        "sub": "__EMPTY__"
    },
    "Other": {
        "verify": None,
        "sub": "__STOP__"
    }
})




# For Nesting You Just Rinse And Repeat, Placing All Options Allowed Inside

CAT_TYPE_TEMPLATE = OrderedDict({
    "calico": {
        "verify": ["orange", "multi-colord"],
        "sub": "__EMPTY__",
    },
    "siamese": {
        "verify": ["siamese", "albino", "lady and the tramp"],
        "sub": "__EMPTY__",
    },
    "other": {
        "verify": None,
        "sub": "__END__"
    }
})


DOG_TYPE_TEMPLATE = OrderedDict({
    "golden retriever": {
        "verify": ["gold", "golden", "golden retriever"],
        "sub": "__EMPTY__",
    },
    "bull dog": {
        "verify": ["bull", "dog", "bulldog", "bull dog"],
        "sub": "__EMPTY__",
    },
    "other": {
        "verify": None,
        "sub": "__END__"
    }
})


CAT_TYPE_DOG_TEMPLATE = OrderedDict({
    "cats": {
        "verify": CAT_DICT,
        "callback": cat_callback,
        "sub": CAT_TYPE_TEMPLATE
    },
    "dogs": {
        "verify": DOG_DICT,
        "callback": dog_callback,
        "sub": DOG_TYPE_TEMPLATE
    },
    "Other": {
        "verify": None,
        "sub": "__STOP__"
    }
})


# As A Last Piece Of Wisdom. If you were categorizing something such as humans, let's say the following categories:
# Race, Sex, Gender, Age, etc.
# You could reuse all the sub categories within all the final templates and this goes for animals too,
# such as for the animal's age.

# But If Every Sub Category Has Differences Then You Will Have To Write Out Different Criteria For Them Of Course

YOUNG = list(range(1, 4))
MID = list(range(4, 7))

# Converting them to strings As 2 is not == "2" in python for example. Just A Small Hassle Saver.
YOUNG = [str(age) for age in YOUNG]
MID = [str(age) for age in MID]



# Example:
ANIMAL_AGE_TEMPLATE = OrderedDict({
    # Ordered Dict Is Used To Ensure Categories Are Checked In The Order They Are Written.
    "young": {
        "verify": YOUNG,
        # "__EMPTY__" Tells It To Stop If Verification Is Successful Else It Will Go On To "mid"
        "sub": "__EMPTY__"
    },
    "mid": {
        "verify": MID,
        "sub": "__EMPTY__",
    },
    "old": {
        # Default Here In This Case So No Verification Needed
        "verify": None,
        "sub": "__STOP__"
    }
})


# Finally We Get To This One. It's A Very Simple Example But It Will Only Check To See If The Numbers Are Contained
# Within The Text, If So, It Will Appropriately Place Them Into That Directory.
# If Not It Defaults To Old... Just Showing An Example Of How This Can Work, I'd say most animals are not older than
# 6
CAT_DOG_AGE_TEMPLATE = OrderedDict({
    "cats": {
        "verify": CAT_DICT,
        "callback": cat_callback,
        "sub": ANIMAL_AGE_TEMPLATE
    },
    "dogs": {
        "verify": DOG_DICT,
        "callback": dog_callback,
        "sub": ANIMAL_AGE_TEMPLATE
    },
    "Other": {
        "verify": None,
        # We Don't Want To __STOP__ Here As There Is Another Sub-Category To Get Through First
        "sub": ANIMAL_AGE_TEMPLATE
    }
})


print(CAT_DOG_AGE_TEMPLATE)







