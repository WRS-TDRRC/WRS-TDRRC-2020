import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS3-Final", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
