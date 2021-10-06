import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS1-Final", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
