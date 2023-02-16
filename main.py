# connect classifier and servo for mnm color filtering

from servo import set_angle
from classifier import classifier

# color with according angle for servo
angles = {
        "red": 10,
        "orange": 20,
        "yellow": 30,
        "green": 40,
        "blue": 50,
        "brown": 60
    }

# take the classifier output, match with the angles dictionary and send the angle to the servo
set_angle(angles[classifier()])