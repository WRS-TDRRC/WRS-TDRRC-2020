import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS1-Pre", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
