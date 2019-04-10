# File dedicated to constructing a fake user profile for tracking the allowed
# algorithms. Since the algorithms are all suppose to be known hashes this
# file will be accompanied by a known_algs.json which contains a list of
# all of the known algorithms. This file will merely select a subset of the
# known algorithms to associate with a user and provide a means to ship them

import json
import numpy as np


class AlgProfile:
    # Class take constructs the "User Profile" of allowed algorithms
    # Based upon details of known_algs.json. For now known_algs.json
    # is filled with meaningless dummy values but can hopefully soon
    # be replaced with actual algorithms and their hashes soon

    # This is really just a wrapper right now for a dictionary with
    # a method for loading JSON data.
    
    # Class variable to see if we have read the file before. If so we will
    # just load it into memory once rather than do many file reads since we
    # expect the file to be large at least initially
    is_read = False
    
    # Class variable holding a mapping of algorithm names to hashes
    alg_dict = None  

    # Default location of known algorithms relative to this file
    alg_file = "emission/simulation/known_algs.json"

    # Default value for number of algorithms
    LAMBDA_ALG = 4
    
    def __init__ (self, mean=LAMBDA_ALG):
        if not AlgProfile.is_read:
            self.read_algorithms ()
            AlgProfile.is_read = True

        self.algs = dict ()
        # Samples from a poisson distribution to get how many algorithms the user should select.
        # The choice of a poisson is arbitrary and simply because it is dependent on one parameter.
        count = round (np.random.poisson (mean))
       
        # Select up to count elements from the array
        alg_names = AlgProfile.alg_dict.keys ()
        names_array = np.array (list (alg_names))
        np.random.shuffle (names_array)
        selected_names = list (names_array) [:count]
        for name in selected_names:
            self.algs[name] = AlgProfile.alg_dict[name]


    # Method for initializing the data from the json of known algorithms
    def read_algorithms (self):
        with open (AlgProfile.alg_file, "r") as f:
            AlgProfile.alg_dict = json.load (f)