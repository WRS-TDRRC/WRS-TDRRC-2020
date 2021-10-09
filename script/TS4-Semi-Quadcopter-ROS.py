import WRSUtil
WRSUtil.loadProject(
    "MultiSceneViews", "TS4-Semi", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, airDifinitionFile = "TS4-Semi-airDifinition.dat", enableVisionSimulation = True, remoteType = "ROS")
