import sys
import ChristmasNamesSelectorModule as s
import EmailModule
import datetime
from address_list import address_list

def print_to_outfile(text):
    """prints results of selection to a text file in case someone forgets
        who they should be giving to.
    """
    current_year = datetime.datetime.now().year
    file_for_appending = "%sResults.txt" %(current_year)
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
    name_list = address_list.keys()
    #print 'name list: ', name_list  #DEBUG only
    giver_receiver_match_list = selector.select_two_christmas_names(name_list)
    #selector.print_pairs(giver_receiver_match_list)  # DEBUG only
    print_to_outfile("Giver : Receiver\n")
    emailer = EmailModule.EmailFolks()
    for match in giver_receiver_match_list:
        emailer.format_email(match.giver, match.receiver)
        print_to_outfile(match.giver + " : " + repr(match.receiver) + "\n")

if __name__ == '__main__':
    main()

