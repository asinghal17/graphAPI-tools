# countLikes by Anurag Singhal

countLikes uses Facebook's Graph API to output Total Like Counts for Page or Photo of Interest.

## Setup

### 1) Access Token
You will need an Access Token from Facebook for this script to be functional. You an generate a temporary one using the Graph API Explorer. Upon obtaining your accessToken navigate to "/input/token.txt" and paste the token in the token.txt file and save it.
### 2) Supporting Libraries
"cd" into the file directory and run the script below to install the necessary libraries for this script.

    $>python install -r requirements.txt

### 3) Input Schema
After installing the supporting Libraries, fill out the "_/input/input.csv_" file in the _input_ Directory. Example Below:

    Name    Facebook_ID     Type
    Alex    12345678        photo
    Bob     9101112134      page
    Carol   484576920048    photo
    
- **Name:** "Page Name"/"Photo Name"
- **ID:** ID of the Interested element.
    - Photos: "http://...facebook.com/photo.php?**fbid=1098762358020430**&set.."
    - Pages: Use http://findmyfbid.com/
- **Type:** What type of element is it i.e. "Photo" or "Page"

## Execute
    $>python countLikes.py <input file path> <output file path>

"input file path" = Path to your input you created in Step 2 above.    
You will find your <output CSV> in the _output_ directory unless stated otherwise.

## Resources
1. [Facebook Graph API Documentation](https://developers.facebook.com/docs/graph-api)
2. [Access Token](https://developers.facebook.com/docs/facebook-login/access-tokens)