import WRSUtil
WRSUtil.loadProject(
    "SingleSceneView", "TS1", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
