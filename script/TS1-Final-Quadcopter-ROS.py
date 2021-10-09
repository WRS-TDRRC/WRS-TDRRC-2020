import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS1-Final", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, airDifinitionFile = "TS1-Final-airDifinition.dat", enableVisionSimulation = True, remoteType = "ROS")
