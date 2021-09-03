import os
from cnoid.Util import *
from cnoid.Base import *
from cnoid.BodyPlugin import *

try:
    from cnoid.MulticopterPlugin import *
except:
    pass

try:
    from cnoid.AGXDynamicsPlugin import *
except:
    pass

try:
    from cnoid.ROSPlugin import *
except:
    pass

def loadProject(
    view, task, simulatorProjects, robotProjects,
    enableMulticopterSimulation = False, enableVisionSimulation = False, targetVisionSensors = "", remoteType = ""):

    projectdir = os.path.join(shareDirectory, "WRS2020", "project")
    
    itv = ItemTreeView.instance
    pm = ProjectManager.instance

    viewProject = SubProjectItem()
    viewProject.name = "ViewProject"
    viewProject.load(os.path.join(projectdir, view + ".cnoid"))
    RootItem.instance.addChildItem(viewProject)
    itv.setExpanded(viewProject, False)

    world = WorldItem()
    world.name = "World"
    RootItem.instance.addChildItem(world)

    taskProject = SubProjectItem()
    taskProject.name = task
    taskProject.load(os.path.join(projectdir, task + ".cnoid"))
    world.addChildItem(taskProject)
    itv.setExpanded(taskProject, False)

    if not isinstance(simulatorProjects, list):
        simulatorProjects = [ simulatorProjects ]
    for project in simulatorProjects:
        pm.loadProject(os.path.join(projectdir, project + ".cnoid"), world)

    # Deselect the simulator items except the first one
    selectedSimulatorItems = RootItem.instance.getSelectedItems(SimulatorItem)
    for i in range(1, len(selectedSimulatorItems)):
        selectedSimulatorItems[i].setSelected(False)

    if not isinstance(robotProjects, list):
        robotProjects = [ robotProjects ]

    robotOffset = 0.0

    for robotProject in robotProjects:

        loadedItems = pm.loadProject(os.path.join(projectdir, robotProject + ".cnoid"), world)
        if not loadedItems:
            continue
        robot = loadedItems[0]
        if not isinstance(robot, BodyItem):
            continue

        rootLink = robot.body.rootLink;
        p = rootLink.translation
        p[1] -= robotOffset
        rootLink.setTranslation(p)
        robot.notifyKinematicStateChange(True)
        robot.storeInitialState()
        robotOffset += 1.5

        if remoteType:
            joystickInput = SimpleControllerItem()
            joystickInput.name = robot.name + "-JoystickInput"
            mainController = robot.findItem(SimpleControllerItem)
            mainController.addChildItem(joystickInput)

            if remoteType == "ROS":
                joystickInput.setController("JoyTopicSubscriberController")
                bodyPublisher = BodyPublisherItem()
                bodyPublisher.name = "BodyPublisher"
                robot.addChildItem(bodyPublisher)

        if enableMulticopterSimulation:
            multicopterSimulator = MulticopterSimulatorItem()
            for simulator in world.getDescendantItems(SimulatorItem):
                simulator.addChildItem(multicopterSimulator.duplicate())

        if enableVisionSimulation:
            visionSimulator = GLVisionSimulatorItem()
            visionSimulator.setTargetSensors(targetVisionSensors)
            visionSimulator.setBestEffortMode(True)
            for simulator in world.getDescendantItems(SimulatorItem):
                simulator.addChildItem(visionSimulator.duplicate())

    logItem = WorldLogFileItem()
    logItem.setLogFile(task + ".log")
    logItem.setTimeStampSuffixEnabled(True)
    logItem.setRecordingFrameRate(100)
    world.addChildItem(logItem)

    pm.setCurrentProjectName(task + "-" + robotProjects[0])
