import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS3-Semi", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
