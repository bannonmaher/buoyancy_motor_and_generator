# import the library for connecting to the relay

# import the library for accessing system resources

# create variables holding values for relay on off values

# create variables to hold the state of each relay including those controlling motors and linear actuators for the support weight extension and retraction, opening – and depending on the configuration closing – the sealable bottom compartment partition, and the buoyant weight pushing linear actuator

# create variables holding the cycle seconds for each component

# create variables to hold the relay board connection, IP address, username, and password


# create a function to update the relay board

    # establish a connection to the relay, if it has not been initialized, or has been dropped
    
    # creating a string sequence of relay states
    
    # send the states to the relay board


# define a function to run on script execution

    # retrieve the current system time

    # perform a continuous loop

        # create a variable holding seconds elapsed as the time initialized minus the current system time

        # if the remainder is zero, when seconds elapsed are divided by any of the force providing device cycle seconds, transition the corresponding force providing device(s) by changing corresponding relay state(s)
        
        # call the function to update the relay with current changes
