from std_srvs.srv import SetBool
from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class Service(Node):
    def __init__(self):
        super().__init__("service_moving_right")
        # create the service server object
        # defines the type, name and callback function
        self.srv = self.create_service(SetBool, "moving_right", self.SetBool_callback)

        # create the publisher object
        # in this case the publisher will publish on /cmd_vel topic with a queuesize of 10 messages.
        # use the Twist module
        self.publisher_ = self.create_publisher(Twist, "cmd_vel", 10)
        # create a Twist message
        self.cmd = Twist()

    def SetBool_callback(self, request, response):
        # The callback function recives the self class parameter,
        # received along with two parameters called request and response
        # - receive the data by request
        # - return a result as response

        # Publish the message to the topic
        # As you see the name of the request parameter is data so let's do it
        if request.data == True:

            # define the linear x-axis velocity of /cmd_vel topic paramater to0.3
            self.cmd.linear.x = 0.3
            # define the angular z-axis velocity of /cmd_vel topic paramater to0.3
            self.cmd.angular.z = -0.3

            self.publisher_.publish(self.cmd)
            # We need a response
            response.success = True
            # We need another response but this time SetBool let us put an String
            response.message = "MOVING TO THE RIGHT RIGHT RIGHT!"
        if request.data == False:
            self.cmd.linear.x = 0.0
            # define the angular z-axis velocity of /cmd_vel topic paramater to0.3
            self.cmd.angular.z = 0.0

            self.publisher_.publish(self.cmd)
            response.success = False
            response.message = "It is time to stop!"

        # return the response parameters
        return response


def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    moving_right_service = Service()
    # pause the program execution, waits for a request to kill the node (ctrl+c)
    rclpy.spin(moving_right_service)
    # shutdown the ROS communication
    rclpy.shutdown()


if __name__ == "__main__":
    main()
