#This project is for doing secret santa style name selection for gift exchanges.#
Note that this project is currently optimized for Widman family Christmas 2012.
It is not (yet) written to be fully general, so many parameters and methods
may be unclear.

This is intended to create a randomized secret santa gift exchange given
names and emails as parameters. It has methods to select a single recipient per
giver or to select 2 recipients for each giver. An email will be sent to each
giver with the name(s) of the person(/people) they should get gifts for. This
email may include a wish list for the person. A text file will be created in
the same folder that includes giver:receiver pairs in case anyone loses their
email and a lookup needs to be done.

##To Run:##
1. Download/clone ChristmasNamesMainModule.py, ChristmasNamesSelectorModule.py,
and EmailModule.py
2. Create your own constants.py file including an address list dictionary,
    an optional list for any people you would like to not give to each other,
    an optional list for people who want to give to each other,
    username and password for a gmail address to send emails from,
    and a DEBUG = False line:
    Format:
        address_list = {'name': ['email@gmail.com','otheremail@gmail.com'],
                    'second-name': ['nextemail@gmail.com'], ...}

        exclude_list = ["name1","name2"]

        preferences = [{("name1","name2"): ["name3", "name4", "name5", "name6"]}]
        (special case for 2012 requests)

        username = email_username
        password = email_password

        DEBUG = False  (if False, does not print debug info)

3. If you wish to use wish lists, include them as text files with the name of
    the person requesting (+.txt) in the same folder. Also update the EmailModule
    to set wish_list to True.
4. Run the ChristmasNamesMainModule.py
5. Check your email.

