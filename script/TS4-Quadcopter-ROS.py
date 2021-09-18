import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS4", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
