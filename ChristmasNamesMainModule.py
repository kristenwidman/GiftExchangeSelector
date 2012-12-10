import sys
import ChristmasNamesSelectorModule as s
import EmailModule
import datetime
from constants import address_list, address_list_test, DEBUG, last_name

def print_to_outfile(text):
    """prints results of selection to a text file in case someone forgets
        who they should be giving to.
    """
    current_year = datetime.datetime.now().year
    if DEBUG: file_for_appending = "%s%sResults_test.txt" % (current_year, last_name)
    else: file_for_appending = "%s%sResults.txt" %(current_year, last_name)
    outfile = open(file_for_appending, 'a')
    outfile.write(text)
    outfile.close()
    return

def main():
    """main method for Christmas names selector. will call other methods as
        necessary to do selections and email people and write to outfile.iu6
    """
    '''args = sys.argv[1:]  #for running from command line with name list
    if len(args) != 1:
        print 'usage: python test.py nameList'
        sys.exit(-1)'''

    selector = s.ChristmasNamesSelector()
    if DEBUG: name_list = address_list_test.keys()
    else: name_list = address_list.keys()
    if DEBUG: print 'name list: ', name_list  #DEBUG only
    giver_receiver_match_list = selector.select_christmas_names(name_list)
    if DEBUG: selector.print_pairs(giver_receiver_match_list)  # DEBUG only
    print_to_outfile("Giver : Receiver\n")
    emailer = EmailModule.EmailFolks()
    for match in giver_receiver_match_list:
        if not DEBUG:
            emailer.format_email(match.giver, match.receiver)
            print_to_outfile(match.giver + " : " + repr(match.receiver) + "\n")

if __name__ == '__main__':
    main()

