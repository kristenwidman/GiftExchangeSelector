# kwidman
# 12/1/11
# Christmas name selector

import random
from constants import exclude_list, DEBUG

class GiverReceiverPair(object):
    '''Class to hold a pair of giver and receiver.
        Note that receiver can be a list of receivers.
    '''
    def __init__(self, giver, receiver):
        self.giver = giver
        self.receiver = receiver

    def __repr__(self):
        return self.giver + repr(self.receiver)

class ChristmasNamesSelector(object):
    '''Methods associated with pairing givers and receivers randomly.
        Contains two public methods for pairing names when given a list
        and to print the pairs.  Also contains private method(s)
    '''

    def _select_one_name(self, giver, receiver_list):
        '''Given one name (giver) and a list of receivers (all not
            yet paired), selects a receiver from the list and creates
            a GiverReceiverPair object.  Returns said object. 
        '''
        receiver = random.choice(receiver_list)
        if (giver != receiver):       # giver cannot be same as receiver
            giver_receiver_dict = {giver: receiver}
            return giver_receiver_dict
        else:
            return self._select_one_name(giver, receiver_list)

    def select_christmas_names(self, name_list):
        '''Main functionality - takes a list of names and returns
            a list of GiverReceiverPair objects. If only name left
            in receiver_list is == giver, this method sets the list
            to empty and calls itself again.
        '''
        giver_list = list(name_list)
        receiver_list = list(name_list)
        list_of_pair_dicts = []
        for name in giver_list:
            if ((len(receiver_list) > 1) or (name != receiver_list[0])):
                giver_receiver_dict = self._select_one_name(name, receiver_list)
                receiver_list.remove(giver_receiver[giver])
                list_of_pair_dicts.append(giver_receiver_dict)
            else:
                list_of_pair_dicts = self.select_christmas_names(name_list)
        return list_of_pair_dicts

    def print_pairs(self, giver_receiver_pairs):
        '''Method to print the generated giver/receiver pairs.
            Takes a GiverReceiverPair object as input.
            Returns nothing.
        '''
        for pair in giver_receiver_pairs:
            print pair.keys()," : ",pair.values(),'\n'
        return

    def _check_for_preferences(self, g_r_list):
        '''For inclusion of people who would like to give to one another.
            Format for this list is a dictionary with tuple keys and list values
            i.e. {("Rob","Linda"): ["Jeff and Kristen", "Michelle and Ryan", "Carla", "Brad"]}
        '''
        givers = None


        givers_tuple = preferences.keys()
        receivers_list = preferences.values()[0].sort()
        for dictionary in g_r_list:
            if dictionary.keys()[0] in givers_tuple[0]:


    def _check_for_conflicts(self, g_r_list):
        '''For inclusion of a list of people who should not be giving to each other
        '''
        for dictionary in g_r_list:
            if dictionary.keys()[0] in exclude_list:
                for value in dictionary.values()[0]:
                    if value in exclude_list:
                        return False
        return True

    def select_two_christmas_names(self,name_list):
        '''For use in 2012 - each person/couple gives gifts to 2 other people/couples.
        '''
        giver_list = list(name_list)
        receiver_dict = {}
        for receiver in name_list:
            receiver_dict[receiver] = 0
        list_of_g_r_dicts = []
        for giver in giver_list:
            if ((len(receiver_dict) > 3) or (len(receiver_dict) == 2 and giver not in receiver_dict)):
                giver_receiver_dict = self._select_two_names(giver, receiver_dict.keys())
                for receiver in giver_receiver_dict[giver]:
                    receiver_dict[receiver] += 1
                    if receiver_dict[receiver] > 1:
                        del receiver_dict[receiver]
                list_of_g_r_dicts.append(giver_receiver_dict)
            else:
                return self.select_two_christmas_names(name_list)
        #added below check people who should NOT be giving to each other
        if self._check_for_conflicts(list_of_g_r_dicts):
            return list_of_g_r_dicts
        else:
            return self.select_two_christmas_names(name_list)

    def _select_two_names(self, giver, receiver_list):
        '''for 2012'''
        receivers = list(receiver_list) #so that the original list can be used in recursion if checks fail
        receiver1 = random.choice(receivers)
        receivers.remove(receiver1)
        receiver2 = random.choice(receivers)
        receiver_picks = [receiver1, receiver2]
        if (giver not in receiver_picks):   # giver cannot be same as receiver
            giver_receiver_match = {giver: receiver_picks}
            return giver_receiver_match
        else:
            return self._select_two_names(giver, receiver_list)


