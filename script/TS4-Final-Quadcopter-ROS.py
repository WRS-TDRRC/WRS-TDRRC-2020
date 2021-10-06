import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS4-Final", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
