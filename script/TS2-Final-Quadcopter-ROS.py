import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS2-Final", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, airDifinitionFile = "TS2-Final-airDifinition.dat", enableVisionSimulation = True, remoteType = "ROS")
