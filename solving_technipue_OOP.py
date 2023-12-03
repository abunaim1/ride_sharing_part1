"""
Before solving a OOP project consider think about,
1. scene
2. class diagram
3. code
"""
"""
1. scene
sakib --request--> uber(dhaka jabo)
uber ---> available_drivers---yes or no
if yes ---> then some work
if no ---> no driver found
"""
"""
(
public +
private -
protected #
)
(
A class inherit to B class
A <-- B
A, B has common Factor (Association) to C
A, B --- C
)
"""
"""
2. class diagram

(class number 1)
Ride_Sharing
------------
+ company_name
- riders : list
- drivers : list
----------------
# add_rider()
# add_driver()

(class number 2)
User
----
+name
+email
-nid
------
+ display_profile()

(class number 3)
Driver
(class number 4)
Rider
(class number 5)
and so on....
"""