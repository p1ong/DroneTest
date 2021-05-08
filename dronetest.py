from djitellopy import Tello
import cv2
import time


def drone_test():
    ######################################################################
    width = 320  # WIDTH OF THE IMAGE
    height = 240  # HEIGHT OF THE IMAGE
    wait_time: int = 5
    ######################################################################

    # CONNECT TO TELLO
    drone = Tello()
    drone.connect()

    print("Battery =", drone.get_battery(), "%")

    # drone.streamoff()
    drone.streamon()

    # Perform a little sequence
    drone.takeoff()
    time.sleep(wait_time)
    # GET THE IMAGE FROM The Tello Drone
    frame_read = drone.get_frame_read()
    time.sleep(wait_time)
    # my_frame = frame_read.frame
    # img = cv2.resize(my_frame, (width, height))

    drone.rotate_clockwise(90)
    time.sleep(wait_time)
    drone.move_left(35)
    time.sleep(wait_time)
    drone.land()
    time.sleep(wait_time)
    drone.streamoff()

    # DISPLAY IMAGE
    # cv2.imshow("MyResult", img)
    # cv2.imshow("Drone View", frame_read.frame)
    # time.sleep(3)