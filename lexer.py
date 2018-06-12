import create

class Command:
    
    def __init__(self, trigger, description):
        self.trigger = trigger
        self.description = description
    
    def __str__(self):
        return "    '!" + self.trigger + "'" + '\t-\t' + self.description

class Lexer:
    
    MOVE = Command("forward", "Moves the robot forward")
    BACK = Command("back", "Moves the robot backward")
    ROTATE = Command("rotate", "Rotates the robot counterclockwise 45°")
    LEFT = Command("left", "Turns the robot 45° counterclockwise and moves forward")
    HARD_LEFT = Command("hard_left", "Turns the robot 90° counterclockwise and moves foward")
    RIGHT = Command("right", "Turns the robot 45° clockwise and moves foward")
    HARD_RIGHT = Command("hard_right", "Turns the robot 90° clockwise and moves forward")
    BLING = Command("blingbling", "Something awesome")
    STAR = Command("star_wars", "Something else awesome")
    MARIO = Command("mario", "Something else else awesome")
    FOLGERS = Command("folgers", "The best way to start your day")
    OLD = Command("old_spice", "The man your man can smell like")
    HELP = Command("help", "Prints available commands")
    COMMANDS = [MOVE, BACK, ROTATE, LEFT, HARD_LEFT, RIGHT, HARD_RIGHT, BLING, STAR, MARIO, FOLGERS, OLD, HELP]
    
    def __init__(self, irc, distance = 20, degrees = 45, speed = 20):
        self.irc = irc
        self.distance = distance
        self.degrees = degrees
        self.speed = speed
        self.robot = create.Create("/dev/tty.KeySerial1")
    
    def parse(self, channel, user, command):
        if (command[0].lower() == "forward"):
            self.robot.move(int(self.distance), self.speed)
        elif (command[0].lower() == "back"):
            self.robot.move(int(self.distance)*-1, self.speed)
        elif (command[0].lower() == "rotate"):
            self.robot.turn(int(self.degrees), self.speed)
        elif (command[0].lower() == "left"):
            self.robot.turn(45, self.speed)
            self.robot.move(int(self.distance), int(self.speed))
        elif (command[0].lower() == "hard_left"):
            self.robot.turn(90, self.speed)
            self.robot.move(int(self.distance), int(self.speed))
        elif (command[0].lower() == "right"):
            self.robot.turn(-45, self.speed)
            self.robot.move(int(self.distance), int(self.speed))
        elif (command[0].lower() == "hard_right"):
            self.robot.turn(-90, self.speed)
            self.robot.move(int(self.distance), int(self.speed))
        elif (command[0].lower() == "blingbling"):
            self.robot.playSong( [(62,15),(62,15),(62,15),(65,15),(64,15),(62,15),(60,15), (64,30),(60,30),(72,15),(72,15),(69,15),(69,15),(72,15),(72,15),(74,20)])
        elif (command[0].lower() == "star_wars"):
            self.robot.playSong([(79,70),(86,70),(84,12),(83,12),(81,12),(91,70),(86,40),(84,12),(83,12),(81,12),(91,70),(86,40),(84,12),(83,12),(84,12),(81,70)])
        elif (command[0].lower() == "mario"):
            self.robot.playSong([(76,15),(76,15),(76,23),(72,15),(76,20),(79,38),(67,35),(77,17),(77,17),(77,17),(76,17),(74,16),(72,15),(64,20),(64,15),(60,15)])
        elif (command[0].lower() == "folgers"):
            self.robot.playSong([(69,15),(71,50),(73,45),(73,15),(74,30),(69,30),(71,45),(69,15),(71,22),(74,26),(78,31),(76,31),(74,50)])
        elif (command[0].lower() == "old_spice"):
            self.robot.playSong([(79,8),(79,8),(81,17),(84,17),(83,17),(86,13),(88,16),(84,16)])
        elif (command[0].lower() == "help"):
            self.irc.print_help(channel)