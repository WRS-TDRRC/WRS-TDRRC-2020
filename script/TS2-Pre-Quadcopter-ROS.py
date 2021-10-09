import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS2-Pre", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, airDifinitionFile = "TS2-Pre-airDifinition.dat", enableVisionSimulation = True, remoteType = "ROS")
