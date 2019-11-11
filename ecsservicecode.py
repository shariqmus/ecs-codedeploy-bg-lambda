import boto3
import cfnresponse

def handler(event, context):
    client = boto3.client('ecs')
    input = client.create_service(
        serviceName='<service-name>',
        taskDefinition='<task-definition-name>',
        loadBalancers=[
            {
                'targetGroupArn': '<target-group-arn>',
                'containerName': '<container-name>',
                'containerPort': 80
            },
        ],

        desiredCount=10,
        launchType='FARGATE',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'subnet-xxxxxxx',
                    'subnet-xxxxxxx'
                ],
                'securityGroups': [
                    'sg-xxxxxxxxxxxxxxx',
                ]
            }
        },
        deploymentController={
            'type': 'CODE_DEPLOY'
        }
    )
    cfnresponse.send(event, context, cfnresponse.SUCCESS, {}, 'none')
