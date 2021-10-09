import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS4", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, airDifinitionFile = "TS4-airDifinition.dat", enableVisionSimulation = True, remoteType = "ROS")
