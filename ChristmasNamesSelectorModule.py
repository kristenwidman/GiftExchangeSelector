# kwidman
# 12/1/11
# Christmas name selector

import random

class GiverReceiverPair(object):
    '''Class to hold a pair of giver and receiver.
    '''
    def __init__(self, giver, receiver):
        self.giver = giver
        self.receiver = receiver

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
            giver_receiver_pair = GiverReceiverPair(giver,receiver)
            return giver_receiver_pair
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
        list_of_pair_objects = []
        for name in giver_list:
            if ((len(receiver_list) > 1) or (name != receiver_list[0])):
                giver_receiver = self._select_one_name(name, receiver_list)
                receiver_list.remove(giver_receiver.receiver)
                list_of_pair_objects.append(giver_receiver)
            else:
                list_of_pair_objects = self.select_christmas_names(name_list)
        return list_of_pair_objects

    def print_pairs(self, giver_receiver_pairs):
        '''Method to print the generated giver/receiver pairs.
            Takes a GiverReceiverPair object as input.
            Returns nothing.
        '''
        for pair in giver_receiver_pairs:
            print pair.giver + " : " + repr(pair.receiver) + '\n'
        return


    def select_two_christmas_names(self,name_list):
        giver_list = list(name_list)
        receiver_dict = {}
        for receiver in name_list:
            receiver_dict[receiver] = 0
        list_of_g_r_objects = []
        for name in giver_list:
            if ((len(receiver_dict) > 2) or (len(receiver_dict) == 2 and name not in receiver_dict)): #!= receiver_dict[0][0] and name != receiver_dict[1][0])):
                giver_receiver = self._select_two_names(name, receiver_dict.keys())
                for receiver in giver_receiver.receiver:
                    receiver_dict[receiver] += 1
                    if receiver_dict[receiver] > 1:
                        del receiver_dict[receiver]
                list_of_g_r_objects.append(giver_receiver)
            else:
                list_of_g_r_objects = self.select_two_christmas_names(name_list)
        return list_of_g_r_objects

    def _select_two_names(self, giver, receiver_list):
        receivers = list(receiver_list) #so that the original list can be used in recursion if checks fail
        receiver1 = random.choice(receivers)
        receivers.remove(receiver1)
        receiver2 = random.choice(receivers)
        if (giver != receiver1 and giver != receiver2):       # giver cannot be same as receiver
            receiver_list = [receiver1, receiver2]
            giver_receiver_match = GiverReceiverPair(giver,receiver_list)
            return giver_receiver_match
        else:
            return self._select_two_names(giver, receiver_list)


