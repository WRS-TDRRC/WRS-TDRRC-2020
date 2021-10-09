import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS2-Semi", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, airDifinitionFile = "TS2-Semi-airDifinition.dat", enableVisionSimulation = True, remoteType = "ROS")
