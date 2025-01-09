import boto3

aws_management_console=boto3.session.Session(profile_name='default')
ec2_console=aws_management_console.client(service_name='ec2')
response = ec2_console.Start_Instance(
    InstanceIds=['i-07fdf6f30662cba61']
)