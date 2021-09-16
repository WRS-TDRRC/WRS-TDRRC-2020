import WRSUtil
WRSUtil.loadProject(
    "SingleSceneView", "TS2", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
