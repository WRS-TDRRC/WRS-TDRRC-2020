import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS1", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, airDifinitionFile = "TS1-airDifinition.dat", enableVisionSimulation = True, remoteType = "ROS")
