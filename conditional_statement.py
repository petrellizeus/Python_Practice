a = 30
b = 30

# if else/elif
# match case
# if b < a:
#     print("a is greater than b")
# elif b == a:
#     print("b equals to a")
# else:
#     print("b is greater than a")

if b <= a:
    print("b is less than or equal to a")
else:
    print("b is greater than a")

# Logical Operator

# and, or, not

# Driver withdrawal criteria
# 1. Must be after 10pm
# 2. Driver must not be suspended and must be verified
# 3. Driver must not have outstanding
# 4. Driver has up to withdrawal amount
# 5. Drvier has valid bank account

"""
if current time is NOT more than 21:59 pm; reject;
if driver is NOT verfied OR driver is suspended; reject;
if driver has outstanding; reject;
if withdrawal amount is greater than user wallet balance; reject;
if driver bank account is NOT valid; reject;

"""
# Rider Booking Criteria
# 1. Must be online 
# 2. Must be connected to an active network provider/ data
# 3. Must be verified
# 4. Must be within booking range

"""
if rider is NOT online; reject;
if rider do NOT have internet connection; reject;
if rider is NOT verified; reject;
if rider is NOT within range; reject;

if rider is NOT offline AND rider have internet connection 
AND rider is verified AND rider is within range; accept;

"""