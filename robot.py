import wpilib
import commands2
from RobotContainer import RobotContainer


class MyRobot(commands2.TimedCommandRobot):
    # robot
    def robotInit(self) -> None:
        self.scheduler = commands2.CommandScheduler.getInstance().enable()
        self.container = RobotContainer()
        self.auto_command = self.container.get_autonomous_command()
        self.container.swerveSubsystem.zeroHeading()
        self.container.swerveSubsystem.check_module_angle()
        self.container.getRedLEDCommand().schedule()

    def robotPeriodic(self) -> None:
        commands2.CommandScheduler.getInstance().run()

    # autonomus
    def autonomousInit(self) -> None:
        if self.auto_command is not None:
            self.auto_command.schedule()
        pass

    def autonomousPeriodic(self) -> None:
        pass

    # teleoperated
    def teleopInit(self) -> None:
        if self.auto_command is not None:
            self.auto_command.cancel()

    def disabledInit(self) -> None:
        self.container.getRedLEDCommand().schedule()
        return super().disabledInit()

    def disabledExit(self) -> None:
        self.container.getYellowLEDCommand().schedule()
        return super().disabledExit()


if __name__ == "__main__":
    wpilib.run(MyRobot)