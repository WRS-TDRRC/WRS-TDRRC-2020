import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS4-Semi", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
