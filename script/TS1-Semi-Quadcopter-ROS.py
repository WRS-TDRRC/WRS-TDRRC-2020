import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS1-Semi", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
