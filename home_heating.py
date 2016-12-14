#import matplotlib.pyplot as plt

dt = 5                  #time step in minutes
n = int(2*24*60/dt)       #number of time steps, 24*60/dt equals 1 day
print(n)
T1 = []                 #temperatures in scenario 1 at time i * dt in F
T2 = []                 #temperatures in scenario 2 at time i * dt in F
dT_heat = 1             #change in temperature in house per time step provided by heater when on in F
dT_loss = 0.2           #change in temperature in house per time step when heater is off in F
T_fluc = 1              #variation +- in temperature allowed by thermostat in F

#Exterior Temperatures
pass

#Scenario 1 - Thermostat set to 68F constantly
T_set = 68                                      #temperature setting on thermostat in F
T1.append(68)                                   #initialize temperature at t = 0, scenario 1
for i in range(1,n):                            #cycle through n time steps
    if T1[i-1] > T_set - T_fluc:                #if heater is off at time i
        T1.append(round(T1[i-1] - dT_loss,1))   #append decreased temperature at time i to T1
        #print("heat off", T1)
    else:                                       #if heater on at time i
        T1.append(round(T1[i-1] + dT_heat,1))   #append increased temperature at time i to T1
        #print("heat on", T1)
#print("T1 = ",T1)

#Scenario 2 - Thermostat set to 68F between 7am and 10pm; 55F between 10pm and 7am
t_day_start = 7             #start of day-time thermostat setting, 24-hour clock
t_night_start = 10 + 12     #start of night-time thermostat setting, 24-hour clock
T_set_day = 68
T_set_night = 55
T2.append(68)   #list of temperatures in scenario 2 at times i in F
day = 0   #current day in scenario 2
for i in range(1,n):
    if i < (t_night_start + 24*day - 7)*dt:             #if day time
        if T2[i-1] > T_set_day - T_fluc:                #if heater off at time i
            T2.append(round(T2[i-1] - dT_loss,1))       #append decreased temperature at time i to T2
        else:                                           #if heater on at time i
            T2.append(round(T2[i-1] + dT_heat,1))       #append increased temperature at time i to T1
    else:
        if T2[i-1] > T_set_night - T_fluc:              #if heater off at time i
            T2.append(round(T2[i-1] - dT_loss,1))       #append decreased temperature at time i to T2
        else:                                           #if heater on at time i
            T2.append(round(T2[i-1] + dT_heat,1))       #append increased temperature at time i to T1
    if divmod(i/dt, 24)[1] == 0:                        #if a 24-hour period has elapsed
        day += 1                                        #increment day counter
        print("day = ",day)
#print("T2 = ",T2)

#Plots
print(len(T1))
print("Time   Temp")
for i in range(0,len(T1)):
    print(i/dt+7, T1[i], T2[i])