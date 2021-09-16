import WRSUtil
WRSUtil.loadProject(
    "SingleSceneView", "TS4", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
