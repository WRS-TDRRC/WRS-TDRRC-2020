import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS2", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
