import WRSUtil
WRSUtil.loadProject(
    "SingleSceneView", "TS3", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
