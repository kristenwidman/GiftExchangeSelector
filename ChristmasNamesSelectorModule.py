# kwidman
# 12/1/11
# Christmas name selector

import random
from constants import exclude, preferences, DEBUG

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

    def _select_names(self, giver, receiver_list, number_receivers):
        '''Given one name (giver) and a list of receivers (all not
            yet paired), selects a receiver from the list and creates
            a GiverReceiverPair object.  Returns said object. 
        '''
        receivers = list(receiver_list)
        receiver_picks = []
        for i in range(number_receivers):
            receiver = random.choice(receivers)
            receivers.remove(receiver)
            receiver_picks.append(receiver)
        if (giver not in receiver_picks): #giver cannot be same as receiver
            giver_receiver_match = GiverReceiverPair(giver, receiver_picks)
            return giver_receiver_match
        else:
            return self._select_names(giver, receiver_list, number_receivers)

    def select_christmas_names(self, name_list, num_receivers):
        '''Main functionality - takes a list of names and returns
            a list of GiverReceiverPair objects. If only name left
            in receiver_list is == giver, this method sets the list
            to empty and calls itself again.
        '''
        giver_list = list(name_list)
        receiver_dict = {}
        list_of_giver_receivers = []
        for receiver in name_list:
            receiver_dict[receiver] = 0
        for name in giver_list:
            if ((len(receiver_dict) > num_receivers) or (len(receiver_dict) == num_receivers and name not in receiver_dict)):
                giver_receiver = self._select_names(name, receiver_dict.keys(), num_receivers)
                for receiver in giver_receiver.receiver:
                    receiver_dict[receiver] += 1
                    if receiver_dict[receiver] >= num_receivers:
                        del receiver_dict[receiver]
                list_of_giver_receivers.append(giver_receiver)
            else:
                return self.select_christmas_names(name_list, num_receivers)
        #added below check people who should NOT be giving to each other and who SHOULD be giving certain others
        if self._check_for_conflicts(list_of_giver_receivers) and self._check_for_preferences(list_of_giver_receivers):
            if DEBUG: print 'Check succeeded!'
            return list_of_giver_receivers
        else:
            if DEBUG: print 'Check failed. Repeating'
            return self.select_christmas_names(name_list, num_receivers)

    def print_pairs(self, giver_receiver_pairs):
        '''Method to print the generated giver/receiver pairs.
            Takes a GiverReceiverPair object as input.
            Returns nothing.
        '''
        for pair in giver_receiver_pairs:
            print pair.giver + " : " + repr(pair.receiver) + '\n'
        return

    def _check_for_preferences(self, g_r_list):
        '''Allows requests for a person/people to give to specific people.
            Format of preferences is like:
            [{("Rob","Linda"): ["Jeff and Kristen", "Michelle and Ryan", "Carla", "Brad"]}]
        '''
        #this will need rework to make more general
        if DEBUG: print 'checking for preferences'
        for dictionary in preferences:
            givers_expected = dictionary.keys()[0]  #tuple
            receivers_expected = dictionary.values()[0]
            receivers_expected.sort()
            receivers_actual = []
            for giver_receiver in g_r_list:
                if giver_receiver.giver in givers_expected:
                    receivers_actual += giver_receiver.receiver
            if DEBUG: print 'receivers wanted for givers ' + repr(givers_expected) + ' are ' + repr(receivers_expected)
            receivers_actual.sort()
            if DEBUG: print 'receivers actual for these givers: '+ repr(receivers_actual)
            if receivers_actual == receivers_expected:
                if DEBUG: print 'receiver lists match!'
            else:
                if DEBUG: print 'preferences check failed'
                return False
        return True

    def _check_for_conflicts(self, g_r_list):
        '''For inclusion of a list of people who should not be giving to each other
        '''
        if DEBUG: print 'checking for conflicts'
        for giver_receiver in g_r_list:
            if giver_receiver.giver in exclude:
                #if DEBUG: print 'giver %s is in exclude list'%(giver_receiver.giver)
                for receiver in giver_receiver.receiver:
                    #if DEBUG: print 'receiver ', receiver
                    if receiver in exclude[giver_receiver.giver]:
                        if DEBUG: print 'giver %s cannot give to receiver %s. Running again.'%(giver_receiver.giver, receiver)
                        return False
        return True
