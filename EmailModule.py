import smtplib
import string
from constants import address_list, address_list_test, DEBUG, email_username, email_password

class EmailFolks(object):

    def format_email(self,giver,receiver,wish_list=False):
        """Takes a giver and receiver names as input.
            Formats email parameters for each giver with the name of the person
            they are giving a gift to (receiver)
        """
        if DEBUG: address_dictionary = address_list_test
        else: address_dictionary = address_list
        host = "localhost"
        subject = "Widman family Christmas gift selection"
        to_address_list = address_dictionary[giver]
        from_address = "widmanChristmasNames@gmail.com"
        text = "Christmas name selection for Widman Family Christmas. You (" + giver + ") are giving presents to " + repr(receiver) + ". Be thoughtful! "
        if wish_list:
            text.append(get_wishlist(receiver))
        for to_address in to_address_list:
            print to_address
            self._send_email(from_address,to_address,subject,text)

    def _send_email(self, from_address, to_address, subject, text):
        '''Actually sends the emails
        '''
        body = string.join((
            "From: %s" % from_address,
            "To: %s" % to_address,
            "Subject: %s" % subject ,
            "",
            text
            ), "\r\n")
        #credentials
        username = email_username
        password = email_password

        server = smtplib.SMTP('smtp.gmail.com:587')  #specific for gmail (I think)
        server.starttls()
        server.login(username,password)
        server.sendmail(from_address, to_address, body)
        server.quit()

    def get_wishlist(self, receiver):
        '''Used when each person supplies a wishlist.
        '''
        wish_list_text = self.get_wish_list_text(receiver)
        text = "Here is his/her wish list: \n\n" + wish_list_text

    def get_wish_list_text(self, receiver):
        """Takes the name of a receiver as input. Returns that
            person's wish list, which has been saved as a text file
            name.txt under the same folder as this program.
        """
        file_name = receiver + ".txt"
        wish_list = open(file_name)
        wish_list_string = ""
        for line in wish_list:
            wish_list_string += line
        wish_list.close()
        return wish_list_string
