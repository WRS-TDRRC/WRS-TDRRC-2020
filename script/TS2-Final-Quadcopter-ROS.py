import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS2-Final", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
