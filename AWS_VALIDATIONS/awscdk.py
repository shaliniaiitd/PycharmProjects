import * as iam
from

'aws-cdk-lib/aws-iam';
import * as sfn
from

'aws-cdk-lib/aws-stepfunctions';
import * as tasks
from

'aws-cdk-lib/aws-stepfunctions-tasks';
import

{ActionOnFailure}
from

'aws-cdk-lib/aws-stepfunctions-tasks';
import

{Construct}
from

'constructs';
import

{CDKUtils}
from

'../lib/util/cdk_utils';
import

{Size}
from

'aws-cdk-lib';

export


class AltWeDdpConstruct extends Construct {
constructor(scope: Construct, id: string

, env: string, space: string, version: string,
ddpVersion: string) {
    super(scope, id);

const
accountId = this.node.tryGetContext('accountId');
const
subnetId = this.node.tryGetContext('subnetId');
var
masterNode = this.node.tryGetContext('masterNode');
const
masterNodes = this.node.tryGetContext('masterNodes');
var
workerNode = this.node.tryGetContext('workerNode');
var
workerNodes = this.node.tryGetContext('workerNodes');
const
customeAMIID = this.node.tryGetContext('customeAmiId');
const
emrVersion = this.node.tryGetContext('emrVersion');
var
driverMem = this.node.tryGetContext('driverMem');
var
driverCores = this.node.tryGetContext('driverCores');
var
executorMem = this.node.tryGetContext('executorMem');
var
executorCores = this.node.tryGetContext('executorCores');
var
ebsVolume = this.node.tryGetContext('ebsVolume');

// Since
there is a
limitation in
not having
2
different
context
for pre and prod; prod configs hard coded here.
if (env == 'prod') {
masterNode = "m5.xlarge";
driverCores = 4;
workerNode = "m5.xlarge";
workerNodes = 4;
executorCores = 4;
driverMem = "10g";
executorMem = "10g";
ebsVolume = 100;
}

const bucket = CDKUtils.getEMRS3Bucket(env);

// clusterRole also called as jobFlowRole
const clusterRole = iam.Role.fromRoleArn(
scope,
`we-ddp-cluster-role-${env}-${space}-${version}`,
`arn:aws: iam::${accountId}: role / EMR_EC2_DefaultRole
`,
);

const
serviceRole = iam.Role.fromRoleArn(
    scope,
    `we - ddp - service - role -${env} -${space} -${version}
`,
`arn: aws:iam::${accountId}: role / EMR_DefaultRole
`,
);

const
createCluster = new
tasks.EmrCreateCluster(this, 'Create-Cluster', {
    instances: {
        ec2SubnetId: `${subnetId}
`,
instanceFleets: [
    {
        instanceFleetType: tasks.EmrCreateCluster.InstanceRoleType.MASTER,
        name: 'master_fleet',
        targetOnDemandCapacity: masterNodes,
        instanceTypeConfigs: [
            {
                instanceType: `${masterNode}
`,
ebsConfiguration: {
    ebsBlockDeviceConfigs: [
        {
            volumeSpecification: {
                volumeSize: Size.gibibytes(ebsVolume),
                volumeType: tasks.EmrCreateCluster.EbsBlockDeviceVolumeType.GP2
            }
        }
    ]
}
},
],
},
{
    instanceFleetType: tasks.EmrCreateCluster.InstanceRoleType.CORE,
    name: 'core_fleet',
    targetOnDemandCapacity: workerNodes,
    instanceTypeConfigs: [
        {
            instanceType: `${workerNode}
`,
ebsConfiguration: {
    ebsBlockDeviceConfigs: [
        {
            volumeSpecification: {
                volumeSize: Size.gibibytes(ebsVolume),
                volumeType: tasks.EmrCreateCluster.EbsBlockDeviceVolumeType.GP2
            }
        }
    ]
}
},
],
},
],
},
clusterRole,
name: `DDP - Cluster -${env}
`,
serviceRole,
logUri: `s3: // ${bucket} / emr - logs / `,
customAmiId: `${customeAMIID}
`,
releaseLabel: `${emrVersion}
`,
applications: [
    {
        name: 'Spark',
    },
],
resultPath: '$.cluster',
});

const
connectionCalc = new
tasks.EmrAddStep(this, 'Connection-Calc', {
    actionOnFailure: ActionOnFailure.TERMINATE_CLUSTER,
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
    jar: 'command-runner.jar',
    name: 'Connection-Calc-Job',
    args: [
        'spark-submit',
        '--verbose',
        '--deploy-mode',
        'cluster',
        '--driver-java-options',
        `-Dspring.profiles.active =${env}
`,
'--conf',
'spark.yarn.maxAppAttempts=1',
'--executor-memory',
`${executorMem}
`,
'--executor-cores',
`${executorCores}
`,
'--driver-memory',
`${driverMem}
`,
'--driver-cores',
`${driverCores}
`,
'--conf',
'spark.local.dir=/mnt',
'--class',
'com.we.ccscl.Application',
`s3: // ${bucket} / application - jar / ccscl / ccscl -${ddpVersion}.jar
`,
'--process=CONNECTION_CALC',
`--space =${space}
`,
],
resultPath: '$.connection-calc',
});

const
buildSpouseDD = new
tasks.EmrAddStep(this, 'Build-Spouse-DD', {
    actionOnFailure: ActionOnFailure.TERMINATE_CLUSTER,
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
    jar: 'command-runner.jar',
    name: 'Build-Spouse-DD-Job',
    args: [
        'spark-submit',
        '--verbose',
        '--deploy-mode',
        'cluster',
        '--driver-java-options',
        `-Dspring.profiles.active =${env}
`,
'--conf',
'spark.yarn.maxAppAttempts=1',
'--executor-memory',
`${executorMem}
`,
'--executor-cores',
`${executorCores}
`,
'--driver-memory',
`${driverMem}
`,
'--driver-cores',
`${driverCores}
`,
'--conf',
'spark.local.dir=/mnt',
'--class',
'com.we.ccscl.Application',
`s3: // ${bucket} / application - jar / ccscl / ccscl -${ddpVersion}.jar
`,
'--process=BUILD_SPOUSE_DD',
`--space =${space}
`
],
resultPath: '$.build-spouse-dd',
});

const
buildFamilyDD = new
tasks.EmrAddStep(this, 'Build-Family-DD', {
    actionOnFailure: ActionOnFailure.TERMINATE_CLUSTER,
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
    jar: 'command-runner.jar',
    name: 'Build-Family-DD-Job',
    args: [
        'spark-submit',
        '--verbose',
        '--deploy-mode',
        'cluster',
        '--driver-java-options',
        `-Dspring.profiles.active =${env}
`,
'--conf',
'spark.yarn.maxAppAttempts=1',
'--executor-memory',
`${executorMem}
`,
'--executor-cores',
`${executorCores}
`,
'--driver-memory',
`${driverMem}
`,
'--driver-cores',
`${driverCores}
`,
'--conf',
'spark.local.dir=/mnt',
'--class',
'com.we.ccscl.Application',
`s3: // ${bucket} / application - jar / ccscl / ccscl -${ddpVersion}.jar
`,
'--process=BUILD_FAMILY_DD',
`--space =${space}
`
],
resultPath: '$.build-spouse-dd',
});

const
summaryCalcStep = new
tasks.EmrAddStep(this, 'Summary-Calc', {
    actionOnFailure: ActionOnFailure.TERMINATE_CLUSTER,
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
    jar: 'command-runner.jar',
    name: 'Summary-Calc-Job',
    args: [
        'spark-submit',
        '--verbose',
        '--deploy-mode',
        'cluster',
        '--driver-java-options',
        `-Dspring.profiles.active =${env}
`,
'--conf',
'spark.yarn.maxAppAttempts=1',
'--executor-memory',
`${executorMem}
`,
'--executor-cores',
`${executorCores}
`,
'--driver-memory',
`${driverMem}
`,
'--driver-cores',
`${driverCores}
`,
'--conf',
'spark.local.dir=/mnt',
'--class',
'com.we.ccscl.Application',
`s3: // ${bucket} / application - jar / ccscl / ccscl -${ddpVersion}.jar
`,
'--process=SUMMARY_CALC',
`--space =${space}
`,
],
resultPath: '$.summary-calc',
});

const
profileQualityCheck = new
tasks.EmrAddStep(this, 'Profile-Quality-Check', {
    actionOnFailure: ActionOnFailure.TERMINATE_CLUSTER,
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
    jar: 'command-runner.jar',
    name: 'Profile-Quality-Check-Job',
    args: [
        'spark-submit',
        '--verbose',
        '--deploy-mode',
        'cluster',
        '--driver-java-options',
        `-Dspring.profiles.active =${env}
`,
'--conf',
'spark.yarn.maxAppAttempts=1',
'--executor-memory',
`${executorMem}
`,
'--executor-cores',
`${executorCores}
`,
'--driver-memory',
`${driverMem}
`,
'--driver-cores',
`${driverCores}
`,
'--conf',
'spark.local.dir=/mnt',
'--class',
'com.we.ccscl.Application',
`s3: // ${bucket} / application - jar / ccscl / ccscl -${ddpVersion}.jar
`,
'--process=FILTER_WEALTHY_PROFILE',
`--space =${space}
`
],
resultPath: '$.profile-quality-check',
});

const
writePgDataset = new
tasks.EmrAddStep(this, 'Build-PG-Dataset', {
    actionOnFailure: ActionOnFailure.TERMINATE_CLUSTER,
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
    jar: 'command-runner.jar',
    name: 'Build-PG-Dataset-Job',
    args: [
        'spark-submit',
        '--verbose',
        '--deploy-mode',
        'cluster',
        '--driver-java-options',
        `-Dspring.profiles.active =${env}
`,
'--conf',
'spark.yarn.maxAppAttempts=1',
'--executor-memory',
`${executorMem}
`,
'--executor-cores',
`${executorCores}
`,
'--driver-memory',
`${driverMem}
`,
'--driver-cores',
`${driverCores}
`,
'--conf',
'spark.local.dir=/mnt',
'--class',
'com.we.ccscl.Application',
`s3: // ${bucket} / application - jar / ccscl / ccscl -${ddpVersion}.jar
`,
'--process=PG_BUILD_DATASET',
`--space =${space}
`
],
resultPath: '$.build-pg-dataset',
});

const
pgPrevBatchLoad = new
tasks.EmrAddStep(this, 'PG-Prev-Batch-Load', {
    actionOnFailure: ActionOnFailure.TERMINATE_CLUSTER,
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
    jar: 'command-runner.jar',
    name: 'PG-Prev-Batch-Load-Job',
    args: [
        'spark-submit',
        '--verbose',
        '--deploy-mode',
        'cluster',
        '--driver-java-options',
        `-Dspring.profiles.active =${env}
`,
'--conf',
'spark.yarn.maxAppAttempts=1',
'--executor-memory',
`${executorMem}
`,
'--executor-cores',
`${executorCores}
`,
'--driver-memory',
`${driverMem}
`,
'--driver-cores',
`${driverCores}
`,
'--conf',
'spark.local.dir=/mnt',
'--class',
'com.we.ccscl.Application',
`s3: // ${bucket} / application - jar / ccscl / ccscl -${ddpVersion}.jar
`,
'--process=PG_PREVIOUS_LOAD',
`--space =${space}
`
],
resultPath: '$.pg-prev-batch-load',
});

const
pgCurrBatchLoad = new
tasks.EmrAddStep(this, 'PG-Curr-Batch-Load', {
    actionOnFailure: ActionOnFailure.TERMINATE_CLUSTER,
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
    jar: 'command-runner.jar',
    name: 'PG-Curr-Batch-Load-Job',
    args: [
        'spark-submit',
        '--verbose',
        '--deploy-mode',
        'cluster',
        '--driver-java-options',
        `-Dspring.profiles.active =${env}
`,
'--conf',
'spark.yarn.maxAppAttempts=1',
'--executor-memory',
`${executorMem}
`,
'--executor-cores',
`${executorCores}
`,
'--driver-memory',
`${driverMem}
`,
'--driver-cores',
`${driverCores}
`,
'--conf',
'spark.local.dir=/mnt',
'--class',
'com.we.ccscl.Application',
`s3: // ${bucket} / application - jar / ccscl / ccscl -${ddpVersion}.jar
`,
'--process=PG_CURRENT_LOAD',
`--space =${space}
`
],
resultPath: '$.pg-curr-batch-load',
});

const
esPrevLoad = new
tasks.EmrAddStep(this, 'ES-Prev-Load', {
    actionOnFailure: ActionOnFailure.TERMINATE_CLUSTER,
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
    jar: 'command-runner.jar',
    name: 'ES-Prev-Load-Job',
    args: [
        'spark-submit',
        '--verbose',
        '--deploy-mode',
        'cluster',
        '--driver-java-options',
        `-Dspring.profiles.active =${env}
`,
'--conf',
'spark.yarn.maxAppAttempts=1',
'--executor-memory',
`${executorMem}
`,
'--executor-cores',
`${executorCores}
`,
'--driver-memory',
`${driverMem}
`,
'--driver-cores',
`${driverCores}
`,
'--conf',
'spark.local.dir=/mnt',
'--class',
'com.we.ccscl.Application',
`s3: // ${bucket} / application - jar / ccscl / ccscl -${ddpVersion}.jar
`,
'--process=ES_PREVIOUS_LOAD',
`--space =${space}
`
],
resultPath: '$.es-prev-load',
});

const
esCurrLoad = new
tasks.EmrAddStep(this, 'ES-Curr-Load', {
    actionOnFailure: ActionOnFailure.TERMINATE_CLUSTER,
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
    jar: 'command-runner.jar',
    name: 'ES-Curr-Load-Job',
    args: [
        'spark-submit',
        '--verbose',
        '--deploy-mode',
        'cluster',
        '--driver-java-options',
        `-Dspring.profiles.active =${env}
`,
'--conf',
'spark.yarn.maxAppAttempts=1',
'--executor-memory',
`${executorMem}
`,
'--executor-cores',
`${executorCores}
`,
'--driver-memory',
`${driverMem}
`,
'--driver-cores',
`${driverCores}
`,
'--conf',
'spark.local.dir=/mnt',
'--class',
'com.we.ccscl.Application',
`s3: // ${bucket} / application - jar / ccscl / ccscl -${ddpVersion}.jar
`,
'--process=ES_CURRENT_LOAD',
`--space =${space}
`
],
resultPath: '$.es-curr-load',
});

const
switchDB = new
tasks.EmrAddStep(this, 'Switch-DB', {
    actionOnFailure: ActionOnFailure.TERMINATE_CLUSTER,
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
    jar: 'command-runner.jar',
    name: 'Switch-DB-Job',
    args: [
        'spark-submit',
        '--verbose',
        '--deploy-mode',
        'cluster',
        '--driver-java-options',
        `-Dspring.profiles.active =${env}
`,
'--conf',
'spark.yarn.maxAppAttempts=1',
'--executor-memory',
`${executorMem}
`,
'--executor-cores',
`${executorCores}
`,
'--driver-memory',
`${driverMem}
`,
'--driver-cores',
`${driverCores}
`,
'--conf',
'spark.local.dir=/mnt',
'--class',
'com.we.ccscl.Application',
`s3: // ${bucket} / application - jar / ccscl / ccscl -${ddpVersion}.jar
`,
'--process=SWITCH_DB'
],
resultPath: '$.switch-db',
});

const
terminateCluster = new
tasks.EmrTerminateCluster(this, 'Terminate-Task', {
    clusterId: sfn.JsonPath.stringAt('$.cluster.ClusterId'),
});

if (env == 'prod')
{
    new
sfn.StateMachine(this, 'StateMachine', {
    stateMachineName: `DDP - Workflow -${env} -${space}
`,
definition: createCluster
.next(pgPrevBatchLoad)
.next(pgCurrBatchLoad)
.next(esPrevLoad)
.next(esCurrLoad)
.next(switchDB)
.next(terminateCluster),
});
} else {
    new
sfn.StateMachine(this, 'StateMachine', {
    stateMachineName: `DDP - Workflow -${env} -${space}
`,
definition: createCluster
.next(connectionCalc)
.next(buildSpouseDD)
.next(buildFamilyDD)
.next(summaryCalcStep)
.next(profileQualityCheck)
.next(writePgDataset)
.next(pgPrevBatchLoad)
.next(pgCurrBatchLoad)
.next(esPrevLoad)
.next(esCurrLoad)
.next(switchDB)
.next(terminateCluster),
});
}
}
}

https: // github.com / aws / aws - cdk / issues / 8599
