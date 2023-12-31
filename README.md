# Categorizer

Categorizes Text Based On A Dictionary Of Lists Of Strings And Callbacks
If Needed. Essentially A Template Is Created And Then It Does Its Work. It Then Moves The File Or File Into A Directory
And Accompanying Sub-Directories Based From The Root Directory Provided, Followed By The Categories Decided Upon,
And Lastly The Final Directory With All Its Contents Will Be In Placed Into The Last Sub Category.
## The End Result Will Look Like: 
### <root_dir>/[...categories]/<categorized_folder_name>/[...files_within_folder]


# Use Cases

- Movies
- Images
- Songs
- Anything With A Descriptive Title

### Categories Are User Defined
#### NOTE
It Is Recommended To Use collections.OrderedDict So That The Flow Will Definitely Run In
The Order You Specify, But This Is Optional.

## Brief
Each Category can have "verify", "sub", "callback", "except"
- 'verify' is explained below in more detail
- 'sub' is a sub category with the same exact structure as the main category and it can continue going down until the end
- 'callback' is a callback function for more precise matching, perhaps with regex or the like
- 'except' will be a list of items that are exceptions to verify and will continue on even if there was a match in 'verify'

Each verify Can Have "main", "word", and/or "phonics"
- 'main' Match Based On The Word Just Existing In Title (Case Insensitive) - it will be converted to title case in any case
- 'word' Matches A Word Exactly Within The Title ( Case Insensitive )
- 'phonics' Matches For The Sound or sub_string Within Each Word In The Directory Name (Case Sensitive) - It Does Not Convert Any Text To Another Case To Find The Match, But It Will Most Likely Be Lower Case
- Lastly, Verify Can Be A Simple List or Tuple To Check Through. It Will Work Just The Same As The Dictionary But Will Check It As If It Were 'main'

## Special Keywords For sub
- if 'sub' is set to "**_ _ EMPTY _ _**" the behavior is such that it will continue categorization after but will always finish after the current sub-category level. Mostly Used For When You're At The Last Sub-Category So That It Will Continue On To The Other Sub-Categories If No Match Is Found, Otherwise It Will Stop And End The Categorization For That Directory
- if 'sub' is set to "**_ _ DIRECTORY _ _**" it will end the categorization process returning the current category and subcategories of the current target directory for further processing. You may then pass the returned data back in after processing and continue with like that. Or it could just be used to check what it has done so far.
- if 'sub' is set to "**_ _ STOP _ _**" then all execution is complete. This Is Mostly Just Reserved For The Last Sub Category Meaning There Is Nothing More And Should Be Used As Such To Decrease Chances Of Infinite Loops

## Perhaps Unintuitive Until Explained:
- if you want a category to be skipped, perhaps for use at another time, simply set it to an empty list and set sub to whatever you would normally want it to be or just use another Template Or Just Simply None.


# EXAMPLE CATEGORIZATION TEMPLATE
Look At The example.py To See An Example


