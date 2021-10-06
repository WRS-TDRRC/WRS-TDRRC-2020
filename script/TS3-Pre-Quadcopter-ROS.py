import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS3-Pre", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
