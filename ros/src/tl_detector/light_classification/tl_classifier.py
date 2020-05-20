from styx_msgs.msg import TrafficLight
import numpy as np

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        self.color_th = 80

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        return self.predict(image)

    def predict(self, image):
        """
        image: cv2.Image (BGR)
        """
        R = image[:,:,2]
        G = image[:,:,1]
        R_area = np.sum(R == R.max())
        G_area = np.sum(G == G.max())

        prediction = TrafficLight.UNKNOWN

        if R_area >= self.color_th and G_area <= self.color_th:
            prediction = TrafficLight.RED
        elif R_area >= self.color_th and G_area >= self.color_th:
            prediction = TrafficLight.YELLOW if 0.8 <= R_area / G_area <= 1.2 else TrafficLight.RED
        elif G_area >= self.color_th:
            prediction = TrafficLight.GREEN
        else:
         prediction = TrafficLight.UNKNOWN

        if prediction == TrafficLight.RED:
            print("red")
        elif prediction == TrafficLight.YELLOW:
            print("yellow")
        elif prediction == TrafficLight.GREEN:
            print("green")
        else:
            print("unknown - clear")
        
        return prediction
