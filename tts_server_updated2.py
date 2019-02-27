#!/usr/bin/python

from roboy_cognition_msgs.srv import Talk


g_node=None #from MSE

# Channel event callback function
class Soncreo_TTS_class:
	def __init__(self):
		#load models
		pass
	
	def synthesize(self, message):
		#function which synthesise the text to the model!!
		pass
	
	def talk_callback(request,response):
		global g_node
		response.success=True #evtl.  return {'success':True} from Cerevoice
		g_node.get_logger().info('Incoming Text: %s' % (request.text))
		print ("Service successful")
		return response

def main(args=None):
	global g_node
	try:
		import rclpy
		from roboy_cognition_msgs.srv import Talk
	except:
		print("Roboy_cognition_msgs was not found")

	#Init Rclpy
	rclpy.init(args=args)
	
	#create node
	g_node = rclpy.create_node('minimal_service')

	#create service
	srv=g_node.create_service(Talk,'/roboy/cognition/speech/synthesis/talk',Soncreo_TTS_class.talk_callback)
	print ("Ready to /roboy/cognition/speech/synthesis/talk")

	#Speech Synthesis is ready now.
	Soncreo_TTS_class.synthesize("Speech synthesis is ready now")
	
	#loop RCLpy
	while rclpy.ok():
		rclpy.spin_once(g_node)
	
	#Destroy Service
	g_node.destroy_service(srv)
	rclpy.shutdown()

if __name__ == '__main__':
	main()

