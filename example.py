import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation, animation3D


alh = SwarmPackagePy.pso(50, tf.ackley_function, -10, 10, 2, 30)
animation(alh.get_agents(), tf.ackley_function, -10, 10)
animation3D(alh.get_agents(), tf.ackley_function, -10, 10)

