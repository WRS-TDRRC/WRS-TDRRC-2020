import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS2", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, airDifinitionFile = "TS2-airDifinition.dat", enableVisionSimulation = True, remoteType = "ROS")
