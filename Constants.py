from wpimath.kinematics import SwerveDrive4Kinematics
from wpimath.geometry import Translation2d
import math
from wpimath.trajectory import TrapezoidProfileRadians
from rev import SparkMax


class AlgiIntake:
    motor_id = 33
    maxAmper = 30
    maxVolts = 6
    rampUp = 0.1
    limit_id = 2


class CorralIntake:
    motor_id = 22
    maxAmper = 30
    maxVolts = 6
    rampUp = 0.1
    limit_id = 3


class CoralSubsys:
    motor_id = 21
    deadBand = 1  # degrees
    maxVolts = 12
    maxAmper = 40
    rampUp = 0.1
    gearRatio = 80
    limit_id = 1
    kp = 1.5
    ki = 0
    kd = 0
    kf = 0
    ks = 0.1
    kv = 0.12
    ka = 0.1
    velocity = 20
    acceleration = 40
    jerk = 80
    revcoder = 7


class AlgiSubsys:
    deadband = 1  # degrees
    motor1_id = 31
    motor2_id = 32
    limit_id = 5 
    motor1_type = SparkMax.MotorType.kBrushless
    motor2_type = SparkMax.MotorType.kBrushless
    gear_ratio = 60
    convertion_factor = 360 / gear_ratio
    kp = 1 
    ki = 0
    kd = 0
    kf = 0
    maxVelocity = 20
    minVelocity = 15
    maxAcceleration = 40
    revcoder = 2


class led:
    led_port = 4
    led_length = 120


class LimeLightConstants:
    limelight_left_name = "limelight-left"
    limelight_right_name = "limelight-right"
    limelight_left_height = 0.33
    limelight_right_height = 0.33
    limelight_right_angle = 20
    limelight_left_angle = 20
    april_tag_height = []


class ModuleConstants:
    driveKS = 0.56548
    driveKV = 3.7091
    driveKA = 0.85702
    # Angle Motor PID Values
    angle_kp = 0.01
    angle_ki = 0.0
    angle_kd = 0.0
    angle_kf = 0.0
    # Drive Motor PID Values
    drive_kp = 1
    drive_ki = 0.0
    drive_kd = 0.0
    drive_kf = 1

    kWheelDiameterMeters = 0.095
    kDriveMotorGearRatio = 6.75
    kTurningMotorGearRatio = 150 / 7
    kDriveEncoderRot2Meter = kDriveMotorGearRatio * math.pi * kWheelDiameterMeters
    kTurningEncoderRot2Rad = kTurningMotorGearRatio * 2 * math.pi
    kDriveEncoderRPM2MeterPerSec = kDriveEncoderRot2Meter / 60
    kTurningEncoderRPM2RadPerSec = kTurningEncoderRot2Rad / 60
    # Drive Motor Conversion Factors #
    driveConversionPositionFactor = (
        kWheelDiameterMeters * math.pi
    ) / kDriveMotorGearRatio
    driveConversionVelocityFactor = driveConversionPositionFactor / 60.0
    angleConversionFactor = 360.0 / kTurningMotorGearRatio
    kPTurning = 0.2


class DriveConstants:
    slowDriveMultiplier = 0.4
    # Chassis
    kTrackWidth = 0.75
    kWheelBase = 0.75
    kDriveKinematics = SwerveDrive4Kinematics(
        Translation2d(kWheelBase / 2, kTrackWidth / 2),
        Translation2d(kWheelBase / 2, -kTrackWidth / 2),
        Translation2d(-kWheelBase / 2, kTrackWidth / 2),
        Translation2d(-kWheelBase / 2, -kTrackWidth / 2),
    )

    swerve_max_speed = 4

    kTeleDriveMaxAccelerationUnitsPerSecond = 3
    kTeleDriveMaxAngularAccelerationUnitsPerSecond = 3

    # FrontLeft
    kFrontLeftDriveMotorPort = 2
    kFrontLeftTurningMotorPort = 1
    kFrontLeftTurningEncoderReversed = True
    kFrontLeftDriveEncoderReversed = True
    kFrontLeftDriveAbsoluteEncoderPort = 9
    kFrontLeftDriveAbsoluteEncoderReversed = False
    kFrontLeftDriveAbsoluteEncoderOffset = 356.22072

    # FrontRight
    kFrontRightDriveMotorPort = 7
    kFrontRightTurningMotorPort = 8
    kFrontRightTurningEncoderReversed = True
    kFrontRightDriveEncoderReversed = True
    kFrontRightDriveAbsoluteEncoderPort = 10
    kFrontRightDriveAbsoluteEncoderReversed = False
    kFrontRightDriveAbsoluteEncoderOffset = 6.6798

    # BackLeft
    kBackLeftDriveMotorPort = 4
    kBackLeftTurningMotorPort = 3
    kBackLeftTurningEncoderReversed = True
    kBackLeftDriveEncoderReversed = False
    kBackLeftDriveAbsoluteEncoderPort = 12
    kBackLeftDriveAbsoluteEncoderReversed = False
    kBackLeftDriveAbsoluteEncoderOffset = 239.854

    # BackRight
    kBackRightDriveMotorPort = 5
    kBackRightTurningMotorPort = 6
    kBackRightTurningEncoderReversed = True
    kBackRightDriveEncoderReversed = False
    kBackRightDriveAbsoluteEncoderPort = 11
    kBackRightDriveAbsoluteEncoderReversed = False
    kBackRightDriveAbsoluteEncoderOffset = 62.9298

    # Constants
    kPhysicalMaxSpeedMetersPerSecond = 4.6
    kPhysicalMaxAngularSpeedRadiansPerSecond = 2 * 2 * math.pi

    kTeleDriveMaxSpeedMetersPerSecond = kPhysicalMaxSpeedMetersPerSecond / 4
    kTeleDriveMaxAngularSpeedRadiansPerSecond = (
        kPhysicalMaxAngularSpeedRadiansPerSecond / 4
    )
    kTeleDriveMaxAccelerationUnitsPerSecond = 3
    kTeleDriveMaxAngularAccelerationUnitsPerSecond = 3


class AutoConstants:
    kMaxSpeedMetersPerSecond = DriveConstants.kPhysicalMaxSpeedMetersPerSecond / 4
    kMaxAngularSpeedRadiansPerSecond = (
        DriveConstants.kPhysicalMaxAngularSpeedRadiansPerSecond / 10
    )
    kMaxAccelerationMetersPerSecondSquared = 3
    kMaxAngularAccelerationRadiansPerSecondSquared = math.pi / 4
    kPXController = 1.5
    kPYController = 1.5
    kPThetaController = 3
    kThetaControllerConstraints = TrapezoidProfileRadians.Constraints(
        kMaxAngularSpeedRadiansPerSecond, kMaxAngularAccelerationRadiansPerSecondSquared
    )


class OIConstants:
    kDriverControllerPort = 0
    kOperatorControllerPort = 1

    # stick drift values
    kStickDriftLX = 0.1
    kStickDriftLY = 0.1
    kStickDriftRX = 0.1